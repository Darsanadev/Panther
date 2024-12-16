from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and mail and phone and message:  # Ensure that all fields are filled
            try:
                send_mail(
                    subject=f'Hey PantherBrigadez i am {name}',
                    message=f'Name: {name} \nPhone: {phone} \nEmail: {mail} \nMessage: {message}.',
                    from_email=mail,  # Use a valid Gmail account
                    recipient_list=['darshuuu11@gmail.com'],  # The admin email
                    fail_silently=False,
                )
                return render(request, 'contact.html')  # Redirect to success page
            except Exception as e:
                # Return an error message if email fails to send
                return HttpResponse(f"Error sending email: {str(e)}")
        else:
            return HttpResponse("All fields are required")
    
    return render(request, 'contact.html')  # Return contact form if not POST
