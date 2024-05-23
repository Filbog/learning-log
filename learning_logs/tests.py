from django.test import TestCase
from django.urls import reverse
from .models import Topic, Entry
from django.contrib.auth import get_user_model


# Create your tests here.

# test if one user can access and/or edit other user's topic
# test if one user can access and/or edit other user's entry

User = get_user_model()


class TopicsViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(
            username="otheruser", password="otherpass"
        )
        self.client.login(username="testuser", password="testpass")
        self.private_topic = Topic.objects.create(
            text="Test Private Topic", owner=self.user
        )
        self.public_topic = Topic.objects.create(
            text="Test Public Topic", owner=self.user, public=True
        )

    def test_page_loads_correctly(self):
        response = self.client.get(reverse("learning_logs:topics"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/topics_new.html")

    def test_topics_displayed_for_logged_in_user(self):
        response = self.client.get(reverse("learning_logs:topics"))
        self.assertContains(response, "Test Public Topic")
        self.assertContains(response, "Test Private Topic")

    def test_topics_displayed_for_not_logged_in_user(self):
        self.client.logout()
        response = self.client.get(reverse("learning_logs:topics"))
        self.assertContains(response, "Test Public Topic")
        self.assertNotContains(response, "Test Private Topic")

    def test_topics_for_different_user(self):
        self.client.logout()
        self.client.login(username="otheruser", password="otherpass")
        response = self.client.get(reverse("learning_logs:topics"))
        self.assertContains(response, "Test Public Topic")
        self.assertNotContains(response, "Test Private Topic")


class SingleTopicAndEntryViewTests(TestCase):

    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="testpass1")
        self.user2 = User.objects.create_user(username="user2", password="testpass2")

        # Create topics
        self.topic1 = Topic.objects.create(text="User1 Topic", owner=self.user1)
        self.topic2 = Topic.objects.create(text="User2 Topic", owner=self.user2)
        self.public_topic = Topic.objects.create(
            text="Public Topic", owner=self.user2, public=True
        )

        # Create entries
        self.entry1 = Entry.objects.create(topic=self.topic1, text="User1 Entry")
        self.entry2 = Entry.objects.create(topic=self.topic2, text="User2 Entry")
        self.public_entry = Entry.objects.create(
            topic=self.public_topic, text="Public Entry"
        )

    def test_view_own_topic(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.topic1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User1 Topic")
        self.assertContains(response, "User1 Entry")

    def test_cannot_view_other_users_private_topic(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.topic2.id])
        )
        self.assertEqual(response.status_code, 404)

    def test_view_public_topic(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.public_topic.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Public Topic")
        self.assertContains(response, "Public Entry")

    def test_view_own_entry(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.topic1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User1 Entry")

    def test_cannot_view_other_users_private_entry(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.topic2.id])
        )
        self.assertEqual(response.status_code, 404)

    def test_view_public_entry(self):
        self.client.login(username="user1", password="testpass1")
        response = self.client.get(
            reverse("learning_logs:topic", args=[self.public_topic.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Public Entry")
