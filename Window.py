from tkinter import *
from Question import *
from Bonuses import *
from tkinter import messagebox
import time


class Window:

    def __init__(self, width=720, height=720):      
        self.width = width
        self.height = height
        self.root = Tk()
        self.background_label = Label()             
        self.questions = Question()
        self.money_you_have = 0
        self.money_label = Label()
        self.question_label = Label()
        self.option_1_label = Label()
        self.option_2_label = Label()
        self.option_3_label = Label()
        self.option_4_label = Label()
        self.number_of_question_label = Label()
        self.bonus_1_label = Label()
        self.bonus_2_label = Label()
        self.bonus_3_label = Label()
        self.walkaway_label = Label()
        self.guaranteed_money = 0

    def set_background_window_parameters(self):
        self.root.resizable(False, False)           
        self.root.iconbitmap("millionaire_icon.ico")
        self.root.title("Who Wants To Be A Millionaire")
        self.root.geometry(str(self.width) + "x" + str(self.height))    
        background = PhotoImage(file="background.png")
        self.background_label = Label(self.root, image=background)      
        self.background_label.image = background
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        play_button = Button(self.root, text="PLAY", bg="blue", command=self.set_play_background_parameters)     
        play_button.place(height=50, width=120, x=100, y=100)
        quit_button = Button(self.root, text="QUIT", bg="blue", command=self.root.destroy)
        quit_button.place(height=50, width=120, x=100, y=250)

    def set_play_background_parameters(self):
        background = PhotoImage(file="play_background.png")
        self.background_label = Label(self.root, image=background)
        self.background_label.image = background
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.set_question_background()

    def set_question_background(self):
        self.questions.make_random_question()
        self.set_other_labels()
        self.set_options()
        self.draw_bonuses()

    def draw_question(self):
        self.questions.make_random_question()
        if not self.bonus_1_label.winfo_exists():
            self.option_1_label.destroy()
            self.option_2_label.destroy()
            self.option_3_label.destroy()
            self.option_4_label.destroy()
            self.set_options()
        self.question_label.config(text=self.questions.question, fg="white")
        self.option_1_label.config(text=self.questions.option_1, fg="white")
        self.option_2_label.config(text=self.questions.option_2, fg="white")
        self.option_3_label.config(text=self.questions.option_3, fg="white")
        self.option_4_label.config(text=self.questions.option_4, fg="white")
        self.number_of_question_label.config(text="Question number " + str(self.questions.question_number))

    def check_answer(self, option):
        if option.cget("text") in self.questions.good_answers:
            time.sleep(1)
            option.config(fg="green")
            if str(self.money_you_have) == "1mln":
                messagebox.showinfo("Congratulations!", "Congratulations! You are now millionaire! Thanks for playing!")
                self.root.destroy()
            else:
                option.bind("<Button 1>", lambda l: self.check_answer(option))
                self.money_you_have = self.questions.money_list[self.questions.question_number]
                self.update_money(self.money_you_have)
                messagebox.showinfo("Correct!", " Correct! Now you have " + str(self.money_you_have)+"$")
                self.draw_question()
        else:
            option.config(fg="red")
            time.sleep(1)
            messagebox.showinfo("You Lost", "You lost! Your prize is: "+str(self.guaranteed_money)+"$")
            self.root.destroy()

    def draw_bonuses(self):
        img1 = PhotoImage(file="5050.png")
        img2 = PhotoImage(file="callFriend.png")
        img3 = PhotoImage(file="audienceHelp.png")
        self.bonus_1_label = Label(self.root, image=img1)
        self.bonus_2_label = Label(self.root, image=img2)
        self.bonus_3_label = Label(self.root, image=img3)
        self.bonus_1_label.image = img1
        self.bonus_2_label.image = img2
        self.bonus_3_label.image = img3
        self.bonus_1_label.place(x=250, y=10)
        self.bonus_2_label.place(x=330, y=10)
        self.bonus_3_label.place(x=410, y=10)
        self.bonus_1_label.bind("<Button-1>", lambda l: self.call_bonus_1())
        self.bonus_2_label.bind("<Button-1>", lambda l: self.call_bonus_2())
        self.bonus_3_label.bind("<Button-1>", lambda l: self.call_bonus_3())

    def set_options(self):
        self.option_1_label = Label(self.root, text=self.questions.option_1, bg="black", fg="white")
        self.option_2_label = Label(self.root, text=self.questions.option_2, bg="black", fg="white")
        self.option_3_label = Label(self.root, text=self.questions.option_3, bg="black", fg="white")
        self.option_4_label = Label(self.root, text=self.questions.option_4, bg="black", fg="white")
        self.option_1_label.config(font=("Courier", 18))
        self.option_2_label.config(font=("Courier", 18))
        self.option_3_label.config(font=("Courier", 18))
        self.option_4_label.config(font=("Courier", 18))
        self.option_1_label.place(x=170, y=257)
        self.option_2_label.place(x=170, y=322)
        self.option_3_label.place(x=170, y=387)
        self.option_4_label.place(x=170, y=452)
        self.option_1_label.bind("<Button-1>", lambda l: self.check_answer(self.option_1_label))
        self.option_2_label.bind("<Button-1>", lambda l: self.check_answer(self.option_2_label))
        self.option_3_label.bind("<Button-1>", lambda l: self.check_answer(self.option_3_label))
        self.option_4_label.bind("<Button-1>", lambda l: self.check_answer(self.option_4_label))

    def set_other_labels(self):
        walkaway = PhotoImage(file="walkaway.png")
        self.walkaway_label = Label(self.root, image=walkaway)
        self.walkaway_label.image = walkaway
        self.walkaway_label.place(x=700, y=10)
        self.walkaway_label.bind("<Button-1>", lambda l: self.walkaway())
        self.number_of_question_label = Label(self.root, text="Question number " + str(self.questions.question_number),
                                              bg="black", fg="red")
        self.number_of_question_label.config(font=("Courier", 18))
        self.number_of_question_label.place(x=150, y=90)
        self.question_label = Label(self.root, text=self.questions.question, bg="black", fg="white")
        self.question_label.config(font=("Courier", 18))
        self.question_label.place(x=100, y=150)
        self.money_label = Label(self.root, text="You have: " + str(self.money_you_have) + "$", bg="black", fg="red")
        self.money_label.config(font=("Courier", 18))
        self.money_label.place(x=10, y=10)

    def update_money(self, money):
        if money in self.questions.money["guaranteed"]:
            self.guaranteed_money = money
        self.money_label.config(text="You have: "+ str(money)+"$")

    def call_bonus_1(self):
        Bonuses(self.option_1_label, self.option_2_label,
                self.option_3_label, self.option_4_label,
                self.questions.good_answers).fifty_fifty()
        self.bonus_1_label.destroy()

    def call_bonus_2(self):
        Bonuses(self.option_1_label, self.option_2_label,
                self.option_3_label, self.option_4_label,
                self.questions.good_answers).call_friend()
        self.bonus_2_label.destroy()

    def call_bonus_3(self):
        Bonuses(self.option_1_label, self.option_2_label,
                self.option_3_label, self.option_4_label,
                self.questions.good_answers).audience_help()
        self.bonus_3_label.destroy()

    def walkaway(self):
        messagebox.showinfo("Winner!", "You won "+ str(self.money_you_have)+"$")
        self.root.destroy()

    def loop_window(self):
        self.root.mainloop()