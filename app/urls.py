from django.urls import path
from .views import message_list
urlpatterns = [
    # path("",)
    path('chat/<int:sender>/<int:receiver>/', message_list, name='chat'),
]
