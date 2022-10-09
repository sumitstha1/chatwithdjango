from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

# API View
class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        context = {
            "status_code": 200,
            "message": "Kathmandu",
            "data": serializer.data,
            "error": []
        }

        return Response(context, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
def home_page(request):
    template = 'chatapp/index.html'
    return render(request, template)

def signup(request):
    template = 'user/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, template, {'form': form})
