from random import randint
from tkinter import messagebox


class Bonuses:

    def __init__(self, opt1, opt2, opt3, opt4, good_answers):
        self.options = [opt1, opt2, opt3, opt4]
        self.good_answers = good_answers

    def fifty_fifty(self):
        counter = 0
        for option in self.options:
            if option.cget("text") not in self.good_answers and counter <= 1:
                option.destroy()
                counter += 1

    def call_friend(self):
        for option in self.options:
            if option.cget("text") in self.good_answers:
                messagebox.showinfo("Call Friend", "Friend said that he is sure that it will be: "+option.cget("text"))
                option.config(fg="green")

    def audience_help(self):
        for option in self.options:
            if option.cget("text") in self.good_answers:
                answer = dict(opt=option.cget("text"), percentage=randint(75, 99))
        messagebox.showinfo("Audience", "Most of audience: "+str(answer["percentage"])+
                            "% have chosen option : "+ answer["opt"])
