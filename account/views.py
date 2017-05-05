from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile, Contact
from actions.models import Action
from actions.utils import create_action
from common.decorators import ajax_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, 'created an account')

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Error while updating the profile.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard(request):
    following_users = request.user.following.values_list('id', flat=True)
    if following_users:
        actions = Action.objects.exclude(user=request.user) \
                                .filter(user_id__in=following_users) \
                                .select_related('user', 'user__profile') \
                                .prefetch_related('target')[:20]
    else:
        actions = []
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'actions': actions})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})

@ajax_required
@login_required
@require_POST
def user_follow(request):
    user_id = request.POST.get('user_id')
    action = request.POST.get('action')

    if user_id and action:
        try:
            user = User.objects.get(id=user_id, is_active=True)
            if action == 'follow':
                Contact.objects.create(from_user=request.user, to_user=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(from_user=request.user, to_user=user).delete()
                create_action(request.user, 'unfollowed', user)
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            pass

    return JsonResponse({'status': 'nok'})
