from django.db.models import F
from django.shortcuts import render,redirect
from random import choices, randrange
import string
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from  .forms import UrlForm
from .forms import UserCreateForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import UrlTable
from django.http import Http404


def random_key():
    "make random key"

    return ''.join(choices(string.ascii_letters + string.digits, k=randrange(5,8)))




class MainView(TemplateView):
    template_name = "index_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            id = request.user
            url = UrlTable.objects.filter(user=id)
            ctx = {}
            ctx["elements"] = url
            return render(request, self.template_name, ctx )
        else:
            return render(request,  self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        # получаем обьект пользователя на основе введеных форм данных
        self.user = form.get_user()


        # выполняе аутетификацию пользователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")



def redirect_view(request, key):
    try:
        url_table = UrlTable.objects.get(key_url=key)
        url_table.click = F('click') + 1
        url_table.save()
    except UrlTable.DoesNotExist:
        raise Http404('Url not found')
    return redirect(to=url_table.long_url)


def get_short_url():
    short_url = random_key()
    taken = UrlTable.objects.filter(key_url=short_url)
    if taken:
        return get_short_url()
    else:
        return short_url

def save_url_to_database(url, request):
    short_url = get_short_url()
    if request.user.is_authenticated:
        key_url = short_url
        user = request.user
        long_url = url
        url_from = UrlTable(key_url=key_url,user=user,long_url=long_url)
    else:
        key_url = short_url
        long_url = url
        url_from = UrlTable(key_url=key_url,long_url=long_url)
    url_from.save()
    return  "http://68.183.158.178" + short_url


def save_short_url(request):
    print(request.POST, 'POST>>')
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            absolute_short_url = save_url_to_database(url, request)
            return HttpResponse(absolute_short_url)

    return HttpResponse ("Url is not valid!!!")
