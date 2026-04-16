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
        record = f"{self.name},{self.id}"
        for question in self.questions:
            record += f"{self.get_question_points(question)}, {self.get_failed_rubrics(question)},"
        record+=f'{self.grade}' #total grade
        return record


    def autograde(self, tests):
        root_folder = '/'.join(self.full_path.split('/')[:-1])
        sys.path.append(root_folder)
        module_name = self.full_path.split('/')[-1][:-3] #module name without .py
        # print(module_name, os.getcwd())
        try:
            module = importlib.import_module(module_name)

        except Exception as e:
            print("Error occured for ", self.name, ' \n------------------')
            print(e)

