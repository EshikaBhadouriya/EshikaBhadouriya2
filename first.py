#                                            QUIZ GAME                                                              #

play=input("Do you want to play:- ")
if play.lower()!="yes":
    quit()
print("Okay! Let's play :)")
score=0

answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("What does PSU stands for? ")
if answer.lower()=="power supply":
    print("correct")
    score+=1
else:
    print("incorrect")

print("You Got:-" + str(score))

# "You Got" is a string
 #   score is integer #
 # string+integer not defined so we converted score in string to concat with string#

print("You Got:-" + str((score/4)*100) + "%")
#here 4=number of Qestions#
