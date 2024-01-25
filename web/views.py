from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage

from django.utils.translation import gettext_lazy as _

def home(request):
    return render(request,'web/home.html')

def about(request):
    return render(request,'web/about.html')

def private_fees(request):
    return render(request,'web/private_fees.html')

def nhs_fees(request):
    return render(request,'web/nhs_fees.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        confirmation_message = _("Thank you %(name)s for submitting your form. We will get back to you very soon.") % {'name': name}
        messages.success(request, confirmation_message)

        email_to_owner = EmailMessage(
            subject=f'Subject: {subject} from {name}',
            body=f"Name: {name} \n\nMobile: {mobile} \n\nEmail: {email}: \n\nMessage: {message}",
            from_email='hmareiwan@outlook.com',
            to=['hmareiwan@outlook.com'],
        )
        email_to_owner.send()

        email_to_user = EmailMessage(
            subject=f'{subject} from Cheapest Dental Clinic',
            body=f"Dear {name} \n\nThank you for contacting our clinic. We will get back to you very soon.\n\nRegards\n\nCheapest Dental Clinic",
            from_email='hmareiwan@outlook.com',
            to=[email],
        )
        email_to_user.send()

        return redirect('contact') 
    return render(request,'web/contact.html')

def new_patients(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST['mobile']
        email=request.POST['email']
        message=request.POST['message']
        
        messages.success(request,f'Thank you {name} for submitting an appointment form. We look forward to seeing you!')

        email_to_user = EmailMessage(
            subject=f'Appointment',
            body=f"Dear {name} \n\nThank you for contacting our clinic. We will get back to you very soon.\n\nRegards\n\nCheapest Dental Clinic",
            from_email='hmareiwan@outlook.com',
            to=[email],
        )
        email_to_user.send()

        send_mail(
            'New patients',
            f'Name: {name}\n\nMobile:{mobile}\n\nEmail:{email}\n\nMessage:{message}',
            'hmareiwan@outlook.com',
            ['hmareiwan@outlook.com'],
            fail_silently=False
        )

        return redirect('new_patients')
    return render(request,'web/new_patients.html')

def fillings(request):
    return render(request,'web/fillings.html')

def dental_hygiene(request):
    return render(request,'web/dental_hygiene.html')

def cosmetic_dentistry(request):
    return render(request,'web/cosmetic_dentistry.html')

def specialist_dentistry(request):
    return render(request,'web/specialist_dentistry.html')

def david_terry(request):
    return render(request,'web/david_terry.html')
def silvia_omer(request):
    return render(request,'web/silvia_omer.html')






