from .models import BlogPost
from django.conf.urls import url, include
from rest_framework import serializers

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'