from django.shortcuts import render_to_response,render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .forms import UserForm,UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import View
from .models import Confession,Like,Comment,Gang,GangMember
from django.views import generic
from django.contrib.auth.models import User,Group

class Welcome(generic.ListView):
    template_name='confess/confdisp.html'
    context_object_name='all_confessions'
    def get_queryset(self):
        return Confession.objects.all

class GangPage(generic.DetailView):
    template_name='confess/gangpage.html'
    model=Gang

class Confession_disp(generic.DetailView):
    model=Confession
    template_name='confess/newcmntdisp.html'

def Comment_entry(request, confession_id):
    con_host=Confession.objects.get(pk=confession_id)
    user_host=request.user
    if user_host.is_authenticated:
        if(request.method=='POST'):
            cur_user=request.user
            user_like=Like.objects.get(user=cur_user)
            conf_set=user_like.like_list.all()
            if(request.POST.get('like')):
                if(con_host in conf_set):
                    user_like.like_list.remove(con_host)                 
                else:
                    user_like.like_list.add(con_host)
                con_host.likes=con_host.like_set.count()
                con_host.save()
                user_like.save()   
            if(request.POST.get('entry')!=''):
                new_com=Comment()
                new_com.user=user_host
                new_com.confession=con_host
                new_com.text=request.POST.get('entry')
                new_com.save()
                con_host.comment_count=con_host.comment_set.count()
                con_host.save()
        return HttpResponseRedirect(reverse('confess:Confession',args=(confession_id,)))
    else: 
        return redirect('confess:Login')

def Confession_entry(request, gang_id):
    user=request.user
    if user.is_authenticated:
        if user in (GangMember.objects.get(gang=Gang.objects.get(pk=gang_id))).members.all():
            if(request.method=='POST'):
                if(request.POST.get('entry')!=''):
                    new_confess=Confession()
                    new_confess.user=user
                    new_confess.entry=request.POST.get('entry')
                    new_confess.host_group=Gang.objects.get(pk=gang_id)
                    new_confess.save()
            return HttpResponseRedirect(reverse('confess:GangPage',args=(gang_id,)))
        return redirect('confess:Welcome')
    else: 
        return redirect('confess:Login')
        
    

class UserFormInput(View):
    form_class= UserForm
    form_template= 'confess/registration.html'
    
    def get(self,request):
        form= self.form_class(None)
        return render(request,self.form_template,{'form':form})
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            likefield=Like()
            user.save()
            likefield.user=user
            likefield.save()
            
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('confess:Welcome')
        return render(request,self.form_template,{'form':form})


def GangForm(request):
    admin=request.user
    if admin.is_authenticated():
        if(request.method=='POST'):
            if(request.POST.get('gangname')!=''):
                new_gang=Gang()
                new_gang.admin=admin
                new_gang.name=request.POST.get('gangname')
                new_gang.save()
                new_members=GangMember()
                new_members.gang=Gang.objects.get(name=new_gang.name)
                new_members.save()
                gangmem=GangMember.objects.get(gang=new_gang)
                gangmem.members.add(request.user)
                gangmem.save()
                return HttpResponseRedirect(reverse('confess:GangPage',args=(new_gang.id,)))
        return HttpResponseRedirect(reverse('confess:NewGang'))
    else:
        return redirect('confess:Login')

def DeleteGang(request,gang_id):
    admin=request.user
    gang=Gang.objects.get(pk=gang_id)
    gangmember=GangMember.objects.get(gang=gang)
    if admin.is_authenticated():
        if gang.admin==admin:
            if(request.method=='POST'):
                for confession in gang.confession_set.all():
                    confession.host_group=Gang.objects.get(name='universal')
                    confession.save()
                gang.delete()
                return redirect('confess:Welcome')
        return HttpResponseRedirect(reverse('confess:GangPage',args=(gang_id,)))
    else:
        return redirect('confess:Login')
def AddGangMember(request,gang_id):
    admin=request.user
    gang=Gang.objects.get(pk=gang_id)
    gangmember=GangMember.objects.get(gang=gang)
    member=User.objects.get(username=request.POST.get('newmember'))
    if admin.is_authenticated():
        if gang.admin==admin:
            if(request.method=='POST'):
                if(member in gangmember.members.all()):
                    pass
                else:
                    gangmember.members.add(member)
                    gangmember.save()
                gang.member_count=gangmember.members.count()
                gang.save()
        return HttpResponseRedirect(reverse('confess:GangPage',args=(gang_id,)))
    else:
        return redirect('confess:Login')


def RemoveGangMember(request,gang_id):
    admin=request.user
    gang=Gang.objects.get(pk=gang_id)
    gangmember=GangMember.objects.get(gang=gang)
    member=User.objects.get(username=request.POST.get('oldmember'))
    if admin.is_authenticated():
        if gang.admin==admin:
            if(request.method=='POST'):
                if(member in gangmember.members.all()):
                    for confession in gang.confession_set.all():
                        if(confession.user == member):
                            confession.host_group=Gang.objects.get(name='universal')
                            confession.save()
                    gangmember.members.remove(member)
                    if member==gang.admin: 
                        newadmin=gangmember.members.all()                     
                        gang.admin=newadmin[0]
                    gangmember.save()
                gang.member_count=gangmember.members.count()
                gang.save()
        return HttpResponseRedirect(reverse('confess:GangPage',args=(gang_id,)))
    else:
        return redirect('confess:Login')



