from django.urls import path
from .views import FeedbackView, UpdateFeedbackView, DoneView

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedbackView.as_view()),
    path('<int:feedback_id>/', UpdateFeedbackView.as_view()),
]
