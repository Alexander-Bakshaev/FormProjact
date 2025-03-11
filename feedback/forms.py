from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=7,
                           error_messages={'min_length': 'Слишком короткое имя', 'max_length': 'Слишком длинное имя', 'required': 'Обязательное поле'},
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}), label='Имя')
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}))
    feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 3, 'cols': 21}))
    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=10)