

class QuestionInfo:
	def __init__(self, qID, question, image):
		self.qID = qID
		self.question = question
		self.image = image


class QuizMain:

	# Returns the ID of the current question
	def __currID(self):
		return self.qDatabase[self.currDatabaseIndex]

	# Retrieve the information for the current question.
	# Returns a QuestionInfo object containing the information for the current question.
	def getQuestionInfo(self):
		qID = self.__currID()
		question = getQuestionLabel( qID )
		imageFile = getQuestionImage( qID )
		return QuestionInfo( qID, question, imageFile)

	# Increments the current question to the next in the database.
	# Returns false if there is no next question.
	def updateToNextQuestion(self):
		self.currDatabaseIndex = self.currDatabaseIndex + 1
		if self.currDatabaseIndex >= self.qDatabase.length:
			return False
		self.currQuestion = self.getQuestionInfo()
		return True

	# Accepts a user userGuess and compares it to the true answer.
	# Returns true if they userGuess is right, false if not.
	def submitAnswer(self, userGuess):
		trueAnswer = getQuestionAnswer()
		isCorrect = (trueAnswer == userGuess)
		# handle whether trueAnswer is correct or not
		if isCorrect:
			self.updateToNextQuestion()

		return isCorrect


	# Start the operation of the game
#	def main(self):
		# initialize the GUI

	# Initialize the internal state of the quiz game, drawing info from the database
	def __init__(self):
		self.qDatabase = getQuestions()
		self.currDatabaseIndex = 0
		self.currQuestion = self.getQuestionInfo()


if __name__ == "__main__":
	quiz = QuizMain()
	quiz.main()

