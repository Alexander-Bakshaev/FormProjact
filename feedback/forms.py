from django import forms
from .models import Feedback
from django.core.exceptions import ValidationError


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг'
        }
        error_messages = {
            'name': {
                'min_length': 'Слишком короткое имя',
                'max_length': 'Слишком длинное имя',
                'required': 'Обязательное поле',
            },
            'surname': {
                'min_length': 'Слишком короткая фамилия',
                'max_length': 'Слишком длинная фамилия',
                'required': 'Обязательное поле',
            },
            'rating': {
                'min_value': 'Слишком низкий рейтинг',
                'max_value': 'Слишком высокий рейтинг',
                'required': 'Обязательное поле',
            },

        }
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 3, 'cols': 21}),
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 10:
            raise ValidationError('Рейтинг должен быть от 1 до 10.')
        return rating