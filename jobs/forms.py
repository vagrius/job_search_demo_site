from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Div, Field

from jobs.models import Application, Company, Vacancy, Resume


class ApplicationSendForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            'written_username',
            'written_phone',
            'written_cover_letter')
        labels = {
            'written_username': 'Имя',
            'written_phone': 'Контактный номер телефона',
            'written_cover_letter': 'Сопроводительное письмо',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Отправить'))
        self.helper.layout = Layout(
            Div(
                Div(
                    'written_username',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'written_phone',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            'written_cover_letter'
        )


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'name',
            'logo',
            'employee_count',
            'location',
            'description'
        )
        labels = {
            'name': 'Название',
            'logo': 'Логотип',
            'employee_count': 'Количество сотрудников',
            'location': 'География',
            'description': 'Информация',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Сохранить'))
        self.helper.layout = Layout(
            'name',
            Div(
                Div(
                    Field('logo'),
                    css_class="form-group col-md-9 mb-0",
                ),
                Div(
                    HTML(
                        """{% if form.logo.value %}<img class="img-responsive" src="{{ company.logo.url }}" width="132"
                        height="84">{% endif %}""",
                    ),
                    css_class="form-group col-md-3 mb-0 mt-4 pt-2",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    'employee_count',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'location',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            'description',
        )


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'speciality',
            'salary_min',
            'salary_max',
            'skills',
            'description'
        )
        labels = {
            'title': 'Название вакансии',
            'speciality': 'Специализация',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
            'skills': 'Требуемые навыки',
            'description': 'Описание',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Сохранить'))
        self.helper.layout = Layout(
            Div(
                Div(
                    'title',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'speciality',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    'salary_min',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'salary_max',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            'skills',
            'description'
        )


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            'name',
            'surname',
            'status',
            'salary',
            'speciality',
            'grade',
            'education',
            'experience',
            'portfolio'
        )
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'speciality': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Сылка на портфолио',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Сохранить'))
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'surname',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    'status',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'salary',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            Div(
                Div(
                    'speciality',
                    css_class="form-group col-md-6 mb-0",
                ),
                Div(
                    'grade',
                    css_class="form-group col-md-6 mb-0",
                ),
                css_class="form-row",
            ),
            'education',
            'experience',
            'portfolio',
        )
