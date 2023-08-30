class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print("Degree:", self.degree)
        print("Institution:", self.institution)
        print("Completion Date:", self.completion_date)
