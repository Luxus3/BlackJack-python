import time
import random

# Proyecto de blackjack en Python para el CMD (estoy aburridisimo en mi casa)

# Maximo 5 Jugadores.

# -------------------------------CODE------------------------------------------

Userone = 0
Usertwo = 0
Userthree = 0
Userfour = 0
Userfive = 0
Cards = random.randint(1, 11)
Cards_2 = random.randint(1, 11)
crupier_cards = random.randint(4, 21)


Playerdefinitions = int(input("How many players are going to play this round of BlackJack: 1,2,3,4,5 \n Answer:"))

if Playerdefinitions == 1:
     print("Selected 1 player as a solitary game.")
     time.sleep(1)
     print("starting game in 2 seconds")
     time.sleep(2)
     print("Okay so we are starting the round,\nI will give you a card in 1 sec")
     time.sleep(1)
     print(Cards)
     Cards + Userone
     while True:
          opcion = int(input("Do you want another card?: 1)Yes 2)No \nAnswer: "))
          if opcion == 1:
               print(Cards_2)
               Cards_2 + Userone
          elif opcion == 2:
               print("Okay! That´s it.. Wait a second..")
               break
          else:
               print("Your answer its outside of my mind man")
if Userone > 21:
     time.sleep(1)
     print("You lose, you have more than 21 cards")
if Userone == 21:
     time.sleep(1)
     print("""
__        ______  _    _   _      ____   _    __    
\\ \\   / / __ \\| |  | | | |    / __ \\ | \\ | |    | | |
 \\ \\_/ / |  | |  |  | | | |   | |  | | |  \\| |    | | |
  \\   / | |  | |  |  | | | |   | |  | | | . ` |     | | |
    | |  | |__| |  |__| | | |___| |__| | | |\\  |    |_|_|
    |_|  \\____/ \\____/  |______\\____/ |_| \\_|     (_)
                                                                      
                     BLACKJACK 21! YOU WON! 🃏🎉
""")
elif Userone > crupier_cards :
     print("Yoou won the round!!")
     time.sleep(1)
elif Userone < crupier_cards :
     time.sleep(1)
     print("ohh you lose the round, the crupier has got more points than you")
     time.sleep(1)
else : 
 print(f"You have {Userone} points")

          
      

      
        

          
    

        
       

            
        
   
   
#if Playerdefinitions == 2:
   #print("Selected 2 player as a solitary game")

#if Playerdefinitions == 3:
   #print("Selected 3 player as a solitary game")

#if Playerdefinitions == 4:
   #print("Selected 4 player as a solitary game")

#if Playerdefinitions == 5:
   #print("Selected 5 player as a solitary game")



