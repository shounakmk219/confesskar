from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime
from django.contrib.auth.models import User

@python_2_unicode_compatible    
class Gang(models.Model):
    name=models.TextField(max_length=20)
    admin=models.ForeignKey(User)
    member_count=models.IntegerField(default=1)
    def __str__(self):
        return self.name   
@python_2_unicode_compatible
class Confession(models.Model):
    host_group=models.ForeignKey(Gang)
    user=models.ForeignKey(User)
    entry= models.TextField()
    likes= models.IntegerField(default=0)
    date= models.DateTimeField(default=datetime.now, blank=True)
    comment_count=models.IntegerField(default=0)
    def __str__(self):
        return self.entry[:10]+'...'
@python_2_unicode_compatible    
class Comment(models.Model):
    user=models.ForeignKey(User)
    confession= models.ForeignKey(Confession)
    text= models.TextField()
    likes= models.IntegerField(default=0)
    date= models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.text[:10]+'...'
@python_2_unicode_compatible 
class Like(models.Model):
    user=models.ForeignKey(User)
    like_list=models.ManyToManyField(Confession)
    def __str__(self):
        return self.user.username
    
@python_2_unicode_compatible 
class GangMember(models.Model):
    gang=models.ForeignKey(Gang)
    members=models.ManyToManyField(User)
    def __str__(self):
        return self.gang.name