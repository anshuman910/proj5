from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.
class Another(View):
    books = Book.objects.all()
    output = f"We have {len(books)} books in database"
    names = ''
    for book in books:
        names += f"We have \" {book.title} \" book in database <br> "
    print(names)

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
