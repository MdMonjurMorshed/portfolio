from django.db import models
from .abstruct_class import *

# Create your models here.

class IntroInfo(Common):
    name=models.CharField(max_length=100,blank=False)
    age=models.IntegerField(blank=True)
    fatherName=models.CharField(max_length=100,blank=False)
    motherName=models.CharField(max_length=100,blank=False)
    bgImage=models.ImageField(upload_to='bg_image')
    skill_ease=models.TextField(max_length=3000,blank=False)
    contact_image=models.ImageField(upload_to='contact_image')
    publish=models.BooleanField(default=False)

    def __str__(self) :
        return self.name

# Model for about section

class AboutInfo(Common):
    aboutImage=models.ImageField(upload_to='about_image')
    aboutCv=models.FileField(upload_to='cv')
    aboutDescription=models.TextField(max_length=3000)
    publish=models.BooleanField(default=False)

# Model for Experience

class ExperienceInfo(Common):
    companyName=models.CharField(max_length=100,blank=False,default=None)
    companyLogo=models.ImageField(upload_to='company_logo',blank=True)
    designation=models.CharField(max_length=100,blank=False)
    responsibility=models.TextField(max_length=300)
    start_date=models.DateField(default=None)
    end_date=models.DateField(default=None,blank=True,null=True)
    publish=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.designation
# Model for Projects

class ProjectsInfo(Common):
    project_title=models.CharField(max_length=100,blank=False,default=None)
    description=models.TextField(max_length=200,blank=False)
    peoject_logo=models.ImageField(upload_to='project_image')
    project_duration=models.IntegerField(blank=True)
    repository=models.CharField(max_length=100,blank=False)
    start_date=models.DateField(default=None)
    end_date=models.DateField(default=None,blank=True,null=True)
    publish=models.BooleanField(default=False)



# Model for Skill & description


class SkillInfo(Common):
    skill_title=models.CharField(max_length=50,blank=False)
    knowledge_percent=models.IntegerField(blank=False)
    publish=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.skill_title


# Model for Education and Training

class EducationTraining(Common):
    institute_name=models.CharField(max_length=100,blank=False)
    institute_logo=models.ImageField(upload_to='education_training',blank=False)
    course_title=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=100,blank=False)
    start_date=models.DateField(default=None,blank=False)
    end_date=models.DateField(default= None,blank=True,null=True)
    publish=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.institute_name

#    Model For Contact Info

class ContactInfo(Common):
    title=models.CharField(max_length=30,blank=False)
    icon=models.CharField(max_length=50,blank=False)
    info=models.CharField(max_length=100,blank=False)
    publish=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title




