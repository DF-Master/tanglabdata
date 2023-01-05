from django.contrib import admin

# Register your models here.

from .models import Tags, ChineseName, EnglishName, Location, Source, Principal, Reagent, ReagentInstance

# ManyToManyField
admin.site.register(Tags)

# ForeignKey




# admin.site.register(Reagent)
# admin.site.register(ReagentInstance)
## Register the Admin classes using the decorator

class ReagentInstanceInline(admin.TabularInline):
    model = ReagentInstance
    extra=0
    
class ReagentInline(admin.TabularInline):
    model = Reagent
    extra=0

@admin.register(Reagent)
class ReagentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'chinese_name',
        'english_name',
        "display_tags"
    )
    search_fields=('name','chinese_name__name','english_name__name','purchase_note','note')
    list_filter = ('source', 'tags','specification')
    inlines = [ReagentInstanceInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'chinese_name','english_name','tags')
        }),
        ('Source', {
            'fields': ('source', 'cas','specification')
        }),
        ('Others', {
            'fields': ('purchase_note','note')
        }),
    )

## Register the Admin classes for Instance using the decorator


@admin.register(ReagentInstance)
class ReagentInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status', 'register_date'
    )
    list_filter = ('status', 'register_date','principal')
    search_fields=('reagent__name','name','id','location__name','principal__first_name','principal__last_name','note')
    fieldsets = (
        (None, {
            'fields': ('reagent','name', 'id','location','principal')
        }),
        ('Availability', {
            'fields': ('status', 'register_date')
        }),
        ('Others', {
            'fields': ('note',)
        }),

    )
    
# Only one name
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ReagentInstanceInline]
  
@admin.register(ChineseName)
class ChineseNameAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    
@admin.register(EnglishName)
class EnglishNameAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    
@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    
    
# admin.site.register(Principal)
## Define the admin class
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    inlines = [ReagentInstanceInline]
    # fields = ['first_name', 'last_name']

## Register the admin class with the associated model
admin.site.register(Principal, PrincipalAdmin)
