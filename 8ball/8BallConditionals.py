import random

# ----- Using conditionals -----
num = random.randint(1, 8) # Generate random integer

if (num == 8): # Vary response based on integer
    response = "Yes"
elif (num == 7):
    response = "No"
elif (num == 6):
    response = "Maybe"
elif (num == 5):
    response = "Try again"
elif (num == 4):
    response = "A high chance"
elif (num == 3):
    response = "A low chance"
elif (num == 2):
    response = "Reply hazy, try again"
elif (num == 1):
    response = "Of course not"

print("Response #{0}: {1}".format(num, response)) # Print result