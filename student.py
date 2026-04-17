import importlib
import traceback
import os
import sys
import copy
from collections import Counter
import math

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

    def get_question_points(self,q):
        return self.questions[q].grade

    def get_failed_rubrics(self,q):
        st = ''
        for rub in self.questions[q].rubrics.values():
            if rub.passed == False:
                st+=f'{str(rub.id)} '
        return st[:-1] #remove last space
  
    def get_record(self):
        record = f"{self.name},{self.id},"
        for question in self.questions:
            record += f"{self.get_question_points(question)}, {self.get_failed_rubrics(question)},"
        record+=f'{self.grade}' #total grade
        return record

    def autograde_pass(self, question):
        for rubric in question.rubrics.values():
            rubric.graded = True
            rubric.passed = True

    def autograde_fail(self, question):
        for rubric in question.rubrics.values():
            rubric.graded = True
            rubric.passed = False


    def autograde(self, tests):
        root_folder = '/'.join(self.full_path.split('/')[:-1])
        sys.path.append(root_folder)
        module_name = self.full_path.split('/')[-1][:-3] #module name without .py
        # print(module_name, os.getcwd())
        print('Grading ', self.name, '\n')
        try:
            module = importlib.import_module(module_name)

            for q in self.questions.values():
                function_result = self.run_func(q, module, tests)     
                if function_result: #if pass
                    self.autograde_pass(q)
                else:
                    self.autograde_fail(q)
                self.update()

        except Exception as e:
            print()
            print('----- error ------', self.name)
            print(e)
            print()

        # check inf loops
        # update grades and views


    def run_func(self, question, module, tests):
        question_pass = True
        try:
            func = getattr(module, question.function_name)
        except:
            print('error loading function.')
        for i, inp in enumerate(tests['function_inputs'][question.function_name]['args']):
            # print(i, inp, tests['function_outputs'][question.function_name][i])
            print(question.function_name, i)
            try:
                if isinstance(inp, tuple):
                    res = func(*copy.deepcopy(inp))
                else:
                    res = func(copy.deepcopy(inp))
                if res != tests['function_outputs'][question.function_name][i]:
                    question_pass = False
            except Exception as e:
                print()
                print('error!')
                print(e)
                question_pass = False
                print()
        return question_pass