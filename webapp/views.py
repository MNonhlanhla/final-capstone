from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from webapp.models import Enquiry


def index(request):
    """This function renders the home page of the website."""
    return render('', 'index.html')


@login_required
def show_specials(request):
    """This function renders the specials page,
    which only applies to logged-in users."""
    if request.method == 'POST':
        # create an instance of our Enquiry, and fill it with the POST data
        enquiry = Enquiry(request.POST)
    else:
        # this must be a GET request, so create an empty Enquiry
        enquiry = Enquiry()
    return render(request, 'contact.html', {'enquiry': enquiry})


def user_login(request):
    """This functions renders the login page."""
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """This function authenticated the user using the provided username and password.
    if the user is logged in, they get redirected to show_user page.
    If not logged in, the remain on the login page."""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )


def contact(request):
    """This function renders the contact page of the website."""
    return render(request, 'contact.html')
