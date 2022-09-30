from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import mensagem
from .serializers import MessageSerializer
# Create your views here.


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        #  id_user_auth = request.user
        # messages = mensagem.objects.filter(emissor_id=id_user_auth, receptor_id=receiver, is_read=False)
        messages = mensagem.objects.filter(emissor_id=sender, receptor_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# def listaChat(request):

    
#     return JsonResponse(serializer.data, safe=False)

def index(request, sender=None, receiver=None):
    recevers = User.objects.all().filter(is_active=True )

    context = {
        "receiver":recevers,
    }
    return render(request,"index.html", context=context)
def chat(request):
    
    return render (request,"chat.html")