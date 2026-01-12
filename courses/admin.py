from django.contrib import admin
from .models import Category, Course, Topic, Video, Subscription

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1
    inlines = [VideoInline] 

class TopicAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'mentor', 'created_at')
    list_filter = ('category', 'mentor')
    search_fields = ('title', 'description')
    inlines = [TopicInline]

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Video)
admin.site.register(Subscription)
