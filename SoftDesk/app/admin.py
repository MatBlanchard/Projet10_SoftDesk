from django.contrib import admin
from django.contrib.auth import get_user_model

from app.models import Project, Contributor, Issue, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

    class Meta:
        model = get_user_model()


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'description', 'author_user')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'permission', 'role')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_user', 'project', 'title', 'description', 'tag', 'priority', 'status')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'author_user', 'issue', 'time_created')


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
