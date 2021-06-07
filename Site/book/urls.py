from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('', views.BooksView.as_view(), name="main_page"),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name="book_itself"),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
    path('search/', views.Search.as_view(), name="search-lis"),
    path('author/<str:slug>', views.AuthorDetailView.as_view(), name="author_itself"),
    path('category/<str:slug>', views.CategoryView.as_view(), name="category_itself"),
]