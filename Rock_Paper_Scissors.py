#Rock_Paper_Scissors_Game...
#The first step to play this game is that user gets to pick any option between Rock or Paper or Scissors..
#After user,System gets to select an option between these three
#Rules to Win the Game:-
#Rock vs Paper     -> Paper wins
#Rock vs Scissors  -> Rock wins
#Paper vs Scissors -> Scissors wins

#For better interaction between user and system we will be using pyttsx3 for audio of the text

#For this project,we will be random module from python libraries for enabling system to select an option
import time
import random
import pyttsx3
t=pyttsx3.init()
print("Please enter  your Name?")
t.say("Please enter  your Name?")
t.runAndWait()
Name=input()
print("\nhey",Name," ,","Lets begin our Game...\n")
t.say("Hey"+Name+" "+"Lets begin our game")
t.runAndWait()
print("But before beginning our Game I would like to remember you about rules for winning this game incase you are new to the game\n")
t.say("But before beginning our Game I would like to remember you about rules for winning this game incase you are new to the game\n")
t.runAndWait()
print("Rock_Paper_Scissors_Game...\n")
t.say("Rock Paper Scissors Game...\n")
t.runAndWait()
print("\nThe first step to play this game is that user gets to pick any option between Rock or Paper or Scissors..\n"+"\nAfter user selection,System gets to select an option between these three\n"+"\n"+"Rules to Win the Game:-\n"+"\n"+"Rock vs Paper     -> Paper wins\n"+"\n"+"Rock vs Scissors  -> Rock wins\n"+"\n"+"Paper vs Scissors -> Scissors wins\n"+"\n")
t.say("\nThe first step to play this game is that user gets to pick any option between Rock or Paper or Scissors..\n"+"\nAfter user selection,System gets to select an option between these three\n"+"\n"+"Rules to Win the Game:-\n"+"\n"+"Rock versus Paper   Paper wins\n"+"\n"+"Rock versus Scissors  Rock wins\n"+"\n"+"Paper versus Scissors  Scissors wins\n"+"\n")
t.runAndWait()
#Incase of the user wanna play it again  and again we use while loop for this:-
while(1):
    print("\nSince Iam not that capable of producing images for Rock Paper and Scissors,I would like you to choose them in the form of Integers..\n"+"\n"+"please forgive my Developer for the inconvineince....\n")
    t.say("\nSince Iam not that capable of producing images for Rock Paper and Scissors,I would like you to choose them in the form of Integers..\n"+"\n"+"please forgive my Developer for the inconvineince....\n")
    t.runAndWait()
    print(Name +" please enter your choice\n"+"\n"+"1 -> Rock\n2 -> Paper\n3 -> Scissors\n")
    t.say(Name +" please enter your choice\n"+"\n"+"1  Rock\n2  Paper\n3  Scissors\n")
    t.runAndWait()
    #Now we will be taking a variable/Identifier for storing the choice the user had made...
    option=int(input())
    while(option>3 or option<1):
        #incase user selecting a number that is not in this range
        print("\n"+Name," ,You are naughty...Please Dont tease me and select a valid choice...\n")
        t.say(Name+"You are naughty...Please Dont tease me and select a valid choice...")
        t.runAndWait()
        option=int(input())
    if(option==1):
        weapon="Rock"
    elif(option==2):
        weapon="Paper"
    else:
        weapon="Scissors"
    print("since you've got your choice...now its my turn")
    t.say("since you've got your choice...now its my turn")
    t.runAndWait()
    print("\nNow its my turn to choose Rock or  Paper or Scissors\n")
    t.say("\nNow its my turn to choose Rock or  Paper or Scissors\n")
    t.runAndWait()
    #By using random module we will be selecting system's choice against the user
    sys_option=random.randint(1,3)
    time.sleep(1)
    if(sys_option==1):
        sys_weapon="Rock"
    elif(sys_option==2):
        sys_weapon="Paper"
    else:
        sys_weapon="Scissors"
    print("\nMy choice is "+sys_weapon+"\n")
    t.say("\nMy choice is "+sys_weapon+"\n")
    t.runAndWait()
    print(weapon," Vs ",sys_weapon,"\n")
    t.say(weapon+"versus"+sys_weapon)
    t.runAndWait()
    #Now we will be checking for winning conditions of the game
    if(option==sys_option):
        print("Its a Draw\n")
        t.say("Its a Draw\n")
        t.runAndWait()
        result="Draw"
    elif(option==1 and sys_option==2):
        print("Paper wins\n")
        t.say("Paper wins\n")
        t.runAndWait()
        result="Paper"
    elif(option==2 and sys_option==1):
        print("Paper wins\n")
        t.say("Paper wins\n")
        t.runAndWait()
        result="Paper"
    if(option==1 and sys_option==3):
        print("Rock wins\n")
        t.say("Rock wins\n")
        t.runAndWait()
        result="Rock"
    elif(option==3 and sys_option==1):
        print("Rock wins\n")
        t.say("Rock wins\n")
        t.runAndWait()
        result="Rock"
    if(option==2 and sys_option==3):
        print("Scissors wins\n")
        t.say("scissors wins\n")
        t.runAndWait()
        result="Scissors"
    elif(option==3 and sys_option==2):
        print("Scissors wins\n")
        t.say("scissors wins\n")
        t.runAndWait()
        result="Scissors"
    if(result=="Draw"):
        print("\nIt's a tie\n")
        t.say("\nIt's a tie\n")
        t.runAndWait()
    elif(result==weapon):
        print("\nYou win...\n")
        t.say("\nYou win...\n")
        t.runAndWait()
    else:
        print("\nSystem win\n")
        t.say("\nSystem win...\n")
        t.runAndWait()
    print("\nDo you want to play again?(Y/N)\n")
    t.say("\nDo you want to play again?If Yes enter y else enter n \n")
    t.runAndWait()
    answer=input().lower()
    if answer=='n':
        #since user no longer wanted to play the game we will be coming out of loop
        print("\nThanks for Playing,hope you like it\n")
        t.say("\nThanks for Playing,hope you like it\n")
        t.runAndWait()
        break
    else:
        #As user wants to continue the game we will iterate the loop
        print("\nYeah Lets play again\n")
        t.say("\nYeah Lets play again\n")
        t.runAndWait()

          
        



