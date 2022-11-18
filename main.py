from tkinter import *
import random
from PIL import Image, ImageTk
import os

root = Tk()

root.geometry("1000x600+300+100")
root.configure(bg="white")
root.resizable(False, False)

###### Variables ######

user_choice = ""
computer_choice = ""
user_score = 0
computer_score = 0

############### functions #############

def rock(event=None):
    global user_choice
    user_choice = "rock"
    blank1.config(image=rock_image)
    main(user_choice)

def paper(event=None):
    global user_choice
    user_choice = "paper"
    blank1.config(image=paper_image)
    main(user_choice)

def scissor(even=None):
    global user_choice
    user_choice = "scissor"
    blank1.config(image=scissor_image)
    main(user_choice)


def main(user_choice):
    global computer_choice, computer_score, user_score
    randint = random.randint(1, 3)
    if randint == 1:
        computer_choice = "rock"
        blank2.config(image=rock_image)
    elif randint == 2:
        computer_choice = "paper"
        blank2.config(image=paper_image)
    elif randint == 3:
        computer_choice = "scissor"
        blank2.config(image=scissor_image)

    if user_choice == computer_choice:
        user_score += 0
        computer_score += 0
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="Match was draw", fg="blue")
        answer.place(x=350, y=300)
    elif user_choice == "rock" and computer_choice == "paper":
        computer_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="Computer grabbed your rock", fg="red")
        answer.place(x=250, y=300)
    elif user_choice == "rock" and computer_choice == "scissor":
        user_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="You broke scissor", fg="green")
        answer.place(x=330, y=300)
    elif user_choice == "paper" and computer_choice == "rock":
        user_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="you grabbed the rock", fg="green")
        answer.place(x=300, y=300)
    elif user_choice == "paper" and computer_choice == "scissor":
        computer_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="Computer cutted the paper", fg="red")
        answer.place(x=250, y=300)
    elif user_choice == "scissor" and computer_choice == "rock":
        computer_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="Computer broke scissor", fg="red")
        answer.place(x=300, y=300)
    elif user_choice == "scissor" and computer_choice == "paper":
        user_score += 1
        us_score.config(text="Your score :- " + str(user_score))
        cp_score.config(text="Computer score :- " + str(computer_score))
        answer.config(text="You cutted the paper", fg="green")
        answer.place(x=300, y=300)
    else:
        answer.cofig(text="something went wrong !")

path = os.getcwd() + "\\"
########### Image work ################
image1 = Image.open(path + os.path.join('images', 'rock.jpg'))
rock_image = ImageTk.PhotoImage(image1)

image2 = Image.open(path + os.path.join('images', 'paper.jpg'))
paper_image = ImageTk.PhotoImage(image2)

image3 = Image.open(path + os.path.join('images', 'scissor.jpg'))
scissor_image = ImageTk.PhotoImage(image3)

image4 = Image.open(path + os.path.join('images', 'blank.jpg'))
blank_image = ImageTk.PhotoImage(image4)

rock = Button(root, border=0, image=rock_image, height=163, width=130, bg="white", command=rock)
rock.pack()
rock.place(x=100, y=400)

paper = Button(root, border=0, image=paper_image, bg="white", command=paper)
paper.place(x=450, y=400)

scissor = Button(root, border=0, image=scissor_image, bg="white", command=scissor)
scissor.place(x=800, y=400)

blank1 = Label(root, image=blank_image, bg="white", height=163, width=130)
blank1.place(x=200, y=120)

blank2 = Label(root, image=blank_image, bg="white", height=163, width=130)
blank2.place(x=700, y=120)

vs = Label(root, text="VS", font=("Didot",80,"bold"), fg="red", bg="white")
vs.place(x=430, y=140)

answer = Label(root, text="", bg="white", fg="black", font=("arial",30,"italic bold"))
answer.place(x=250, y=300)

us_score = Label(root, text="Your Score :- 0", bg="white", fg="orange", font=("arial",30,"italic bold"))
us_score.place(x=10, y=10)
cp_score = Label(root, text="Computer Score :- 0", bg="white", fg="orange", font=("arial",30,"italic bold"))
cp_score.place(x=600, y=10)

root.mainloop()