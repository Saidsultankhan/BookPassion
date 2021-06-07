from django.db import models
from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from cart.forms import CartAddBookForm

from .models import Book, Category, Author
from .forms import  ReviewForm
from django.db.models import Q

class BookDetailView(View):

    def get(self, request, slug):

        book = Book.objects.get(slug=slug)


        cart_book_form = CartAddBookForm()
        return render(request, "sites/book-itself.html", {'book' : book, 'cart_book_form': cart_book_form})

    # model = Book
    # template_name = "sites/book-itself.html"
    # slug_field = 'url'

    # def get_context_data(self, **kwargs):

    #     context = super().get_context_data(**kwargs)
    #     context['star_form'] = RatingForm()
    #     return context

class AddReview(View):

    def post(self, request, pk):

        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())

class Search(ListView):

    model = Book
    template_name = 'sites/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        book = Book.objects.filter(Q(name__icontains=query))
        return book

class BooksView(ListView):

    model = Book
    queryset = Book.objects.filter(available=True)[:4]
    
    template_name = "sites/main.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context["categories"]= Category.objects.all()
        return context

class AuthorDetailView(DetailView):

    model = Author
    template_name = "sites/actor.html"
    slug_field = 'name'

class CategoryView(DetailView):

    model = Category
    template_name = 'sites/category.html'

    slug_field = 'name'