from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from django.contrib.auth import authenticate, login, logout
from app.models import Project
from app.serializers import ProjectSerializer, SignupSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class SignupViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username, 'first_name': user.first_name,
                             'last_name': user.last_name, 'email': user.email})
        return Response(serializer.errors, status=400)


class LoginViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Successfully logged in.'})
        else:
            return Response({'message': 'Invalid credentials'}, status=401)


class LogoutViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out.'})


class ProjectViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.filter(author_user=self.request.user)
        return queryset
