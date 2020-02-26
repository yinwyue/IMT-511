# Define your functions up here!

def ask_for_name():
	# ask for the player's name
	name = input("Before we start, what's your name? ")
	if name == "":
		name = input("Could you please tell me your name? ")
	print("Hi " + name + "! Let's see how well you know me!")
	return name


def ask_multiple_choice_question(question, num_of_choices):
	print(question)
	player_answer = int(input("> "))
	if player_answer < 0 or player_answer > num_of_choices:
		print("That's invalid answer! Please answer my question!")
		player_answer = ask_multiple_choice_question(question, num_of_choices)
	return player_answer

def question_worths_100_points():
	answer = ask_multiple_choice_question("How do you like the quiz? \n1. I like it! \n2. It's awesome! \n3. It worths full Points! ",3)
	# This is the question that decides whether you are my best friend or not
	if answer == 3:
		point = 100
	else:
		point = 1
	return point

def question_worths_minus_points():
	# This is a gift for the player.
	answer = ask_multiple_choice_question("This is a given point so you won't get 0. \n1. Wrong! \n2. This is the correct answer! \n3. Don't look at me! \n4. I don't know what's happening! ",4)
	if answer == 2:
		point = 1
	else:
		 point = -50
	return point


def grade(player_answer, correct_answer):
	# player_answer, correct_answer, point should all be int
	if player_answer == correct_answer:
		point = 1
	else:
		point = 0
	return point

def ask_branching_question():
	answer1 = ask_multiple_choice_question("Do you know which building I like the most? \n1. Ode \n2. Suz \n3. MGH ",3)
	if answer1 == 3:
		print("Yeah! ")
	else: 
		print("Oh I actually like MGH best...")
	answer2 = ask_multiple_choice_question("Do you know why I like MGH? \n1. The expresso bar \n2. The lab \n3. Because I can meet you there! ",3)
	answer = [answer1, answer2]
	correct = [3, 3]
	point = sum(answer[i] == correct[i] for i in range(2))
	return point


def take_quiz():
	answer_1 = ask_multiple_choice_question("You define me as... \n1. Someone I know \n2. Teammate \n3. My friend ",3)
	points_1 = grade(answer_1, 3)
	answer_2 = ask_multiple_choice_question("Do you know what my favorite color is? \n1. UW purple \n2. Green \n3. Orange ",3)
	points_2 = grade(answer_2, 2)
	points_3 = ask_branching_question()
	points_4 = question_worths_minus_points()
	points_5 = question_worths_100_points()
	total =  points_1 + points_2 + points_3 + points_4 + points_5
	return total


def coffee_preference():
	# ask coffee preference for the final result
	coffee = input ("What's your favorite coffee? ")
	return coffee

def report_results(points, name):
	if points > 100:
		print("Oh! " + name + "! You are my best friend! ")
	elif points > 50: 
		print("I can't believe you got the wrong answer on Q5, but you are still my best friend! ")
	elif points < 0 :
		print("How can you get the wrong answer on Q5! You should do the quiz again. ")
	else:
		coffee = coffee_preference()
		if points >= 4:
			print("Great! You know a lot about me! We should have a cup of " + coffee + " someday. ")
		else:
			print("Call me and we'll have a " + coffee + " together")



if __name__ == '__main__':
	print("Hello! Welcome to the quiz! ")
	# Record the player's name so that can be used again at the end.
	player_name = ask_for_name()  # return a str
	points = take_quiz()  # return an int which is the score the player gets	
	report_results(points, player_name)
	print("Thanks for taking the quiz! ")
	
