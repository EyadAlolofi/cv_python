from education import Education
from experience import Experience
from skill import Skill


class CV:
    def __init__(self):
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self):
        company = input("Enter company name: ")
        job_title = input("Enter job title: ")
        start_date = input("Enter start date: ")
        end_date = input("Enter end date: ")

        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)

        choice = input("Do you want to add another experience? (yes/no): ")
        if choice.lower() == "yes":
            self.add_experience()

    def add_education(self):
        degree = input("Enter degree: ")
        institution = input("Enter institution: ")
        completion_date = input("Enter completion date: ")

        education = Education(degree, institution, completion_date)
        self.education.append(education)

        choice = input("Do you want to add another education? (yes/no): ")
        if choice.lower() == "yes":
            self.add_education()

    def add_skill(self):
        skill = input("Enter skill: ")
        percentage = input("Enter skill percentage: ")

        skill = Skill(skill, percentage)
        self.skills.append(skill)

        choice = input("Do you want to add another skill? (yes/no): ")
        if choice.lower() == "yes":
            self.add_skill()

    def display_cv(self):
        print("CV:")
        print("--------")
        print("Experiences:")
        for experience in self.experiences:
            experience.display_experience()
            print("--------")
        print("Education:")
        for education in self.education:
            education.display_education()
            print("--------")
        print("Skills:")
        for skill in self.skills:
            skill.display_skill()
            print("--------")