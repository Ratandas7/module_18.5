from django.shortcuts import render, redirect
from user.forms import SignUpForm, UserDataChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, 'Account Created Successfully!')
                return redirect('user_signup')
        else:
            signup_form = SignUpForm()
        return render(request, './user/signup.html', {'form' : signup_form, 'type' : 'Sign Up'})
    else:
        return redirect('user_profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                user_name = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_pass)
                if user is not None:
                    messages.success(request, 'Logged In Successfully!')
                    login(request, user)
                    return redirect('user_profile')
        else:
            login_form = AuthenticationForm()
        return render(request, './user/signup.html', {'form' : login_form, 'type' : 'Login'})
    else:
        return redirect('user_profile')

@login_required
def user_profile(request):
    return render(request, './user/profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('home')

@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = UserDataChangeForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('edit_profile')
    else:
        profile_form = UserDataChangeForm(instance=request.user)
    return render(request, './user/update_profile.html', {'form' : profile_form, 'type' : 'Update Profile'})


@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            messages.success(request, 'Password Updated Successfully!')
            return redirect('change_password')
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, './user/change_password.html', {'form' : password_form, 'type' : 'Change Password'})



@login_required
def change_password_without_old_password(request):
    if request.method == 'POST':
        password_form = SetPasswordForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            messages.success(request, 'Password Updated Successfully!')
            return redirect('change_password_without_old_password')
    else:
        password_form = SetPasswordForm(user=request.user)
    return render(request, './user/change_password_without_old_password.html', {'form' : password_form, 'type' : 'Change Password'})



        




