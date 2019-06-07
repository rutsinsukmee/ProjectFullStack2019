from django.shortcuts import render
from .models import Publisher, Binding, Book, Borrow, Transaction
from .form import PublisherForm, BindingForm, BookForm, BorrowForm, TransactionForm
# Create your views here.

def list_book(request):
    context = dict()
    context['books'] = Book.objects.all().order_by('title')
    return render(request, 'listbook.html', context)

def borrow_book(request):
    context = dict()
    borrowed_books = Borrow.objects.all().values_list('book__id', flat=True)
    book = Book.objects.all().exclude(id__in=borrowed_books)
    if book.count():
        context['books'] = book
    return render(request, 'borrowedbook.html', context)

def transaction_book(request):
    context = dict()
    context['transactions'] = Transaction.objects.all().order_by('created')
    return render(request, 'transactionbook.html', context)

def isavailable_borrow_book(request):
    context = dict()
    t = Transaction.objects.filter(book__isavailable=True)
    for i in t:
        b = Book.objects.filter(pk=i.book.pk)
        b.update(isavailable=False)

def isavailable_return_book(request):
    context = dict()
    t = Transaction.objects.filter(book__isavailable=False)
    for i in t:
        b = Book.objects.filter(pk=i.book.pk)
        b.update(isavailable=True)

