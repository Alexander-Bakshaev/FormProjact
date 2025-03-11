from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View


class FeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        else:
            return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedbackView(View):
    def get(self, request, feedback_id):
        feed = Feedback.objects.get(id=feedback_id)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, feedback_id):
        feed = Feedback.objects.get(id=feedback_id)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{feedback_id}')
        else:
            return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')
