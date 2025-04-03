questions = [
    {
        "prompt": "What is the capital of Lesotho?",
        "options": ["A. Spain", "B. Morocco", "C. Berlin", "D. Maseru"],
        "answer": "D"
    },
    {
        "prompt": "Which language is primarily spoken in Lesotho?",
        "options": ["A. Sepeli", "B. English", "C. Sesotho", "D. Maseru"],
        "answer": "C"
    },
    {
        "prompt": "What's the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B" 
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Thabo Lesholu"],
        "answer": "A"
    },
    {
        "prompt": "The most popular car brand in Lesotho is?",
        "options": ["A. VW", "B. Honda", "C. Babus", "D. Toyota"],
        "answer": "D"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        
        while True:
            answer = input("Enter your answer (A, B, C, D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct, Hooray!!\n") 
            score += 1
        else:
            print(f"Wrong, Come Tomorrow!!! The correct answer was {question['answer']}\n")

    print(f"You got {score} out of {len(questions)} questions correct.\n")

run_quiz(questions)