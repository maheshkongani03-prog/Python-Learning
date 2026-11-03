class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer
        self.dict={
            "text1":q_text,
            "answer1":q_answer
        }
        #print(f"1st: {self.text}")

#new_q=Question("Name","True")
#print(new_q.answer)
        