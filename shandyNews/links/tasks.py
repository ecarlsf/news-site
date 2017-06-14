from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.db.models import Count
from .models import Link

@shared_task
def rank_all():
    for link in Link.objects.annotate(votes=Count('vote')):
        link.set_rank(link.votes)
        print(link.rank_score)
