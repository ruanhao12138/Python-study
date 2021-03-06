from django.contrib import admin
from .models import Object_list_current, Objects


class AllModelAdmin(admin.ModelAdmin):
    #list_display = ['Object_ID', 'Object_name', 'Observer', 'Obj_RA', 'Obj_DEC', 'prioriy']
    class Meta:
        model = Objects

class CurrentModelAdmin(admin.ModelAdmin):
    #list_display = ['Object_ID', 'Obs_date_current', 'Obs_timewindow_begin', 'Obs_timewindow_end', 'Obs_complete_stage', 'mode']
    class Meta:
        model = Object_list_current

admin.site.register(Objects, AllModelAdmin)
admin.site.register(Object_list_current, CurrentModelAdmin)