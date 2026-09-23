# [Personality Test]
# Author: [Marcus Morris]
# A quiz/questionaire progrma built for CS 104 Project 1

print("Welcome to your personality test!")
print("You will answer some questions to determine what type of personality you have!")
print()

# Store core
total_score = 0

# Helper function for yes/no questions
def ask_questions(promt)
while True: 
  answer = input(prompt + " (yes/no): "). lower() .strip()
  if answer == "yes" : 
    return 1 
  elif answer == "no" :
    return 0
  else: 
print("Please type 'yes' or 'no'.")

def run_personality_test():
    questions = [
        "1. Do I enjoy working in a team-oriented environment?",
        "2. Do I handle stress well under pressure?",
        "3. Do I handle conflict well?",
        "4. Do I have the ability to persuade people to do almost anything?",
        "5. Do I often feel like I take too much responsibility upon myself?"
    ]

total_score = 0

 print("\n--- Personality Test Results ---")

    if total_score >= 4:
        print("You are confident, resilient, and thrive under pressure.")
    elif total_score >= 2:
        print("You are balanced and adapt depending on the situation.")
    else:
        print("You prefer independence and calmer environments.")

    print("\nThank you for taking the personality test!")
   


       
# TODO: Display the final results to the user.
