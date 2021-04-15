from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),

    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
    path('author/<int:pk>/update/', views.BlogCommentUpdate.as_view(), name='blog-update'),
    path('author/<int:pk>/delete/', views.BlogCommentDelete.as_view(), name='blog-delete'),

    path('blog/create/', views.BlogCreate.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', views.BlogUpdate.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog-delete'),

    path('signup/', views.signup, name='signup'),

]
