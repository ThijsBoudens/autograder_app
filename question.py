class Question():
    def __init__(self, question_ID):
        self.total_points = 0
        self.rubrics = {}
        self.been_graded = False
        self.grade = None
        self.question_ID = question_ID
    

    def get_rubrics(self, rubric_id):
        if rubric_id in self.rubrics:
            return self.rubrics[rubric_id]
        else:
            print("rubric not found")
    
    # def set_grade(self):
    #     for rubric in self.rubrics.values():
    #         self.grade

