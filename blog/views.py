from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog, BlogAuthor, BlogComment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm


def index(request):
    num_blogs = Blog.objects.all().count()
    num_author = BlogAuthor.objects.all().count()
    num_bloggers = BlogComment.objects.all().count()
    context = {
        'num_blogs': num_blogs,
        'num_author': num_author,
        'num_bloggers': num_bloggers,
    }
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogListbyAuthorView(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


class BlogDetailView(generic.DetailView):
    model = Blog


class BloggerListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description']
    success_url = '/'


class BlogCommentUpdate(UpdateView):
    model = Blog
    fields = '__all__'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return HttpResponse("Invalid username & password")

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class BlogCommentDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')


class BlogCreate(CreateView):
    model = Blog
    fields = ['name', 'author', 'description', 'post_date']
    initial = {'name': ''}


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = '__all__'


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
