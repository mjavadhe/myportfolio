from django.contrib import admin
from .models import Project, SocialLink

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'date_created', 'display_technologies')
    list_filter = ('is_featured', 'date_created')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('is_featured',)
    fieldsets = (
        ('اطلاعات پایه', {
            'fields': ('title', 'description', 'full_description', 'technologies', 'technologies2', 'technologies3', 'technologies4', 'is_featured')
        }),
        ('تصاویر و لینک‌ها', {
            'fields': ('image', 'url', 'github_url')
        }),
    )
    
    def display_technologies(self, obj):
        return obj.technologies[:50] + '...' if obj.technologies else '-'
    display_technologies.short_description = 'تکنولوژی‌ها'

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'icon_class')
    list_filter = ('platform',)
    search_fields = ('platform', 'url')

