from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(IntroInfo)

class InfoAdmin(admin.ModelAdmin):
    list_display=['name','age']


# register for about info

@admin.register(AboutInfo)
class AboutAdmin(admin.ModelAdmin):
    list_display=['aboutImage']

# register for  experience

@admin.register(ExperienceInfo)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=['designation']


# register for Projects

@admin.register(ProjectsInfo)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['project_title']

# register for Skill info

@admin.register(SkillInfo)
class SkillAdmin(admin.ModelAdmin):
    list_display=['skill_title'] 

# register for  education and training
@admin.register(EducationTraining)
class EducationAdmin(admin.ModelAdmin):
    list_display=['institute_name']  


# registr for contact info

@admin.register(ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    list_display=['title']


