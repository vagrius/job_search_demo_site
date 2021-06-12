from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredMixinCustom(LoginRequiredMixin):

    LoginRequiredMixin.login_url = '/login/'
    LoginRequiredMixin.redirect_field_name = None
