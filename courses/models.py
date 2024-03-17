from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DURATION_CHOICES = (
    ('short_term', 'Short-term'),
    ('long_term', 'Long-term')
)

STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published")
)
class Course(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Tag")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_posts"
    )  
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(verbose_name="Course Content")
    date = models.DateField(verbose_name="Course Date")
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, verbose_name="Course Duration")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
               