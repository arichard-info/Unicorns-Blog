from django import forms

from .models import Article, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content',)
        widgets = {
        	'author': forms.TextInput(attrs={'placeholder': 'Pseudo'}),
            'content': forms.Textarea(
                attrs={
                'placeholder': 'Contenu',
                'rows': 4,
                }),
        }