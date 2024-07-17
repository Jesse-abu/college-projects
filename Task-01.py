val = list()
while len(val) != 3:
    sub = input('Course Name: ')
    score = input('Grade: ')
    g_score = eval(score) if score.isnumeric() else print('Error: Enter a numeric value') 
    val.append((sub, g_score))
file = {course: grade for course, grade in val}
average_score = sum([file[course] for course in file])/len(val)
highest_score = max(file, key=file.get)
lowest_score = min(file, key=file.get)
print(f'Average Score = {average_score}\nHighest Score = {highest_score}:{file[highest_score]}\nLowest Score = {lowest_score}:{file[lowest_score]}' )