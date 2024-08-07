import random
quiz_data = {
    "question1": {
        "question": "What is the name of the school that Harry Potter attends?\n",
        "options": ["A) Hogwarts School of Witchcraft and Wizardry","B) Beauxbatons Academy", "C) Durmstrang Institute", "D) Magic Academy"],
        "correct_answer": "A) Hogwarts School of Witchcraft and Wizardry"
    },
    "question2": {
        "question": "Who is Harry Potter's best friend?\n",
        "options": ["A) Neville Longbottom", "B) Luna Lovegood", "C) Ron Weasley", "D) Hermione Granger"],
        "correct_answer": "C) Ron Weasley"
    },
    "question3": {
        "question": "What is the name of the sport played on broomsticks in the Harry Potter series?\n",
        "options": ["A) Wizardball", "B) Broomball", "C) Quidditch", "D) Flying Football"],
        "correct_answer": "C) Quidditch"
    },
    "question4": {
        "question": "Who is the main antagonist in the Harry Potter series?\n",
        "options": ["A) The Dursleys","B) Draco Malfoy", "C) Professor Snape", "D) Lord Voldemort"],
        "correct_answer": "D) Lord Voldemort"
    },
    "question5": {
        "question": "What is the name of the magical train that takes students from Platform 9 3/4 to Hogwarts?\n",
        "options": ["A) The Hogwarts Express","B) The Wizard's Rail", "C) The Magic Choo-Choo", "D) The Flying Train"],
        "correct_answer": "A) The Hogwarts Express"
    },
    "question6": {
        "question": "Who is the headmaster of Hogwarts when Harry first attends?\n",
        "options": ["A) Severus Snape","B) Minerva McGonagall", "C) Rubeus Hagrid", "D) Albus Dumbledore"],
        "correct_answer": "D) Albus Dumbledore"
    },
    "question7": {
        "question": "What is the name of the Potions master who teaches Harry in his first year?\n",
        "options": ["A) Albus Dumbledore", "B) Minerva McGonagall", "C) Rubeus Hagrid", "D) Severus Snape"],
        "correct_answer": "D) Severus Snape"
    },
    "question8": {
        "question": "What is the name of the magical creature that is the guardian of the Philosopher's Stone?\n",
        "options": ["A) Fluffy","B) Norbert", "C) Buckbeak", "D) Fawkes"],
        "correct_answer": "A) Fluffy"
    },
    "question9": {
        "question": "Who helps Harry, Ron, and Hermione in their quest to prevent the return of Lord Voldemort?\n",
        "options": ["A) Remus Lupin", "B) Albus Dumbledore", "C) Severus Snape", "D) Sirius Black"],
        "correct_answer": "D) Sirius Black"
    },
    "question10": {
        "question": "What is the name of the wizarding village near Hogwarts?\n",
        "options": ["A) Diagon Alley", "B) Godric's Hollow", "C) Ottery St. Catchpole", "D) Hogsmeade"],
        "correct_answer": "D) Hogsmeade"
    }
}

def get_user_answer(question, options):
    while True:
        print(question)
        for option in options:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer.upper() in ["A", "B", "C", "D"]:
            return user_answer.upper()
        print("Invalid input.")

def quiz_game(num_questions):
    score = 0
    questions = random.sample(list(quiz_data.values()), num_questions)
    for i, question_data in enumerate(questions, start=1):
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"][0]
        user_answer = get_user_answer(question, options)
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"That's incorrect. The correct answer is {correct_answer}.")
        print(f"Current Score: {score} out of 5\n")
    print(f"\nQuiz finished! Your final score is {score} out of {num_questions}")
    
if __name__ == "__main__": 
    num_questions = 5 
    quiz_game(num_questions) 
    input("Press Enter to exit")