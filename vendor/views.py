from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import UserProfileForm
from .forms import VendorForm
from django.contrib import messages
from accounts.models import UserProfile
from .models import Vendor
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_vendor


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vprofile(request):
    # To load the repective vendor instance
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    # FOr updating the changes done in form

    if request.method == 'POST':
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        # print("test")
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Settings Updated')
            return redirect('vprofile')
        else:
            print(profile_form.errors)
            print(vendor_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        vendor_form = VendorForm(instance=vendor)
    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor
    }
    return render(request, 'vendor/vprofile.html', context)


def menu_builder(request):
    return render(request, 'vendor/vprofile.html')
