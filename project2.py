
def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

average = calculate_average(marks)

print("Average:", round(average, 2))
print("Grade:", calculate_grade(average))
