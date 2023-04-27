from django.contrib import admin

from .models import Job, Skill


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "get_skills")
    search_fields = ("title", "level")
    list_filter = ("level", "skills")

    @admin.display(description="Skills")
    def get_skills(self, obj):
        return ", ".join([skill.title for skill in obj.skills.all()])


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)