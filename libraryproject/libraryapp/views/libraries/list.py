import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Library, Book
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def library_list(request):
    if request.method == 'GET':
        
        all_libraries = Library.objects.all()
        all_books = Book.objects.all()

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries,
            'all_books': all_books
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        Library.objects.create(
        name = form_data['name'],
        address = form_data['address'])

        return redirect(reverse('libraryapp:libraries'))
