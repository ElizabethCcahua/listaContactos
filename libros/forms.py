from django import forms
from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'rating', 'text', 'comments']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'comments': forms.Textarea(attrs={'rows': 3}),
        }
