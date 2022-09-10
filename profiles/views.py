# External
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# Internal
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    '''View to display a list of all profiles'''
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    

class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            profile=Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)