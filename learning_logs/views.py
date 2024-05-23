from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def check_topic_owner(topic, user):
    # make sure the topic belongs to the current user
    if topic.owner != user:
        raise Http404


def index(request):
    return render(request, "learning_logs/index.html")


# @login_required
def topics(request):
    if request.user.is_authenticated:
        user_topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    else:
        user_topics = None
    public_topics = Topic.objects.filter(public=True).order_by("date_added")
    print(public_topics)
    context = {"user_topics": user_topics, "public_topics": public_topics}
    return render(request, "learning_logs/topics_new.html", context)


# @login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.public == False:
        check_topic_owner(topic, request.user)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")

    # display blank or invalid form
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request.user)

    if request.method != "POST":
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request.user)

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        # updated form
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "form": form, "topic": topic}
    return render(request, "learning_logs/edit_entry.html", context)
