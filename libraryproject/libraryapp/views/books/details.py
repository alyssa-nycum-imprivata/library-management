import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection


def get_book(book_id):
    
    return Book.objects.get(pk=book_id)

@login_required
def book_details(request, book_id):

    book = get_book(book_id)

    if request.method == 'GET':

        template_name = 'books/detail.html'
        return render(request, template_name, {'book': book})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            book.title = form_data['title']
            book.author = form_data['author']
            book.isbn = form_data['isbn']
            book.year_published = form_data['year_published']
            book.publisher = form_data['publisher']
            book.librarian_id = request.user.librarian.id 
            book.library_id = form_data['library']

            book.save()

            return redirect(reverse('libraryapp:book', args=[book.id]))
    
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            book.delete()

            return redirect(reverse('libraryapp:books'))
