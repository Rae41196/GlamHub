from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import (
    RegistrationForm,
    AccountAuthenticationForm,
    AccountUpdateForm
)

from blog.models import BlogPost
from artist.models import ArtistPortfolio


# The registration form view creation
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            password = account.password
            account.set_password(password)
            account.save()
            account = authenticate(
                request, username=account.email, password=password)
            if account:
                login(request, account)
                return redirect('home')
        else:
            context['registration_form'] = form  # to pass back to form to display the errors

    else:  # GET request since its a first time visit
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

# view for logging out creation


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    redirect_url = request.GET.get('next')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                url = redirect_url if redirect_url else 'home'
                return redirect(url)

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Successfully updated!"
    else:
        form = AccountUpdateForm(
                initial={
                    "email": request.user.email,
                    "username": request.user.username,
                }
            )
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    artistportfolios = ArtistPortfolio.objects.filter(business_owner=request.user) # noqa
    context['artistportfolios'] = artistportfolios

    return render(request, "account/account.html", context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})










