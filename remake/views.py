import json
import smtplib, ssl
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def email_gather(request):
    if request.method == 'POST':
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "linkedinhackathon30@gmail.com"
        password = "trxt vbgt bvwv wfds"
        receiver_email = request.POST.get('email')
        message = """Subject: Internship Opportunity

        This is your internship message."""
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def second_page(request):
    return render(request, 'post.html')