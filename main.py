from question_model import *
from data import *
from quiz_brain import *

question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz")
print(f"your final Score was : {quiz.score}/{len(question_bank)}")