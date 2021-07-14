from django.db import models

class Course(models.Model):
    course = models.CharField(
        max_length=255,
        verbose_name='Название курса'
    )
    description = models.TextField()


    def __str__(self):
        return f'{self.course}'

    class Meta:
        ordering = ('-id',)


class Exercise(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='city_exercise'
    )
    exercise=models.CharField(
        max_length=100,
        verbose_name='exercise'
    )
    url = models.URLField(
        blank=True, null=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    
    def __str__(self) -> str:
        return f"{self.create_at} -- {self.exercise}"



class Exercise_file(models.Model):
    exercise_file = models.FileField(
        upload_to='files',
        verbose_name='закрепленные файлы',
        blank=True,null=True,
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='exercise_file',
    )


    def __str__(self) -> str:
        return f"{self.exercise}--{self.exercise_file}"