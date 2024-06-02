from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = "learning_logs"
urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    path(
        "about/",
        TemplateView.as_view(template_name="learning_logs/creation_process.html"),
        name="about",
    ),
    path("add_comment/<int:entry_id>/", views.add_comment, name="add_comment"),
]
