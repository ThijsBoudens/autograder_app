class Rubric():
    def __init__(self, rubric_ID, title, points):
        self.rubric_ID = rubric_ID
        self.title = title
        self.points = points
        self.been_graded = False
        self.pass_state = None
    