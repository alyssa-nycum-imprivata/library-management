import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    if request.method == 'GET':

        all_books = Book.objects.all()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        new_book = Book()
        new_book.title = form_data['title']
        new_book.author = form_data['author']
        new_book.isbn = form_data['isbn']
        new_book.year_published = form_data['year_published']
        new_book.publisher = form_data['publisher']
        new_book.librarian_id = request.user.librarian.id 
        new_book.library_id = form_data['library']

        new_book.save()

        return redirect(reverse('libraryapp:books'))