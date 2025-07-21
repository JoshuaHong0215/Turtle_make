import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-300,-300)
player_one.setheading(90)

player_two = player_one.clone()
player_two.color("blue")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200,-300)
player_two.setheading(90)

player_third = player_one.clone()
player_third.color("red")
player_third.shape("turtle")
player_third.penup()
player_third.goto(-100, -300)
player_third.setheading(90)

player_fourth = player_one.clone()
player_fourth.color("yellow")
player_fourth.shape("turtle")
player_fourth.penup()
player_fourth.goto(0, -300)
player_fourth.setheading(90)

player_fifth = player_one.clone()
player_fifth.color("black")
player_fifth.shape("turtle")
player_fifth.penup()
player_fifth.goto(100, -300)
player_fifth.setheading(90)

player_sixth = player_one.clone()
player_sixth.color("deeppink")
player_sixth.shape("turtle")
player_sixth.penup()
player_sixth.goto(200, -300)
player_sixth.setheading(90)

player_seventh = player_one.clone()
player_seventh.color("brown4")
player_seventh.shape("turtle")
player_seventh.penup()
player_seventh.goto(300, -300)
player_seventh.setheading(90)


#골대 그리는 코드
player_one.goto(-200,250)
player_one.setheading(0)
player_one.pendown()
for _ in range(2):
    player_one.forward(400)
    player_one.right(90)
    player_one.forward(20)
    player_one.right(90)
player_one.penup()    
player_one.goto(-300,-300)
player_one.setheading(90)




die = [1,2,3,4,5,6]

for i in range(20):
    if player_one.pos()[1] >= 250:
        print("Player one WINS!!")
        break
    elif player_two.pos()[1] >= 250:
        print("Player two WINS!!")
        break
    elif player_third.pos()[1] >= 250:
        print("Player third WINS!!")
        break
    elif player_fourth.pos()[1] >= 250:
        print("Player fourth WINS!!")
        break
    elif player_fifth.pos()[1] >= 250:
        print("Player fifth WINS!!")
        break
    elif player_sixth.pos()[1] >= 250:
        print("Player sixth WINS!!")
        break
    elif player_seventh.pos()[1] >= 250:
        print("Player seventh WINS!!")
        break
    
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)
        player_third_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_third.fd(20*die_outcome)
        player_fourth_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_fourth.fd(20*die_outcome)
        player_fifth_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_fifth.fd(20*die_outcome)
        player_sixth_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_sixth.fd(20*die_outcome)
        player_seventh_turn = input("Press 'Enter' to roll the die ")   #num
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_seventh.fd(20*die_outcome)
        
    
        
