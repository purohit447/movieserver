from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import data
from . serializers import dataSerializer
from django.db.models import Q
class dataList(APIView):
    def get(self, request, movie_id = None):
        genre_mapping = {
            'romance': 'Romance',
            'horror': 'Horror',
            'comedy': 'Comedy',
            'thriller': 'Thriller',
            'drama': 'Drama',
            'mystery': 'Mystery',
            'war': 'War',
        }
        if movie_id is None:
            getquery = data.objects.all()
        elif movie_id == 'toprated':
            # Filter movies with rating above 8.5
            getquery = data.objects.filter(IMDBrating__gt=8.5)
        elif movie_id == 'trending':
            # Filter movies with rating above 8.9 and released after 2022
            getquery = data.objects.filter(IMDBrating__gt=8.1, releasedyear__gt=2010)
        elif movie_id in genre_mapping:
            genre = genre_mapping[movie_id]
            # Filter movies where the Genre field contains the genre name
            getquery = data.objects.filter(Q(genre__contains=genre) | Q(genre__startswith=genre + ',') | Q(genre__endswith=',' + genre) | Q(genre__icontains=', ' + genre + ',')) 
        else:
            getquery = data.objects.filter(movie_id=movie_id)
        serializer = dataSerializer(getquery, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, movie_id):
        # Get the data object based on the user_id
        data_object = get_object_or_404(data, movie_id=movie_id)

        # Update the data object with the new data from the request
        serializer = dataSerializer(data_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, movie_id):
        # Get the data object based on the user_id
        data_object = get_object_or_404(data, movie_id=movie_id)

        # # Delete the data object
        data_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)