from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Link, Vote, UserProfile
from .forms import UserProfileForm, LinkForm

# Create your views here.
class LinkListView(generic.ListView):
    model = Link
    template_name = 'links/link_list.html'
    queryset = Link.with_votes.all()
    paginate_by = 3

class UserProfileDetailView(generic.DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user})

class LinkeCreateView(CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()

        return super(CreateView, self).form_valid(form)

class LinkDetailView(generic.DetailView):
    model = Link
