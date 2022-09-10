from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile

class ProfileList(APIView):
    '''View to display a list of all profiles'''
    
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)