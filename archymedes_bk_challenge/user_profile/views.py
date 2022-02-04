from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    """Manages user profile"""

    def get(self, request):
        """Retrieve user profiles"""

        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({'success': True, 'users': serializer.data, 'message': 'Successful'})

    def post(self, request):
        """Create a new user profile"""

        user = request.data.get('user')
        serializer = ProfileSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            'success': True, 'message': f'User profile created successfully'
        }, status=HTTP_201_CREATED)

    def put(self, request, user_id):
        """Update a user profile"""

        user_instance = get_object_or_404(Profile, pk=user_id)
        user = request.data.get('user')
        serializer = ProfileSerializer(instance=user_instance, data=user, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success': True, 'message': f'User profile updated successfully'})

    def delete(self, request, user_id):
        """Delete a user profile"""

        user_instance = get_object_or_404(Profile, pk=user_id)
        user_instance.delete()
        return Response({'success': True, 'message': f'User profile deleted successfully'})


class Custom404View(APIView):
    """Custom View for undefined endpoints"""

    data = {
        'api_docs': '/api/docs',
        'message': 'The API endpoint is not defined. Please see api docs'
    }

    def get(self, request):
        return Response(self.data, status=HTTP_404_NOT_FOUND)

    def post(self, request):
        return Response(self.data, status=HTTP_404_NOT_FOUND)

    def put(self, request):
        return Response(self.data, status=HTTP_404_NOT_FOUND)

    def delete(self, request):
        return Response(self.data, status=HTTP_404_NOT_FOUND)
