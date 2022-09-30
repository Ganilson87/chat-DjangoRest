from django.urls import path
from .views import message_list,index,chat
urlpatterns = [
    # path("",)
    path('chat/<int:sender>/<int:receiver>/', message_list, name='chat'),
    path('Send/<int:receiver>/', chat, name='chat'),
    path("", index, name="index")
]
