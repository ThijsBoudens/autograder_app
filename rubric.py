class Rubric():
    def __init__(self, rubric_ID, title, points):
        self.id = rubric_ID
        self.title = title
        self.points = points
        self.graded = False
        self.passed = None
    