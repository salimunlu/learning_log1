from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry    # Bu form Entry modeline bağlıdır.
        fields = ['text']  # Sadece text alanı formda yer alacak
        labels = {'text': ''}   # text alanı için bir etiket gösterilmeyecek
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # alanın genişliği 80 olacak.


class SearchForm(forms.Form):
    query = forms.CharField()

