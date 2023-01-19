from rest_framework.permissions import BasePermission


class IsProjectAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author_user == request.user
