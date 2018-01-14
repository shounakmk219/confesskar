from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
app_name='confess'
urlpatterns=[
		url(r'^$',login_required(views.Welcome.as_view()), name='Welcome'),
        url(r'^signup/$',views.UserFormInput.as_view(),name='Signup'),
        url(r'^login/$',auth_views.login, {'template_name':'confess/login.html'},name='Login'),
        url(r'^logout/$',auth_views.logout,{'next_page':'/main/login'},name='Logout'),
        url(r'^(?P<pk>[0-9]+)/$',login_required(views.Confession_disp.as_view()),name='Confession'),
        url(r'^(?P<confession_id>[0-9]+)/comments/$',views.Comment_entry,name='Comment'),
        url(r'^(?P<gang_id>[0-9]+)/confession/$',views.Confession_entry,name='Confess'),
        url(r'^(?P<gang_id>[0-9]+)/addmember/$',views.AddGangMember,name='AddMember'),
        url(r'^gang/(?P<pk>[0-9]+)/$',views.GangPage.as_view(),name='GangPage'),
        url(r'^(?P<gang_id>[0-9]+)/removemember/$',views.RemoveGangMember,name='RemoveMember'),
        url(r'^newgang/$',views.GangForm,name='NewGang'),
        url(r'^(?P<gang_id>[0-9]+)/deletegang/$',views.DeleteGang,name='DeleteGang'),
	]
