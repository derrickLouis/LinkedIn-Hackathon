import json
import os

def main():
    with open("user_data.json", "r") as users_file:
        users = json.load(users_file)
    
    with open("jobs_data.json", "r") as jobs_file:
        jobs = json.load(jobs_file)
    
    with open("course_data.json", "r") as courses_file:
        courses = json.load(courses_file)

    


if __name__ == "__main__":
    main()