class Student():
    def __init__(self, name):
        self.name = name
        self.points_per_question = {}
        self.failed_rubrics = {}
        self.grade = None
        self.been_graded = False
        self.questions = {}
        self.pending = False
    
    def set_grade(self):
        total_points = 0
        for point in self.points_per_question.values():
            total_points += point
        self.grade = total_points
        
    def set_points_per_question(self, question, points):
        if question not in self.points_per_question:
            self.points_per_question[question] = 0
        self.points_per_question[question] += points
        

    def set_failed_rubrics(self, question, failed_rubrics_list):
        if question not in self.failed_rubrics:
            self.failed_rubrics[question] = failed_rubrics_list
        # self.failed_rubrics[question].append(rubric.rubric_title)
        
    def get_question(self,question_id):
        if question_id in self.questions:
            return self.questions[question_id]
        else:
            print("question not found")
    
    def set_questions(self, questions):
        self.questions = questions

    def return_record(self):
        record = f"{self.name}"
        for question in self.questions:
            record += f", {self.points_per_question[question]}, {self.failed_rubrics[question]}"
        record +=  f", {sum(self.points_per_question.values())}"
        return record