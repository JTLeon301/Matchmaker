# Jaiden Leonard
# jaidentleonard@lewisu.edu
# CPSC-20000

import os
import time

INTRODUCTION = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 Welcome my love,
		Today you will be taking a test...
        To see how pure our love can be!
  Please answer the questions in the form of 1 through 5;
  1 being strongly disagree and 5 being strongly agree.
  But be careful, this relationship is within your grasp.
        Don't be foolish, answer them honestly.
         I will be awaiting your response! :D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

QUESTION = [
	'Hockey is the best sport to watch.',
	'Working on and modifying cars is a fun hobby and past-time.',
	'Video games can be relaxing and enjoyable to play.',
	'Dogs are the best pets to exist.',
	'I would like to live in a big and bustling city.'
]

DESIRED_RESPONSE = [
	4, # agree
	5, # strongly agree
	4, # agree
	3, # median
	1  # strongly disagree
	
]

# Weighted question compatibility scores
WEIGHTS = [
    2, # weight of question 1
    3, # weight of question 2
    2, # weight of question 3
    1, # weight of question 4
    2  # weight of question 5
]

MAX_SCORE = 25

# Beginning of program
os.system('clear')
print(INTRODUCTION)

response = []
compatibility = []
weighted_compatibility = []

# Asking questions (I found a thread about the validation on Reddit lol)
for i in range(len(QUESTION)):
    while True:
        try:
            userResponse = int(input(QUESTION[i]))
            if userResponse < 1 or userResponse > 5:
                raise ValueError("Don't you know how to read; Pick a number between 1 through 5.")
            break
        except ValueError as e:
            print(f'{e}')

    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)

    # Calculate weighted question compatibility score
    weighted_totalCompatibility = WEIGHTS[i] * questionCompatibility
    weighted_compatibility.append(weighted_totalCompatibility)

    # Print regular and weighted compatibility scores
    print(f"Question {i+1} compatibility: {questionCompatibility}")
    print(f"Question {i+1} weighted compatibility: {weighted_totalCompatibility}\n")

# Adjusting weights (Had to use google because my weights were going above 100%)
TOTAL_WEIGHT = sum(WEIGHTS)
WEIGHTS = [w * MAX_SCORE // TOTAL_WEIGHT for w in WEIGHTS]

# Total compatibility calculations
totalCompatibility = sum(compatibility)
weighted_totalCompatibility = sum(weighted_compatibility)

# Cap weighted total compatibility score to 25 (Had to use google because my weights were going above 100%)
if weighted_totalCompatibility > MAX_SCORE:
    weighted_totalCompatibility = MAX_SCORE

# Percentage conversion
percentCompatibility = totalCompatibility * 100 / MAX_SCORE
percentWeightedCompatibility = weighted_totalCompatibility * 100 / MAX_SCORE


print("Calculating if you were the perfect match...")
time.sleep(3)

if percentCompatibility >= 90:
    print("Ayo, send me your phone number right now -jaidentleonard@lewisu.edu. We're a perfect match!")
elif percentCompatibility >= 70:
    print("I can be able to work with this, there just might need to be some accommodations on your end...")
else:
    print("It's not you, It's me. Actually, no. It's you. You're the problem.")

print(f"Total Compatibility: {percentCompatibility:.2f}%")
print(f"Total Weighted Compatibility: {percentWeightedCompatibility:.2f}%\n")
