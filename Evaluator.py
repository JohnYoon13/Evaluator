'''INSTRUCTIONS: In your terminal, enter " python Evaluator.py".
A prompt will appear to ask for your expression. Type your
expression with only INTEGERS and the ADDITION and SUBTRACTION
operators, separated by a space. Press Enter to see your result.'''


#Function (whose parameter is a space delimited string), that
#evaluates simple mathematical expressions, specifically supporting
#the two operator types of addition and subtraction for only INTEGERS.

def expressionEvaluator(string):
	operations = set(["+", "-"])
	numbers = []
	total = 0
	
	#Loop through each character in the expression
	#in reverse order (reverse, because we must have the
	#ability to nest one expression inside another).

	for character in reversed(string):
		#If the character is not an empty space,
		#then evaluate whether it is a number or operator.

		if character != " ":
			#If the character is a number, then add it
			#to the numbers list to be later used with the operators.
			#If there is only one number in the expression, then
			#simply return the aforementioned number.

			if character not in operations:
				numbers.append(int(character))
				if len(string) == 1:
					return numbers[0]
			#If the character is an operator, then
			#add or subtract the relevant numbers, 
			#depending on which operator is present.
			#In order to handle any possible nested expression
			#cases, after using the operators, reset the numbers
			#list by popping numbers[1] and setting numbers[0] to total.

			else:
				if character == "+":
					total = numbers[0] + numbers[1]
					numbers.pop()
					numbers[0] = total
				elif character == "-":
					total = numbers[1] - numbers[0]
					numbers.pop()
					numbers[0] = total

	return total



#Ask the user to provide the expression that they want to be evaluted,
#and then take that input and insert it into the expressionEvaluator function.
#Print the result.

string = input("\nType your expression to be evaluated:\n")
print("Your RESULT is: " + str(expressionEvaluator(string)) + "\n")






