from django.shortcuts import render
from .models import Sponsor, Image, Team , Event
from .serializers import SponsorSerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class SponsorGetView (APIView):
    def get(self,request):
        try:
            sponsors= Sponsor.objects.all()
            serializer= SponsorSerializer(sponsors, many= True)
            return Response(serializer.data)
        except Exception :
            return Response("An error has happened!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SponsorPostView (APIView):
    def post(self, request): #still has to link image table
        try:
            serializer= SponsorSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=True)
        except Exception :
            return Response("An error has happened!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SponsorDelView (APIView): #error in url
    def delete(self, request,pk):
        try:
            sponsors = Sponsor.objects.get(id=pk)
            #serializer= SponsorSerializer(sponsors)
            #return Response(serializer.data)
        except Sponsor.DoesNotExist:
            raise Http404
        sponsors.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class Events (APIView):
    def get(self, request):
        try:
            Events = Event.objects.all()
            serializer = EventSerializer(Events, many = True)
            return Response(serializer.data)
        except Exception:
            return Response("Error ", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = Event.objects.create

    #Put Method to edit existing event

    #Delete Method to delete event

class ActiveEvents (APIView):
    def get(self, request):
        try:
            Events = Event.objects.filter(status = "True")
            serializer = EventSerializer(Events, many = True)
            return Response(serializer.data)
        except Exception:
            return Response("Error ", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TeamView (APIView):
    def get (self,request):
        pass

    def post (self, request):
        pass

class TeamEditView (APIView):
    def put (self, request, pk):
        pass
    
    def delete (self, request, pk):
        pass