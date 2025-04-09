from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [Question(question['text'], question['answer']) for question in question_data]


quiz = QuizBrain(question_bank)


while True:
    if not quiz.still_has_questions():
        print("You have completed the quiz")
        print(f"Your final score: {quiz.score}/{len(question_bank)}")
        exit("Quiz finished!")

    quiz.next_question()
