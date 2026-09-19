# [Personality Test]
> "How well do you  really know yourself?" 

## Overview
>  This program's focus is to describe someone's personality based on answers to questions and situations
> The program is a personality test, and the final output is your personality type. 
> You will answer some questions with the responses (Yes/No)
>
## Sample Questions and Responses
> 1. Do I enjoy working in a team-oriented environment? 
> 2. Do I handle stress well under pressure?
> 3. Do I handle conflict well?
> 4. Do I have the ability to persuade people to do almost anything?
> 5. Do I often feel like I take too much responsibility upon myself? 
>
> 
> 1. Do I enjoy working in a team-oriented environment?
> Yes
> No   
> 2. Do I handle stress well under pressure?
> Yes
> NO
> 3. Do I handle conflict well?
> Yes
> No
> 4. Do I have the ability to persuade people to do almost anything?
> Yes
> No
> 5. Do I often feel like I take too much responsibility upon myself?
> Yes
> NO
## Variables
> `questions`(list of str): stores all five questions so they can be looped through one at a time.
> `question-text`(str): the individual question currently being displayed to the user; passed into ask_question() as a parameter.
> `answer`(str): the user's typed response ("yes" or "no") lowercased and trimmed for comparison.
> `total_score`(int): single running tally of points. One variable works here because the result is based on a cumulative total, not separate competing categories.
> `question`(str): the loop variable that holds the current question as the program moves through the questions list.
> `result`(int): the 0 or 1 returned by ask_question() for the current question, added into total_score.
> `score`(int): a single running tally of points. One variable works here because the result is based on a cumulative total, not separate competing categories.    
> message`(str): the result text being built inside get_result_message() to determine which result message to return.
> `final_score`(int): stores the completed quiz score once all questions have been answered.
> `result_text`(str): stores the final message returned to the user, ready to be printed.  
>
## Conditional Logic Outline
> Example:
> - **Conditional statement 1** — related to each yes/no question
>  `if` answer is "yes": return 1 (add a point to the total score) 
>  `elif` answer is "no": return 0 (adds nothing to the total score)  
>  `else` : display a message asking the user to type "yes" or "no", and ask the question again (this is a loop, not a branch that ends the program)  
> 
>
> - **Conditional statement 2** — reveals final results based on total_score (inside get_result_message) 
>   - `if` score is 4 or 5: display message - "You're confident, resilient, and thrive under pressure".
>   - `elif` score is 2 or 3: display message - "You're confident, resilient, and thrive under pressure".
>   - `else` score is 0 or 1: display message - "You may prefer independence and calmer environments " 

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
