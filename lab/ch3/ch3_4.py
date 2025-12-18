emp = ["\"\"","\'\'"]

def add_score(duck, student, subject, score):
	if '.' in score:
		score = float(score)
	else:
		score = int(score)
	if score < 0:
		raise Exception
	if not (student in duck):
		duck[student] = {}
	duck[student][subject.strip("'")] = score
      
def calc_average_score(duck):
	avg_score = {}
	for student, student_score in duck.items():
		if str(student).isnumeric() == False:
			raise Exception
		avg = 0
		student_score = dict(student_score)
		for subj, score in student_score.items():
			avg += score
		avg /= len(student_score)
		avg_score[student] = f"{avg:.2f}"
	return avg_score


try:
    user_input = input("Input : ").strip()
    user_input = user_input.split('|')
    user_input = [x.strip() for x in user_input]
    subject_score = user_input[0]
    user_input = user_input[1::]
    subject_score = dict(eval(subject_score))
    if (len(user_input) % 3 != 0):
        raise Exception
    for i in range(2, len(user_input), 3):
        student = user_input[i - 2]
        subject = user_input[i - 1]
        score = user_input[i]
        if (student in emp) or (subject in emp) or (score in emp) or (student.isdigit() == False):
            raise Exception
        add_score(subject_score, student, subject, score)
    avg = calc_average_score(subject_score)
    print(f"{subject_score}, Average score: {avg}")
except:
    print("Invalid")