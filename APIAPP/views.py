from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import constructserialiser,featureserialiser,contactserialiser
# from rest_framework import viewsets
from .models import construction, feature, contact
    
    

@api_view(['GET'])
def getnotes(request):
    construct = construction.objects.all()
    serialiser = constructserialiser(construct, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def getfeatures(request):
    keyfeature = feature.objects.all()
    serialiser = featureserialiser(keyfeature, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def note(request,pk):
    construct = construction.objects.get(id=pk)
    serialiser = constructserialiser(construct, many=False)
    return Response(serialiser.data)

@api_view(['PUT'])
def noteupdate(request,pk):
    data = request.data
    note = construction.objects.get(id = pk)
    serialiser = constructserialiser(instance = note, data = data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.date)

@api_view(['DELETE'])
def deletenote(request, pk):
    note = construction.objects.get(id = pk)
    note.delete()
    return Response('note was deleted')

@api_view(['POST'])
def createnote (request):
    data = request.data
    note = construction.objects.create(
        body = data['body']
    )
    serialiser = constructserialiser(note, many=False)
    return Response(serialiser.data)