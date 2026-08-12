print("Very warm is very far\n","Warm is far\n","Very cold is slighly close\n", "Cold is very close\n")


secret = 29
print ("You have 5 lives.")
lives = 5
while lives > 0:
    user = int(input("Please enter your number:"))
    if user == secret:
        print("Well done! You have cracked the secret number.")
        break
    elif user - secret >= 50:
        print("You are very warm.")
    elif user - secret >= 20:
        print ("You are warm.")
        lives = lives - 1
    elif user - secret >= 10:
        print ("You are very cold.")
        lives = lives - 1
    elif user - secret <= 2:
        print("You are cold. Keep trying.")
        lives = lives - 1 
    else: print ("Unlucky! Try again.")


