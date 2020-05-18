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

        Book.objects.create(
        title = form_data['title'],
        author = form_data['author'],
        isbn = form_data['isbn'],
        year_published = form_data['year_published'],
        publisher = form_data['publisher'],
        librarian_id = request.user.librarian.id,
        library_id = form_data['library'])

        return redirect(reverse('libraryapp:books'))