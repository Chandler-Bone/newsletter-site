from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from twilio.rest import Client
from crud.settings import TWILIO

from newsletter.models import RegisteredUser
from newsletter.forms import RegisteredUserForm

# Create your views here.
def home(request):
    if request.method == "POST":

        # makes a entry based on the user form, checks if valid, and saves
        form = RegisteredUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("registered")
        else:
            context = {"form": form}
            return render(request, "home.html", context)

    # if not making a post request to store data, then return the form
    context = {"form": RegisteredUserForm()}
    return render(request, "home.html", context)


def unsubscribe(request):
    if request.method == "POST":

        # if the phone number exists in the table then delete
        query = RegisteredUser.objects.filter(phone=request.POST["phone"])
        if(query.exists()):
            query.delete()
        return redirect("home")

    context = {"form": RegisteredUserForm()}
    return render(request, "unsubscribe.html", context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Username or password is incorrect.")

    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registered(request):
    return render(request, "registered.html")


@login_required(login_url="login")
def dashboard(request):
    # loads in all registered users for the page to show
    context = {"dataset": RegisteredUser.objects.all(), "form": RegisteredUserForm()}
    return render(request, "dashboard.html", context)


@login_required(login_url="login")
def create_sub(request):
    if request.method == "POST":

        # makes a entry based on the user form, checks if valid, and saves
        form = RegisteredUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.info(request, "Error adding element.")

        return dashboard(request)

    return dashboard(request)


@login_required(login_url="login")
def edit_sub(request, id):

    user = get_object_or_404(RegisteredUser, id=id)
    form = RegisteredUserForm(request.POST or None, instance=user)
        
    if(form.is_valid()):
        form.save()
        return redirect("dashboard")
    elif(request.POST != {}): 
        messages.info(request, "Error editing element.")
        return redirect("dashboard")
        
    return render(request, "edit_sub.html", {"user": user, "form": form})


@login_required(login_url="login")
def delete_sub(request, id):

    query = RegisteredUser.objects.filter(id=id)
    print(query)
    if query.exists():
        query.delete()
    return redirect("dashboard")


@login_required(login_url="login")
def delete_all_sub(request):

    RegisteredUser.objects.all().delete()
    return redirect("dashboard")


@login_required(login_url="login")
def send_newsletter(request):

    if request.method == "POST":
        message = request.POST.get("message")

        client = Client(TWILIO["account_sid"], TWILIO["auth_token"])

        # gets a list of all phone numbers in the table
        phone_numbers = RegisteredUser.objects.all().values_list("phone")

        for phone in phone_numbers:
            try:
                client.messages.create(body=message, from_=TWILIO["twilio_number"], to=phone)
            except:
                pass # trial account only allows authorized phone numbers to be messaged

        return redirect("dashboard")

    return render(request, "send_newsletter.html")
