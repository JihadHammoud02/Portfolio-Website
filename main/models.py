from django.db import models

# Create your models here.


class Personal(models.Model):
    profession=models.CharField(max_length=250)
    about_me=models.TextField()


class Skills(models.Model):
    skill_name=models.CharField(max_length=250,help_text='Enter a Skill')
    skill_rating=models.CharField(max_length=250,help_text=' Choose between: excellent,very-good,good,beginner')

class projects(models.Model):
    project_name=models.CharField(max_length=250)
    project_desc=models.TextField(max_length=250)
    project_link=models.CharField(max_length=250)

class jihad(models.Model):
    living_country=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=250)
    email_add=models.EmailField(max_length=250)

class Education(models.Model):
    type=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    country=models.CharField(max_length=250)

class previous_jobs(models.Model):
    job_name=models.CharField(max_length=250)
    job_desc=models.TextField(max_length=250)
    job_date=models.CharField(max_length=250)

class experiences(models.Model):
    experience=models.TextField()
    