from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import DetailView, ListView
from .models import AboutMe, Project, Course, Education, ProfesstionalIntrests, ComputerSkills, PossitionsOfResponsibility, Hackathon, VolunteerExperience, Hobbies

class ProjectListView(ListView):
    template_name = 'website/projects.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return sorted(Project.objects.all(), key=lambda x: x.order)

class SkillsetListView(ListView):
    template_name = 'website/courses.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return sorted(Course.objects.all(), key=lambda x: x.order)

class AboutMeListView(ListView):
    template_name = 'website/index.html'
    context_object_name = 'all_about_me'

    def get_queryset(self):
        return AboutMe.objects.all()

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'website/projectDetails.html'
    context_object_name = 'project'

def cv(request):
    all_education = Education.objects.all()
    all_professional_inrests = ProfesstionalIntrests.objects.all()
    all_computer_skills = ComputerSkills.objects.all()
    all_possitions_of_responsibility = PossitionsOfResponsibility.objects.all()
    all_hackathon = Hackathon.objects.all()
    all_volunteer_experience = VolunteerExperience.objects.all()
    all_hobbies = Hobbies.objects.all()

    context = {
    'all_education' : all_education,
    'all_professional_inrests' : all_professional_inrests,
    'all_computer_skills' : all_computer_skills,
    'all_possitions_of_responsibility' : all_possitions_of_responsibility,
    'all_hackathon' : all_hackathon,
    'all_volunteer_experience' : all_volunteer_experience,
    'all_hobbies' : all_hobbies
    }
    return render(request, 'website/cv.html', context)

def download(request):
    file_path = settings.BASE_DIR + '/website/static/website/files/Resume.pdf'
    file_wrapper = open(file_path, 'rb')
    response = HttpResponse(file_wrapper, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=Resume.pdf'
    response['X-Sendfile'] = file_path
    return response
