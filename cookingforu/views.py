from typing import List
from  knox.models import AuthToken
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RecipeSerializer
from .models import Recipe
from cookingforu.models import Recipe
from  knox.models import AuthToken
from rest_framework import generics, permissions
from .serializers import UserSerializer, RegisterSerializer
@api_view(['GET'])
# Create your views here.
def index(request):
    return render(request,'cokingforu/index.html')
def recipeOverview(request):
    cookingforu_url ={
        'List':'/recipe-list/',
        'Detail View':'/recipe-detail/<int:id>/',
        'Create':'recipe-create',
        'Update':'/recipe-update/<int:id>',
        'Delete':'/recipe-delete/<int:id>',    
        
    }
    return Response(cookingforu_url);
@api_view(['GET'])
def ShowAll(request):
    Recipes = Recipe.objects.all()
    serializer = RecipeSerializer(Recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateRecipe(request):
    serializer = RecipeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()

    return Response('Items delete successfully!')


    class RegisterAPI(generics.GenericAPIView):
     serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

