from django.shortcuts import render
from .models import *
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

class ObtainAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# articles list
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, View): 
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    # retreive all articles
    def get_queryset(self):

        conditions = {
            'title': self.request.GET.get('title', None),
            'content': self.request.GET.get('content', None),
            'author': self.request.GET.get('author', None),
            }

        conditions = {
            key: val for key, val in conditions.items() if val is not None
        }

        articles = Article.objects.filter(**conditions)

        if not articles.exists():
            raise Http404()
        return articles

class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        profile = models.Profile(user=user, nickname=request.POST.get['nickname'])

        user.save()
        profile.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

# Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# Register new user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer