from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
        })

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
                })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save(commit=False)
                name = participant.name 
                email = participant.email
                address = participant.address
                participant.save()
                selected_meetup.participants.name = name
                selected_meetup.participants.email = email
                selected_meetup.participants.address = address
                selected_meetup.save()
                return redirect('confirm-registration')
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
            })
    
def confirm_registration(request): 
    return render(request, 'meetups/registration-success.html')

# participant.save()
#                 selected_meetup.participants.add(participant.name)
#                 selected_meetup.participants.add(participant.email)
#                 selected_meetup.participants.add(participant.address)
#                 selected_meetup.save()