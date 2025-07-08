
from tkinter import*
import random
window=Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x500")
window.configure( bg="#ed7e7e")

result=StringVar()
computer_choice=StringVar()


def play(user_choice,computer_choice,result):
    options=["Rock","Paper","Scissor"]
    comp_choice=random.choice(options)
    computer_choice.set(f"computer chose:{comp_choice}")

    if user_choice==comp_choice:
        result.set("Its a Tie!")
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result.set("You Win! 🎉")
    else:
        result.set("You Lose 😢")

l1=Label(window,text="Choose Rock,Paper or Scissors",font=("Arial",15,"bold"))
l1.place(x=30,y=50,height=30,width=340)

b1=Button(window,text="Rock",width=10,font=("Arial",10,"bold"),command=lambda:play("Rock",computer_choice,result))
b1.place(x=25,y=100,height=23,width=110)
b2=Button(window,text="Paper",width=10,font=("Arial",10,"bold"),command=lambda:play("Paper",computer_choice,result))
b2.place(x=150,y=100,height=23,width=110)
b3=Button(window,text="Scissor",width=10,font=("Arial",10,"bold"),command=lambda:play("Scissor",computer_choice,result))
b3.place(x=270,y=100,height=23,width=110)

Label(window,textvariable=computer_choice,font=("Arial",15,"bold")).place(x=60,y=150,height=25,width=280)
Label(window,textvariable=result,font=("Arial",15,"bold")).place(x=60,y=200,height=25,width=280)


window.mainloop()