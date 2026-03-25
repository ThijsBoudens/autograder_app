class Question():
    def __init__(self, question_ID):
        self.rubrics = {}
        self.graded = False
        self.grade = 0
        self.max_grade = 0
        self.id = question_ID


    def add_rubric(self, rub):
        self.rubrics[rub.id] = rub
        self.update()

    def update(self):
        self.graded = self.check_if_graded()
        self.max_grade = self.calculate_max_grade()
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        total = 0
        for rub in self.rubrics:
            if self.rubrics[rub].passed:
                total += self.rubrics[rub].points
        return total

    def calculate_max_grade(self):
        total = 0
        for rub in self.rubrics:
            total += self.rubrics[rub].points
        return total

    def check_if_graded(self):
        for rub in self.rubrics:
            if not self.rubrics[rub].graded:
                return False
        return True

    

