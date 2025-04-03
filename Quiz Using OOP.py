class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions 
        self.score = 0

    def run(self):
        for question in self.questions:
            self.ask_question(question)
        self.display_score()

    def ask_question(self, question):
        print(question.prompt)
        for option in question.options:
            print(option)
        
        while True:
            answer = input("Enter your answer (A, B, C, D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        if answer == question.answer:
            print("Correct, Hooray!!\n") 
            self.score += 1
        else:
            print(f"Wrong, Come Tomorrow!!! The correct answer was {question.answer}\n")

    def display_score(self):
        print(f"You got {self.score} out of {len(self.questions)} questions correct.\n")

# Define the questions
questions = [
    Question("What is the capital of Lesotho?", ["A. Spain", "B. Morocco", "C. Berlin", "D. Maseru"], "D"),
    Question("Which language is primarily spoken in Lesotho?", ["A. Sepeli", "B. English", "C. Sesotho", "D. Maseru"], "C"),
    Question("What's the smallest prime number?", ["A. 1", "B. 2", "C. 3", "D. 5"], "B"),
    Question("Who wrote 'To Kill a Mockingbird'?", ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Thabo Lesholu"], "A"),
    Question("The most popular car brand in Lesotho is?", ["A. VW", "B. Honda", "C. Babus", "D. Toyota"], "D"),
]

# Run the quiz
quiz = Quiz(questions)
quiz.run()