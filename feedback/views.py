from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         else:
#             return render(request, 'feedback/feedback.html', context={'form': form})

class FeedbackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def post(self, request):
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect('/done')
    #     else:
    #         return render(request, 'feedback/feedback.html', context={'form': form})


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


# class ListFeedBackView(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedbacks'] = Feedback.objects.all()
#         return context


class ListFeedBackView(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'


# class DetailFeedBackView(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedback_id = kwargs['feedback_id']
#         feedback = Feedback.objects.get(id=feedback_id)
#         context['feedback'] = feedback
#         return context

class DetailFeedBackView(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Спасибо'
        return context
