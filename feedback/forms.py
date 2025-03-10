from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}), label='Имя')
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}))
    feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 3, 'cols': 21}))
