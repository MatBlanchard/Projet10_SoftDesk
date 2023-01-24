from django.db.models import Q
from rest_framework.viewsets import ModelViewSet, ViewSet
from app.models import Project, Contributor, Issue, Comment
from app.permissions import IsProjectAuthor
from app.serializers import SignupSerializer, ProjectListSerializer, ProjectDetailSerializer, ContributorSerializer, \
    IssueListSerializer, IssueDetailSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class SignupViewSet(ViewSet):
    @action(methods=['post'], detail=False)
    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        queryset = Project.objects.filter(Q(author_user=self.request.user) |
                                          Q(contributors__user=self.request.user)).distinct()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author_user=self.request.user)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class ContributorsViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['projects_pk'])

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['projects_pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project)
        return Response(serializer.data, status=201)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class IssuesViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['projects_pk'])

    def create(self, request, *args, **kwargs):
        project = Project.objects.get(id=self.kwargs['projects_pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project, author_user=self.request.user)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issues_pk'])

    def create(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=self.kwargs['issues_pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(issue=issue, author_user=self.request.user)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)




