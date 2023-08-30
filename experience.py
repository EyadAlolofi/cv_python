class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):
        print("Company:", self.company)
        print("Job Title:", self.job_title)
        print("Start Date:", self.start_date)
        print("End Date:", self.end_date)