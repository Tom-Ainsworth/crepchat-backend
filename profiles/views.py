# External
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


# Internal
from .models import Profile
from .serializers import ProfileSerializer
from CrepChat.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    '''View to display a list of all profiles'''
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request':request})
        return Response(serializer.data)
    

class ProfileDetail(APIView):
    '''View to retrieve and update a profile'''
    
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request':request})
        self.check_object_permissions(self.request, profile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request':request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    