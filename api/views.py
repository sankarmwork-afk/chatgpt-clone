

from django.shortcuts import render, redirect
from.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from google import genai
import json
from .models import Chat

# Create your views here.


@login_required(login_url='/signin')
def index(request):
    chats = Chat.objects.order_by("-created_at")
    context = {"chats": chats}
    return render(request, 'chatapp/index.html', context)


def signup(request):
    if request.user.is_authenticated:
        return render(request, 'chatapp/index.html')
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username =request.POST['username']
            password =request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'chatapp/index.html')
    context = {'form': form}
    return render(request, 'chatapp/signup.html', context)

def signin(request):
    err = None
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        
        else:
            err = "Invalid Credentials"
        
        
    context = {"error": err}
    return render(request, "chatapp/signin.html", context)


def signout(request):
    logout(request )
    return render(request, 'chatapp/index.html')
def getValue(request):
    return JsonResponse('its working', safe=False)

def chat(request):

    if request.method == "POST":

        data = json.loads(request.body)

        client = genai.Client(api_key="")

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=data["message"]
            )

            answer = response.text
            Chat.objects.create(
            user_message=data["message"],
            bot_response=answer
            )

        except Exception as e:
            print("ERROR:", e)

            answer = "Sorry, the AI service is busy right now. Please try again in a moment."

        return JsonResponse({
            "response": answer
        })
    
def chat_detail(request, id):

    chat = Chat.objects.get(id=id)

    context = {
        "chat": chat
    }

    return render(
        request,
        "chatapp/chat_detail.html",
        context
    )




def new_chat(request):
    return redirect("/")
   

