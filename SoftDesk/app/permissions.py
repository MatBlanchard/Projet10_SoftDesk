from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission
from app.models import Project, Issue, Comment


class ProjectPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'list']:
            return obj.contributors.filter(user=request.user).exists() or obj.author_user == request.user
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.author_user


class ContributorPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user and request.user.is_authenticated:
            return False
        try:
            project = Project.objects.get(pk=view.kwargs['projects_pk'])
        except ObjectDoesNotExist:
            return False
        if view.action in ['retrieve', 'list']:
            return project.contributors.filter(user=request.user).exists() or project.author_user == request.user
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user == project.author_user


class IssuePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user and request.user.is_authenticated:
            return False
        try:
            project = Project.objects.get(pk=view.kwargs['projects_pk'])
        except ObjectDoesNotExist:
            return False
        if view.action in ['list', 'create']:
            return project.contributors.filter(user=request.user).exists() or project.author_user == request.user
        try:
            issue = Issue.objects.get(pk=view.kwargs['pk'])
        except ObjectDoesNotExist:
            return False
        if view.action == 'retrieve':
            return issue.assignee_user == request.user or issue.author_user == request.user
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == issue.author_user


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user and request.user.is_authenticated:
            return False
        try:
            project = Project.objects.get(pk=view.kwargs['projects_pk'])
        except ObjectDoesNotExist:
            return False
        if view.action in ['create', 'retrieve', 'list']:
            return project.contributors.filter(user=request.user).exists() or project.author_user == request.user
        try:
            comment = Comment.objects.get(pk=view.kwargs['pk'])
        except ObjectDoesNotExist:
            return False
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user == comment.author_user
