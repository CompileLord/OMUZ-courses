from rest_framework import serializers
from .models import Category, Course, Topic, Video, Subscription

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    mentor_name = serializers.CharField(source='mentor.username', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ('student', 'subscribed_at')