import json
from django.http import HttpResponse

def main():
    with open("user_data.json") as users_file:
        users = json.load(users_file)
    
    with open("jobs_data.json") as jobs_file:
        jobs = json.load(jobs_file)
    
    with open("course_data.json") as courses_file:
        courses = json.load(courses_file)
    
    outfile = open("eList.csv", "w")

    emailList = []

    def email_gather(request):
        emailList.append(request)
        return
    
    if len(emailList) >= 1:
        for email in emailList:
            outfile.write(email)


if __name__ == "__main__":
    main()