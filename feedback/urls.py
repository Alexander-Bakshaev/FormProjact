from django.urls import path
from .views import FeedbackView, UpdateFeedbackView, DoneView, ListFeedBackView, DetailFeedBackView, FeedbackViewUpdate

urlpatterns = [
    path('', FeedbackView.as_view()),
    path('done', DoneView.as_view()),
    path('all', ListFeedBackView.as_view(), name='list_feedback'),
    path('detail/<int:pk>/', DetailFeedBackView.as_view(), name='detail_feedback'),
    path('update/<int:pk>/', FeedbackViewUpdate.as_view(), name='update_feedback'),

    path('<int:feedback_id>/', UpdateFeedbackView.as_view()),
]
