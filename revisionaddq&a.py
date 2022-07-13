import sqlite3, pygame, _impfuncs as _
beingannoying=True

conn = sqlite3.connect("Python/Revision/revision.db")
cursorObj = conn.cursor()

subjects = [subject[0] for subject in cursorObj.execute("SELECT SUBJECT FROM SUBJECTS")]

[print(str(i+1)+". ",subjects[i]) for i in range(0,len(subjects))]

def adding():
    print('Question: '); q = input()
    while _.ques(f'Is {q} your question?\n1. Yes \n   or \n2. No',1,2) == 2:
        print('Question: '); q= input()
    print('Answer: '); a = input()
    while _.ques(f'Is {a} your answer?\n1. Yes \n   or \n2. No',1,2) == 2:
        print('Answer: '); a = input()
    IDnum = len([cursorObj.execute(f"SELECT ID FROM {subjects[choice-1]}")])
    conn.execute(f"INSERT INTO {subjects[choice-1]} (ID, QUESTION, Answer) \
         VALUES ('{IDnum}','{q}','{a}')")

def editing():
    global choice
    questions =[question[0] for question in cursorObj.execute(f"SELECT QUESTION FROM {subjects[choice-1]}")]
    answers = [answer[0] for answer in cursorObj.execute(f"SELECT Answer FROM {subjects[choice-1]}")]
    [[_.ques(f'{questions[i]}\n{answers[i]}\nDo you want to edit this?\n1. Yes\n2. No/Next\n3. Quit',1,3)] for i in range(0,len(questions))]
    def edit():

choice = _.ques('Which one do you want to edit?',1,len(subjects))

aore= _.ques('Do you want to \n1. add \n   or \n2. edit?',1,2)
if aore == 1: adding()
if aore == 2: editing()

conn.commit()
conn.close()


    

