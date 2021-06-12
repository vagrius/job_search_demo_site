from django.views import View
from django.shortcuts import render, redirect

from jobs.models import Company
from jobs.forms import CompanyForm
from jobs.utils import LoginRequiredMixinCustom


class CompanyStartView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner_id=request.user.id)
        if not company:
            return render(request, "personal/company_start.html")
        else:
            return redirect("company_my")


class CompanyCreateView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner_id=request.user.id)
        if not company:
            form = CompanyForm
            context = {
                'form': form,
            }
            return render(request, "personal/company_create.html", context=context)
        else:
            return redirect("company_my")

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner_id = request.user.id
            company.save()
            request.session['company_status'] = 'created'
            return redirect("company_my")
        context = {
            'form': form,
        }
        return render(request, "personal/company_create.html", context=context)


class CompanyMyView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner_id=request.user.id)
        if company:
            company = company.first()
            initial = {
                'name': company.name,
                'logo': company.logo,
                'employee_count': company.employee_count,
                'location': company.location,
                'description': company.description,
            }
            form = CompanyForm(initial=initial)
            if 'company_status' not in request.session:
                request.session['company_status'] = ''
            context = {
                'company': company,
                'form': form,
                'status': request.session['company_status'],
            }
            request.session['company_status'] = ''
            return render(request, "personal/company_create.html", context=context)
        else:
            return redirect('company_start')

    def post(self, request, *args, **kwargs):
        company = Company.objects.get(owner_id=request.user.id)
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            request.session['company_status'] = 'changed'
            return redirect("company_my")
        context = {
            'form': form,
        }
        return render(request, "personal/company_create.html", context=context)
