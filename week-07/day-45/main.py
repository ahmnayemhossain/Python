class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            user_answer = input(question.prompt + " ").strip().lower()
            if user_answer == question.answer.lower():
                self.score += 1
        print(f"Final score: {self.score}/{len(self.questions)}")


question_bank = [
    Question("Capital of Bangladesh?", "Dhaka"),
    Question("2 + 2 = ?", "4"),
    Question("Python is a programming language? yes/no", "yes"),
]

quiz = Quiz(question_bank)

print("Welcome to Quiz App CLI!")
quiz.run()
