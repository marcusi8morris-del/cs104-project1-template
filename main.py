## [Personality Test]
# Author: [Marcus Morris]
# A quiz/questionaire progrma built for CS 104 Project 1

print("Welcome to your personality test!")
print("You will answer some questions to determine what type of personality you have!")
print()

# Store core
total_score = 0

# Helper function for yes/no questions
def ask_question(prompt):
    while True:
        answer = input(prompt + " (yes/no): ").lower().strip()
        if answer == "yes":
            return 1
        elif answer == "no":
            return 0
        else:
            print("Please type 'yes' or 'no'.")
    
def run_personality_test():
    questions
print("Do I enjoy working in a team-oriented environment?")

print("Do I handle stress well under pressure?")

print("Do I handle conflict?")

print("Do I have the ability to persuade people to do almost anything?")

print("Do I often feel like I take too much responsibility?")
        

total_score = 0

if total_score == 4:
    print("You are confident, resilient, and thrive under pressure.")
elif total_score == 2:
    print("You are balanced and adapt depending on the situation.")
else:
    print("You prefer independence and calmer environments.")

print("\nThank you for taking the personality test!")
