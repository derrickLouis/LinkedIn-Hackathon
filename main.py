import json
from django.http import HttpResponse
from django.shortcuts import render
import smtplib, ssl


def main():

    with open("user_data.json") as users_file: 
        users = json.load(users_file) #Saves user json as dict
    
    with open("jobs_data.json") as jobs_file:
        jobs = json.load(jobs_file) #Saves jobs json as dict
    
    with open("course_data.json") as courses_file:
        courses = json.load(courses_file) #Saves courses json as dict
    
    def email_gather(request): #View for email input from site
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "linkedinhackathon30@gmail.com"
        password = "hackathon123"
        receiver_email = request
        message = """This is your internship Message"""
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server: #Opens SMTP server to send email
            server.starttls(context=context)
            server.login(sender_email, password) #Logs into sender email
            server.sendmail(sender_email, receiver_email, message) #Sends message #saves request to emailList
        
        return render(request, 'index.html')

if __name__ == "__main__":
    main()