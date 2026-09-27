name = input("Enter your name: ")

maths = int(input("Enter Maths marks: "))
chemistry = int(input("Enter Chemistry marks: "))
python = int(input("Enter Python marks: "))
ece = int(input("Enter ECE marks: "))
ai = int(input("Enter AI marks: "))

total = maths + chemistry + python + ece + ai

print("Total marks =", total)

average = total / 5

print("Average marks =", average)

percentage = (total / 500) * 100

print("Percentage =", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade =", grade)
print("\n--- STUDENT RESULT ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)
