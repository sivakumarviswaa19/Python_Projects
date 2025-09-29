class QuizBrain:
    global score


    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.score=0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        qn = self.question_list[self.question_number]
        self.question_number += 1

        ans=input(f"Q.{self.question_number}:{qn.question} (True/False):")

        if ans==qn.correct_answer:
            print("Correct answer")
            self.score +=1
            print(f"Total score : {self.score}")
        else:
            print("Wrong answer")
            print(f"Total score : {self.score}")







