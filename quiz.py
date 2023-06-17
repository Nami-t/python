print("welcome to quiz")
play = input("do you want to play? ")
if play.lower() != "yes":
    quit()

print("okay lets play : ")
score=0

answer = input ("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct')
    score+=1
else:
    print('incorrect')

answer = input ("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct')
    score+=1
else:
    print('incorrect')

answer = input ("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct')
    score+=1
else:
    print('incorrect')

answer = input ("what does PSU stand for?")
if answer.lower() == "power supply unit":
    print('correct')
    score+=1
else:
    print('incorrect')

print("you got "+str(score)+" points")
print("you got "+str((score/4)*100)+"%")

