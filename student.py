class Student():
    def __init__(self, name):
        self.name = name
        self.points_per_question = {}
        self.failed_rubrics = {}
        self.total_score = 0
        self.been_graded = False
    
    def set_score(self):
        total_points = 0
        for point in self.points_per_question.values():
            total_points += point
        self.total_score += total_points
    
    def set_points_per_question(self, question, points):
        if question not in self.points_per_question:
            self.points_per_question[question] = 0
        self.points_per_question[question] += points
        

    def set_failed_rubrics(self, question, failed_rubrics_list):
        if question not in self.failed_rubrics:
            self.failed_rubrics[question] = failed_rubrics_list
        # self.failed_rubrics[question].append(rubric.rubric_title)
        