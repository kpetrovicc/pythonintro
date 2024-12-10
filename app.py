# import useful_tools as ut

# print(ut.roll_dice(10))

from Student import Student

student1 = Student("Jim", "Business", 3.4, True)
student2 = Student("Pam", "Art", 2.5, False)
print(student1.name + " is a " + student1.major + " major with a GPA of " + str(student1.gpa) + (" and is on probation: " if student1.is_on_probation else " is not on probation."))
print(student2.name + " is a " + student2.major + " major with a GPA of " + str(student2.gpa) + (" and is on probation: " if student2.is_on_probation else " is not on probation."))

print(student1.name +" "+ ("is" if student1.on_honor_roll() else "is not") + " on the honor roll.")
