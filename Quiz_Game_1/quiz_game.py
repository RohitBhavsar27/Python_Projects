print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")

if(playing.lower() != "yes"):
    quit()
print("Okay! Let's play : )")

score = 0


answer = input("1. What does CPU stand for? ")
if(answer.lower() == "central processing unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("2. What does GPU stand for? ")
if(answer.lower() == "graphics processing unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("3. What does RAM stand for? ")
if(answer.lower() == "random access memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("4. What does PSU stand for? ")
if(answer.lower() == "power supply unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("5. What does ROM stand for? ")
if(answer.lower() == "read only memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!") 
print("You got " + str((score/5) * 100) + "%.") 
