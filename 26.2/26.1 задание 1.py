class CourseSerializer(serializers.ModelSerializer):
      lessons = LessonSerializer(many=True)

      class Meta:
          model = Course
          fields = ['id', 'name', 'lessons']

