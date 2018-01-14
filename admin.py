from django.contrib import admin
from .models import Confession
from .models import Comment,Gang,User,Like,GangMember
from _codecs import register

class Commentlist(admin.TabularInline):
    model=Comment
class ConfessionAdmin(admin.ModelAdmin):
    inlines=[Commentlist]
class GangConfessionList(admin.TabularInline):
    model=Confession
class GangAdmin(admin.TabularInline):
    model=User
class GangList(admin.ModelAdmin):
    inlines=[GangAdmin]
    inlines=[GangConfessionList]

admin.site.register(Confession,ConfessionAdmin)
admin.site.register(Gang,GangList)
admin.site.register(Like)
admin.site.register(GangMember)