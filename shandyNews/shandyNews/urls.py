"""shandyNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth
# from links.views import LinkListView, UserProfileDetailView, UserProfileEditView, LinkeCreateView
import links.views as lviews

urlpatterns = [
    url(r'^$', lviews.LinkListView.as_view(), name='home'),
    # url(r'^login/$', auth_views.LoginView.as_view(), {
    #     'template_name': 'templates/login.html'}, name="login"),
    # url(r'^logout/$', auth_views.LogoutView.as_view(),
    #     name="logout"),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/(?P<slug>\w+)/$', lviews.UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(lviews.UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^link/create/$', auth(lviews.LinkeCreateView.as_view()), name='link_create'),
    url(r'^link/(?P<pk>\d+)/$', lviews.LinkDetailView.as_view(),
        name='link_detail'),
]
