from django.shortcuts import render
from .models import Book

def main(request):
    books = Book.objects.all()
    return render(
        request,
        'main/main.html',
        context= {"books":books}
    )
