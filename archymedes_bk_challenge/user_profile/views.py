from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = ProfileSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success': True, 'message': f'User {user.get("email", "")} created successfully'})



