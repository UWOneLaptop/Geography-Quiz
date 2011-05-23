from QuizMain import *

#main
quiz = QuizMain()


print "Starting the treasure hunt..."
moreQs = True
while moreQs:
	qInfo = quiz.getQuestionInfo()
	# display the question, get input
	print "Question! "+str(qInfo.question)
	
	guess = input("") #user input on a blank line
	while not quiz.submitAnswer(guess): # while !correct
		print "Yarr, try yer luck again..."
	
	print "Aha! Yer smarter than I thought..."
	moreQs = quiz.updateToNextQuestion()
#	

print "Shivar my timbars, you found all the loot!"

