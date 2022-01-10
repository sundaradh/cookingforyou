from typing import List
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
# Create your views here.
def recipeOverview(request):
    cookingforu_url ={
        'List':'/recipe-list/',
        'Detail View':'/product-detail/<int:id>/',
        'Create':'recipe-create',
        'Update':'/recipe-update/<int:id>',
        'Delete':'/recipe-delete/<int:id>',    
        
    }
    return Response(cookingforu_url);