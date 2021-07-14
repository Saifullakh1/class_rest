from django.db.models import fields
from rest_framework import serializers
from cources.models import *
from django.contrib.auth.models import User


class CourseListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = ('course', 'description')



class ExerciseListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Exercise
        fields = ('course','exercise','url','end_at')


class Exercise_fileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise_file
        fields = ('exercise_file')