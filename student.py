class Student():
    def __init__(self, path, full_path):
        self.parse_path(path)
        self.exam_path = path
        self.full_path = full_path
        self.grade = 0
        self.max_grade = 0
        self.questions = {}
        self.graded = False

    def parse_path(self, path):
        pathList = path.split('_')
        self.name = pathList[2]
        self.id = pathList[3]

    def update(self):
        for q in self.questions:
            self.questions[q].update()
        self.grade = self.calculate_grade()
        self.max_grade = self.calculate_max_grade()
        self.graded = self.check_if_graded()

    def calculate_grade(self):
        total = 0
        for que in self.questions:
            total+= self.questions[que].grade
        return total

    def calculate_max_grade(self):
        total = 0
        for que in self.questions:
            total+= self.questions[que].max_grade
        return total

    def check_if_graded(self):
        for que in self.questions:
            if not self.questions[que].graded:
                return False
        return True

    def get_content(self):
        with open(self.full_path, 'r') as f:
            content = f.read()
            return content
    
    def set_questions(self, questions):
        self.questions = questions
    
  
    def return_record(self):
        record = f"{self.name}"
        for question in self.questions:
            record += f", {self.points_per_question[question]}, {self.failed_rubrics[question]}"
        record +=  f", {sum(self.points_per_question.values())}"
        return record