import random
from tkinter import*


#Dictionary and vars
anurag = {
"rock":{"rock":1,"paper":0,"scissor":2},
"paper":{"rock":2,"paper":1,"scissor":0},
"scissor":{"rock":0,"paper":2,"scissor":1}

}


computer_score = 0
player_score = 0


#Functions

def outcome_handler(user_choice):
 global computer_score
 global player_score
 outcomes = ["rock","paper","scissor"]
 random_number = random.randint(0,2)
 computer_choice = outcomes[random_number]
 result = anurag[user_choice][computer_choice]

 player_choice_label.config(fg="red",text="Player_Choice: "+str(user_choice))
 computer_choice_label.config(fg="green",text="Computer_Choice: "+str(computer_choice)) 

 if result ==2:
    player_score = player_score + 2
    player_score_label.config(text="Player :"+ str(player_score))
    output_label.config(fg="blue",text="Outcome : Player Won")

 elif result ==1:
    player_score = player_score + 1 # Increment both scores by 1 for draw
    computer_score = computer_score + 1 
    player_score_label.config(text="Player :"+ str(player_score))
    computer_score_label.config(text="Computer :"+ str(computer_score))
    output_label.config(fg="blue",text="Outcome : Draw")
    
 elif result == 0:
   computer_score = computer_score + 2 
   computer_score_label.config(text="Computer :"+ str(computer_score))
   output_label.config(fg="blue",text="Outcome : Computer Won")

    


  



# Main screen
master = Tk()
master.title("GAME")




#Labels
Label(master,text="Rock,Paper,Scissor",font=("Calibri", 14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="Please select an option",font=("Calibri", 12)).grid(row=1,sticky=N)
player_score_label = Label(master,text="Player: 0",font=("Calibri", 12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(master,text="Computer: 0",font=("Calibri", 12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label = Label(master,font=("Calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(master,font=("Calibri",12))
computer_choice_label.grid(row=3,sticky=E)

output_label = Label(master,font=("Calibri",12))
output_label.grid(row=3,sticky=N)


#Buttons
Button(master,text="Rock",width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(master,text="Paper",width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,padx=5,pady=5)
Button(master,text="Scissor",width=15,command=lambda:outcome_handler("scissor")).grid(row=4,sticky=E,padx=5,pady=5)

#Dummy label
Label(master).grid(row=5)

master.mainloop()
