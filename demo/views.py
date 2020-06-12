# from django.shortcuts import render

# from django.http import HttpResponse


# from django.views import View
from .models import Book

# Create your views here.
# class Another(View):
#     books = Book.objects.all()
#     output = f"We have {len(books)} books in database"
#     names = ''
#     for book in books:
#         names += f"We have \" {book.title} \" book in database <br> "
#     print(names)
#
#     def get(self, request):
#         return HttpResponse(self.output)


# def first(request):
#     return HttpResponse('First message from views')

# def first(request):
#     return render(request, 'first_temp.html')
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication

# def first(request):
#     books = Book.objects.all()
#     # return render(request, 'first_temp.html', {'data': 'This is a data from views'}
#     return render(request, 'first_temp.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
