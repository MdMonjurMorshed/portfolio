from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
from .models import *
# Create your views here.

class PortfolioView(ListView):
    template_name='morshed_portfolio/base.html'
    model=IntroInfo
   

    
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['intro_obj']=IntroInfo.objects.all()
        context['about_obj']=AboutInfo.objects.all()
        context['experience_obj']=ExperienceInfo.objects.all().order_by('-createdAt')
        context['projects_obj']=ProjectsInfo.objects.all().order_by('-createdAt')
        context['skill_obj']=SkillInfo.objects.all()
        context['education_obj']=EducationTraining.objects.all().order_by('-createdAt')
        context['contact_obj']=ContactInfo.objects.all()

      
        return context
    

