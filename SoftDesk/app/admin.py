from django.contrib import admin
from app.models import Project, Contributor, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'author_user')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'permission', 'role')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'title', 'description', 'tag', 'priority')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'author_user', 'issue', 'time_created')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
