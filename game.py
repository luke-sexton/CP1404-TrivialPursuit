file_open = open("Questions.txt", "r")

questions = []

for line in file_open:
    question = line.strip("\n").split(",")
    questions.append(question)

print(questions)

file_open.close()