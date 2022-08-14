"""
A Simple quiz game written in Python for practice and education.
"""

class Game:
    def __init__(self, questions: list, answers: list):
        self.questions = questions
        self.answers = answers
        self.current_index = 0
        self.round = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.questions_asked = 0
        self.score = 0
        self.winning_score = 10
        self.current_answer = -1
        self.running = True

    def update(self):
        # Update the current game and either ask the next question or end the game.
        pass

    def ask_question(self):
        # Check if the current index is less than the total number of questions.
        if self.current_index < len(self.questions):
            print(self.questions[self.current_index])
            print(f"Choose and option below:")
            for i in enumerate(self.answers[self.current_index]):
                print(f"{i[0] + 1}. {self.answers[self.current_index][i[0]]['answer']}")
            self.questions_asked += 1
            self.current_answer = int(input())
            self.check_answer()
        else:
            print("No more questions!")
            self.running = False

    def check_answer(self):
        # Make sure we have a valid index.
        if not self.current_answer == -1:
            if self.answers[self.current_index][self.current_answer - 1]['correct']:
                print("Correct!")
                self.score += 100
                self.correct_answers += 1
            else:
                print("Incorrect!")
                self.incorrect_answers += 1
        self.current_index += 1






if __name__ == '__main__':
    questions = ["What is the capitol of Kansas?",
                 "What color is a stop sign?",
                 "How many eggs are in a dozen?",
                 "The tides are controlled by the Sun's gravity on the Earth"]

                # Question 1
    answers = [[{"answer": "Juno", "correct": False},
                {"answer": "Bakersfield", "correct": False},
                {"answer": "Bangor", "correct": False},
                {"answer": "Topeka", "correct": True}],
                # Question 2
               [{"answer": "Blue", "correct": False},
                {"answer": "Green", "correct": False},
                {"answer": "Red", "correct": True},
                {"answer": "Purple", "correct": False},
                {"answer": "Orange", "correct": False}],
                # Question 3
               [{"answer": 5, "correct": False},
                {"answer": 9, "correct": False},
                {"answer": 12, "correct": False},
                {"answer": 18, "correct": False}],
                # Question 4
               [{"answer": True, "correct": False},
                {"answer": False, "correct": True}]]
    game = Game(questions, answers)


    while game.running:
        game.ask_question()

    print(f"""
            Final Score: {game.score}            
            {game.questions_asked} questions asked!
            
            Correct Answers: {game.correct_answers} - {round((game.correct_answers / game.questions_asked) * 100, 2)}%
            Incorrect Answers: {game.incorrect_answers} - {round((game.incorrect_answers / game.questions_asked) * 100, 2)}%
            
            Thanks for Playing Simple Quiz Game!
        """)

