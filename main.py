import json
import smtplib, ssl
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def main():
    print("hello")
    with open("user_data.json") as users_file: 
        users = json.load(users_file) # Saves user json as dict
    
    with open("jobs_data.json") as jobs_file:
        jobs = json.load(jobs_file) # Saves jobs json as dict
    
    with open("course_data.json") as courses_file:
        courses = json.load(courses_file) # Saves courses json as dict

def email_gather(request):
    if request.method == 'POST':
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "linkedinhackathon30@gmail.com"
        password = "hackathon123"
        receiver_email = request.POST.get('email')
        message = """Subject: Internship Opportunity

        This is your internship message."""
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server: # Opens SMTP server to send email
                server.starttls(context=context)
                server.login(sender_email, password) # Logs into sender email
                server.sendmail(sender_email, receiver_email, message) # Sends message
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        return render(request, 'post.html')


