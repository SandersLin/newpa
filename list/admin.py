from django.contrib import admin

from . models import Admission, Item

# Register your models here.

class ItemInline(admin.TabularInline):
	model = Item
	extra = 1


class ItemAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Content', {'fields': ['done','admission', 'content']}),
        ('Alarms', {'fields': ['start_time','stop_time','alert_time']}),
        ('Status', {'fields': ['priority','color']}),

    ]
	list_display =['done','content','admission','start_time','priority']
	list_filter = ['done','start_time']


class AdmissionAdmin(admin.ModelAdmin):
	fieldsets = [
	    ('Basic information', {'fields': ['name', 'age', 'sex','bed_number','chart_id','admission_date','discharged']}),
	    ('Admission diagnosis', {'fields': ['diagnosis','secondary_diagnosis']}),
	    ('Data', {'fields': ['memo']}),
	    ('Notes', {'fields': ['progress_note','admission_note','weekly_summary','discharge_note']}),
	]
	inlines = [ItemInline]
	list_display = ['bed_number','name','admission_date','diagnosis','discharged']
	list_filter = ['discharged']
	search_fields = ['diagnosis','name']






admin.site.register(Admission,AdmissionAdmin)	
admin.site.register(Item, ItemAdmin)