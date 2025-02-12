from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_user = get_user_model().objects.create_user(
            username=validated_data['username'],
         
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user 
        
class VerySimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "profile_picture"]

class BlogSerializer(serializers.ModelSerializer):
    author = VerySimpleUserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__' 

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'profile_picture', 'email', 'job_title', 'facebook', 'twitter', 'instagram', 'youtube', 'username', 'bio']

class UserInfoSerializer(serializers.ModelSerializer):
    author_post = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ["id", "username", 'first_name', 'last_name', "job_title", "bio",  'profile_picture', "author_post"] 

    def get_author_post(self, obj):
        blogs = Blog.objects.filter(author=obj)[:9]
        serializer= BlogSerializer(blogs, many=True)
        return serializer.data
        