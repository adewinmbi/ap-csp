import random

# ----- Using Lists -----
choices = ["Yes", "No", "Maybe", "Try again", "A high chance", "A low chance", "Reply hazy, try again", "Of course not"] # List of possible results
response = random.choice(choices) # Choose random string from list

print("The 8Ball tells you: ", response) # Print result