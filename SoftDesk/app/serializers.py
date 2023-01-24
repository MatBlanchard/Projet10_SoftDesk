from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app.models import Project, Contributor, Issue, Comment
from django.contrib.auth import get_user_model


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def save(self):
        user_model = get_user_model()
        user = user_model(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'}
            )
        user.set_password(password)
        user.save()
        return user


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']
        read_only_fields = ('author_user',)


class ProjectDetailSerializer(ModelSerializer):
    issues = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user', 'issues']
        read_only_fields = ('author_user',)

    @staticmethod
    def get_issues(instance):
        queryset = Issue.objects.filter(project_id=instance.id)
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'permission', 'role']


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'time_created', 'title', 'description', 'tag', 'priority', 'status', 'author_user',
                  'assignee_user']
        read_only_fields = ('author_user',)


class IssueDetailSerializer(ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['id', 'time_created', 'title', 'description', 'tag', 'priority', 'status', 'author_user',
                  'assignee_user', 'comments']
        read_only_fields = ('author_user',)

    @staticmethod
    def get_comments(instance):
        queryset = Comment.objects.filter(issue_id=instance.id)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'time_created', 'description', 'author_user']
        read_only_fields = ('author_user',)





