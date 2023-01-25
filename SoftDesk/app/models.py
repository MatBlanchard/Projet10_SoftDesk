from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='author_projects')

    def __str__(self):
        return self.title


class Contributor(models.Model):
    PERMISSIONS_CHOICES = (
        ('author', 'author'),
        ('contributor', 'contributor'),
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')
    permission = models.CharField(max_length=255, choices=PERMISSIONS_CHOICES)
    role = models.CharField(max_length=255)

    class Meta:
        unique_together = ('project_id', 'user_id')


class Issue(models.Model):
    STATUS_CHOICES = (
        ('to-do', 'to-do'),
        ('work-in-progress', 'work-in-progress'),
        ('solved', 'solved')
    )

    TAG_CHOICES = (
        ('bug', 'bug'),
        ('improvement', 'improvement'),
        ('task', 'task')
    )

    PRIORITY_CHOICES = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, choices=TAG_CHOICES)
    priority = models.CharField(max_length=255)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='author_issues')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='assignee_issues')
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='author_comments')
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    time_created = models.DateTimeField(auto_now_add=True)
