from django.db import models
from django.urls import reverse

class AboutMe(models.Model):
    about_me = models.CharField(max_length = 1500)

    def get_absolute_url(self):
        return reverse('website:index')

    def __str__(self):
        return self.about_me

class Course(models.Model):
    course_title = models.CharField(max_length = 100)
    offered_by = models.CharField(max_length = 100)
    plateform = models.CharField(max_length = 50)
    score = models.IntegerField(blank=True)
    certificate_link = models.CharField(max_length = 250, blank=True)

    def get_absolute_url(self):
        return reverse('website:skillset')

    def __str__(self):
        return self.course_title

class Project(models.Model):
    project_title = models.CharField(max_length = 100)
    s_description = models.CharField(max_length = 250)
    l_description = models.CharField(max_length = 1000)
    highlight_1 = models.CharField(max_length = 250, blank=True)
    highlight_2 = models.CharField(max_length = 250, blank=True)
    highlight_3 = models.CharField(max_length = 250, blank=True)
    github_link = models.CharField(max_length = 250, blank=True)

    def get_absolute_url(self):
        return reverse('website:project_details', kwargs={'pk':self.id})

    def __str__(self):
        return self.project_title

class Education(models.Model):
    education = models.CharField(max_length = 1500)

    def __str__(self):
        return self.education

class ProfesstionalIntrests(models.Model):
    professional_inrests = models.CharField(max_length = 1500)

    def __str__(self):
        return self.professional_inrests

class ComputerSkills(models.Model):
    title = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

class PossitionsOfResponsibility(models.Model):
    title = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

class Hackathon(models.Model):
    title = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title

class VolunteerExperience(models.Model):
    title = models.CharField(max_length = 100)
    definition = models.CharField(max_length = 1000)
    role1 = models.CharField(max_length = 500, blank = True)
    role2 = models.CharField(max_length = 500, blank = True)
    role3 = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.title

class Hobbies(models.Model):
    hobbies = models.CharField(max_length = 1500)

    def __str__(self):
        return self.hobbies
