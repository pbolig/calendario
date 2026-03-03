from rest_framework import serializers
from .models import Category, Event, StickyNote, Calendar

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'name', 'description', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'calendar', 'name', 'color']

class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Event
        fields = ['id', 'calendar', 'date', 'category', 'category_name', 'description']

class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyNote
        fields = ['id', 'calendar', 'text', 'color', 'created_at']
