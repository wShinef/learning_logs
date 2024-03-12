from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entires = topic.entry_set.order_by('-date_added')
    
