from django.shortcuts import render, redirect
from .models import Contact, Glasses, User
from django.contrib.auth import authenticate, login, logout
from base import models
from .forms import ContactForm
# for class views
from django.views.generic import TemplateView
from django.views import generic, View

from django.views.generic import FormView

# Create your views here.
"""
def index(request):
    glasses= Glasses.objects.all()
    context = {'glasses': glasses}
    return render(request, 'base/index.html',context)

"""


class IndexView(generic.ListView):
    model = Glasses
    template_name = "base/index.html"
    context_object_name = 'glasses'

    def get_queryset(self):
        return Glasses.objects.all()


"""
def about(request):
    return render(request, 'base/about.html')
"""


class AboutView(View):
    def get(self, request):
        return render(request, 'base/about.html')


"""
def glasses(request):
    glasses= Glasses.objects.all()
    context = {'glasses': glasses}
    return render(request, 'base/glasses.html', context)
"""


class GlassesView(generic.ListView):
    model = Glasses
    template_name = "base/glasses.html"
    context_object_name = 'glasses'


"""
def shop(request):
    return render(request, 'base/shop.html')

"""


class ShopView(TemplateView):
    template_name = "base/shop.html"


"""
using template in function base view
def contact(request):
    if request.method == "POST":
        name = request.POST["Name"]
        phone = request.POST["Phone Number"]
        email = request.POST["Email"]
        message = request.POST["Message"]
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'base/contact.html')
"""
"""
#function base view and use forms class
#using forms.py file and class

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'base/contact.html', context)
"""


class ContactFormView(FormView):
    template_name = "base/contact.html"
    success_url = "base/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'base/contact.html')

    def post(self, request, *args, **kwargs):
        """
        form = ContactForm()

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return render(request, 'base/contact.html', context)
        """
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():

                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                """
                # how we handle error throw views
                
                if len(phone) > 13:
                    message = "Phone number is incorrect"
                    context = {'message': message}
                    return render(request, 'base/contact.html', context)

                if name != str(name):
                    mess = "name only in alphabetic"
                    context = {'message': mess}
                    return render(request, 'base/contact.html', context)

                if phone != int(phone):
                    mess = 'phone number must be numeric.'
                    context = {'message': mess}
                    return render(request, 'base/contact.html', context)
                """
                    
                contact = Contact(name=name, phone=phone, email=email, message=message)
                contact.save()
                return redirect("index")

            context = {'form': form}
            return redirect('/', context)


"""
#using template class base view
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/contact.html')

    def post(self, request, *args, **kwargs):
        name = request.POST["Name"]
        phone = request.POST["Phone Number"]
        email = request.POST["Email"]
        message = request.POST["Message"]
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()
        return redirect('index')

"""

"""
class ContactView(CreateView):

    template_name = "base/contact.html"
    success_url = '/index/'
"""

"""
def handleregister(request):
    if request.method == "POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']
        user = models.User.objects.filter(email=email)
        if user:
            message=("User is already exist")
            context={"message":message}
            return render(request, "base/register.html", context)
        else:
            if pass1 == pass2:
                data = {
                    "email" : email,
                    "first_name": fname,
                    "last_name" : lname,
                }
                user_obj = models.User.objects.create(**data)
                user_obj.set_password(pass1)
                user_obj.save()
                return redirect('login')
            message=("Password and Re-enter password not matching..")
            context = {"message": message}
            return render(request, "base/register.html", context)

    return render(request, "base/register.html")

"""


class HandleRegisterView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, "base/register.html")

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']
        user = models.User.objects.filter(email=email)
        if user:
            message = "User is already exist"
            context = {"message": message}
            return render(request, "base/register.html", context)
        else:
            if pass1 == pass2:
                data = {
                    "email": email,
                    "first_name": fname,
                    "last_name": lname,
                }
                user_obj = models.User.objects.create(**data)
                user_obj.set_password(pass1)
                user_obj.save()
                return redirect('login')
            message = "Password and Re-enter password not matching.."
            context = {"message": message}
            return render(request, "base/register.html", context)


"""
def handlelogin(request):
    if request.method == "POST":
        email=request.POST["email"]
        password = request.POST["pass"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, "base/login.html")
"""


class HandleLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base/login.html")

    def post(self, request, *args, **kwargs):
        email = request.POST["email"]
        password = request.POST["pass"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


"""
def handlelogout(request):
    logout(request)
    return redirect("index")
"""


class HandleLogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("index")
