from random import randint


class Question:

    def __init__(self):                 
        self.question = "No_Question"
        self.option_1 = "1"
        self.option_2 = "2"
        self.option_3 = "3"
        self.option_4 = "4"
        self.used_random = []           
        self.good_answers = []
        self.money_list = [0, 100, 200, 300, 500, "1k", "2k", "4k", "8k", "16k", "32k", "64k",     
                           "125k", "250k", "500k", "1mln"]
        self.guaranteed_list =[0, "1k", "32k", "1mln"]
        self.money = {"values": self.money_list,
                      "guaranteed": self.guaranteed_list
                      }
        self.question_number = 0
        self.used_questions = []

    def get_random_int(self, in_range):     
        random = randint(0, in_range)
        if random not in self.used_random:
            self.used_random.append(random)     
            return random
        else:
            return self.get_random_int(in_range)            

    def make_random_question(self):
        self.question_number += 1
        file = open("questions.txt", 'r')
        lines = [line[:-1] for line in file]
        questions = lines[0::5]                 
        self.good_answers = lines[2::5]        
        question_number = randint(0, len(questions) - 1)        
        self.question = questions[question_number]          
        if self.question in self.used_questions:
            self.make_random_question()
        else:
            self.used_questions.append(self.question)
            options = lines[question_number * 5 + 1: (question_number + 1) * 5]
            self.option_1 = options[self.get_random_int(3)]
            self.option_2 = options[self.get_random_int(3)]
            self.option_3 = options[self.get_random_int(3)]
            self.option_4 = options[self.get_random_int(3)]
            self.used_random = []

