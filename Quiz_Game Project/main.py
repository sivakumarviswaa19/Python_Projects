from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for i in question_data:
    q=i["question"]
    a=i["correct_answer"]
    Qn=Question(q,a)
    question_bank.append(Qn)

QN=QuizBrain(question_bank)


while QN.still_has_questions():
    QN.next_question()


