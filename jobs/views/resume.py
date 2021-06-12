from django.shortcuts import render, redirect
from django.views import View

from jobs.models import Resume
from jobs.forms import ResumeForm
from jobs.utils import LoginRequiredMixinCustom


class ResumeStartView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.filter(user_id=request.user.id)
        if not resume:
            return render(request, "personal/resume_start.html")
        else:
            return redirect("resume_my")


class ResumeCreateView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.filter(user_id=request.user.id)
        if not resume:
            initial = {}
            if request.user.first_name:
                initial['name'] = request.user.first_name
            if request.user.last_name:
                initial['surname'] = request.user.last_name
            form = ResumeForm(initial=initial)
            context = {
                'form': form,
                'status': 'new'
            }
            return render(request, "personal/resume_create.html", context=context)
        else:
            return redirect("resume_my")

    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user_id = request.user.id
            resume.save()
            request.session['resume_status'] = 'created'
            return redirect("resume_my")
        context = {
            'form': form,
        }
        return render(request, "personal/resume_create.html", context=context)


class ResumeMyView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.filter(user_id=request.user.id)
        if resume:
            resume = resume.first()
            initial = {
                'name': resume.name,
                'surname': resume.surname,
                'status': resume.status,
                'salary': resume.salary,
                'speciality': resume.speciality,
                'grade': resume.grade,
                'education': resume.education,
                'experience': resume.experience,
                'portfolio': resume.portfolio,
            }
            form = ResumeForm(initial=initial)
            if 'resume_status' not in request.session:
                request.session['resume_status'] = ''
            context = {
                'resume': resume,
                'form': form,
                'status': request.session['resume_status'],
            }
            request.session['resume_status'] = ''
            return render(request, "personal/resume_create.html", context=context)
        else:
            return redirect('resume_start')

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(user_id=request.user.id)
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            request.session['resume_status'] = 'changed'
            return redirect("resume_my")
        context = {
            'form': form,
        }
        return render(request, "personal/resume_create.html", context=context)
