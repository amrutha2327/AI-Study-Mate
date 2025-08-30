import random
import time

# Simple database of subjects and topics
subjects = {
    'Math': ['Algebra', 'Geometry', 'Calculus'],
    'Science': ['Physics', 'Chemistry', 'Biology'],
    'History': ['Ancient Civilizations', 'World Wars', 'American History']
}

# A basic set of quiz questions (for demo purposes)
quiz_data = {
    'Math': {
        'Algebra': [
            {"question": "What is the solution to x + 5 = 12?", "answer": "7"},
            {"question": "What is the value of x in 2x = 10?", "answer": "5"}
        ],
        'Geometry': [
            {"question": "What is the area of a circle with radius 7?", "answer": "153.94"},
            {"question": "What is the perimeter of a square with side 4?", "answer": "16"}
        ]
    },
    'Science': {
        'Physics': [
            {"question": "What is the speed of light?", "answer": "299,792,458 m/s"},
            {"question": "What is the formula for force?", "answer": "F = ma"}
        ],
        'Chemistry': [
            {"question": "What is the atomic number of Carbon?", "answer": "6"},
            {"question": "What is the chemical formula for water?", "answer": "H2O"}
        ]
    }
}

# AI Study Mate Functions
def greet_user():
    print("Hello! I'm your AI Study Mate.")
    time.sleep(1)
    print("I can help you study by providing quiz questions and explanations.")
    time.sleep(1)

def get_subject():
    while True:
        print("\nHere are some subjects I can help you with:")
        for i, subject in enumerate(subjects.keys(), 1):
            print(f"{i}. {subject}")
        try:
            choice = int(input("Which subject would you like to study? Enter the number: "))
            if 1 <= choice <= len(subjects):
                selected_subject = list(subjects.keys())[choice - 1]
                return selected_subject
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_topic(subject):
    while True:
        print(f"\nGreat! Here are some topics under {subject}:")
        for i, topic in enumerate(subjects[subject], 1):
            print(f"{i}. {topic}")
        try:
            choice = int(input("Which topic would you like to focus on? Enter the number: "))
            if 1 <= choice <= len(subjects[subject]):
                selected_topic = subjects[subject][choice - 1]
                return selected_topic
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_quiz_question(subject, topic):
    print("\nStarting quiz...\n")
    # Check if the subject and topic exist in quiz_data before accessing
    if subject in quiz_data and topic in quiz_data[subject]:
        questions = quiz_data[subject][topic]
        if questions:
            question = random.choice(questions)
            user_answer = input(question["question"] + " ")
            if user_answer.strip().lower() == question["answer"].lower():
                print("Correct! Well done.")
            else:
                print(f"Oops! The correct answer is {question['answer']}.")
        else:
            print(f"No quiz questions available for {topic} in {subject}.")
    else:
        print(f"No quiz data available for {topic} in {subject}.")


def study_session():
    greet_user()

    subject = get_subject()
    topic = get_topic(subject)

    print(f"\nYou selected {topic} under {subject}. Let’s begin your study session.")
    time.sleep(1)

    ask_quiz_question(subject, topic)

def main():
    while True:
        study_session()
        cont = input("\nDo you want to study another topic? (yes/no): ")
        if cont.lower() != 'yes':
            print("Thanks for studying with me! Goodbye!")
            break

if __name__ == "__main__":
    main()