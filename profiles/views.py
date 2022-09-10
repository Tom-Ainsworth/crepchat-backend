# External
from rest_framework.views import APIView
from rest_framework.response import Response

# Internal
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    '''View to display a list of all profiles'''
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)