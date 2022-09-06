from django.contrib import admin

from .models import Glasses,Contact,User,Organisation,Userorg
# Register your models here.
admin.site.register(Glasses),
admin.site.register(Contact),
admin.site.register(User),

@admin.register(Organisation)
class OrgAdmin(admin.ModelAdmin):
    list_display=["name","city", "created", "modified"]



@admin.register(Userorg)
class UserRoleAdmin(admin.ModelAdmin):
    list_display=["role","user","organisation","created", "modified"]

    


