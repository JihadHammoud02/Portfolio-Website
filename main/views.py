from webbrowser import get
from django.shortcuts import render
from requests import request
from main.models import Personal
from main.models import Skills,projects,jihad,Education,previous_jobs,experiences
from django.core.mail import send_mail


def test(request):
    return render(request,'main/homepage.html',{'pro':show_professions()[0],'ab':show_professions()[1],'skills':show_skills(),'projects':show_projects(),'country':get_pers_info()[0],'email':get_pers_info()[1],'num':get_pers_info()[2],'educ':get_educational_background(),'jobs':get_previous_jobs(),'exp':show_exp()})


def show_professions():
    professions=Personal.objects.all()
    prof=''
    about_myself=''
    for i in professions:
        prof=i.profession
        about_myself=i.about_me

    return (prof,about_myself)

def show_skills():
    skills=Skills.objects.all()
    skill_me={}
    list_skills=[]
    for i in skills:
        skill_me['skill']=i.skill_name
        skill_me['rating']=i.skill_rating
        list_skills.append(skill_me)
        skill_me={}
    return list_skills

def show_projects():
    project=projects.objects.all()
    projects_me={}
    list_projects=[]
    for i in project:
        projects_me['name']=i.project_name
        projects_me['desc']=i.project_desc
        projects_me['url']=i.project_link
        list_projects.append(projects_me)
        projects_me={}
    return list_projects

def get_pers_info():
    info=jihad.objects.all()
    country=''
    email=''
    num=''
    for k in info:
        country=k.living_country
        email=k.email_add
        num=k.phone_number
    return (country,email,num)

def get_educational_background():
    educ=Education.objects.all()
    dict_edu={}
    list_of_educ=[]
    for j in educ:
        dict_edu['name']=j.name
        dict_edu['type']=j.type
        dict_edu['country']=j.country
        list_of_educ.append(dict_edu)
        dict_edu={}
    return list_of_educ

def get_previous_jobs():
    jobs=previous_jobs.objects.all()
    dict_jobs={}
    list_of_jobs=[]
    for j in jobs:
        dict_jobs['name']=j.job_name
        dict_jobs['desc']=j.job_desc
        dict_jobs['date']=j.job_date
        list_of_jobs.append(dict_jobs)
        dict_jobs={}
    return list_of_jobs

def show_exp():
    exp=experiences.objects.all()
    list_of_exp=[]
    for j in exp:
        list_of_exp.append(j.experience)
    return list_of_exp