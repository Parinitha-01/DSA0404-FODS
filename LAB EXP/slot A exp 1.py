import numpy as np

student_scores = np.array([
    [85, 78, 92, 88],
    [90, 82, 85, 91],
    [76, 89, 88, 80],
    [95, 91, 94, 87]
])

subjects = ["Math", "Science", "English", "History"]

averages = np.mean(student_scores, axis=0)

print("Average scores:")

for i in range(4):
    print(subjects[i], ":", averages[i])

highest = np.argmax(averages)

print("\nSubject with highest average:", subjects[highest])
print("Highest average score:", averages[highest])
