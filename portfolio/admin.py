from django.contrib import admin
from .models import Category, Project, Skill, Contact
# Register your models here.




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'technologies')


admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Contact)

