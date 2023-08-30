class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print("Skill:", self.skill)
        print("Percentage:", self.percentage)