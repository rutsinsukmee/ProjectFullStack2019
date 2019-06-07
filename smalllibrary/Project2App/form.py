from django.forms import ModelForm
from .models import Publisher, Binding, Book, Borrow, Transaction

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        exclude = ['id']

class BindingForm(ModelForm):
    class Meta:
        model = Binding
        fields = '__all__'
        exclude = ['id']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['id']

class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'
        exclude = ['id']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['id']