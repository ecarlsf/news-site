from django.shortcuts import render
from django.views import generic

from .models import Link, Vote

# Create your views here.
class LinkListView(generic.ListView):
    model = Link
    template_name = 'links/link_list.html'
    queryset = Link.with_votes.all()
    paginate_by = 3
