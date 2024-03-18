from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Course, Comment

class TestCourseViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.course = Course.objects.create(
            title="Course Title",
            author=self.user,
            slug="course-title",
            excerpt="Course Excerpt",
            content="Course Content",
            status=1
        )
        self.comment = Comment.objects.create(
            course=self.course,
            author=self.user,
            body="Test Comment",
            approved=True
        )

    def test_comment_edit(self):
        response = self.client.get(reverse('comment_edit', args=['course-title', self.comment.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect because it's a POST request

    def test_comment_delete(self):
        response = self.client.get(reverse('comment_delete', args=['course-title', self.comment.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect because it's a POST request

    def test_course_detail(self):
        response = self.client.get(reverse('course_detail', args=['course-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Course Title", response.content)
        self.assertIn(b"Course Content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertIn(self.comment.body.encode(), response.content)

    def test_search_results(self):
        response = self.client.get(reverse('search_results') + '?q=Course')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Course Title", response.content)