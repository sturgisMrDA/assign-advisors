"""
Nick Stulsky, Owen Conlon, Marty Toenniessen

This function takes the input of an array of students and their name email etc. and uses
the student class created by another group to turn each student into an object and add the
objects to a dictionary which is outputted.

"""
#Global Variables
NAME_COLUMN = 0
EMAIL_COLUMN = 1
GRADE_COLUMN = 2
FIRST_CHOICE_COLUMN = 3
SECOND_CHOICE_COLUMN = 4
THIRD_CHOICE_COLUMN = 5
FOURTH_CHOICE_COLUMN = 6
SAME_ADVISORY_COLUMN = 7
NEW_TEACHER_COLUMN = 8
row = 0
column = 0

################################
#Function
def convert_array_to_object(array):
    #Turns the student into an object
    students = {}
    for row in array:
        student_obj = Student()
        student_obj.name = row[0] #Meant to take the name column from the thing the other group is doing if that is at all how this works
        student_obj.email = row[1]# ^ but with email
        student_obj.grade = row[2] # ^ but with grade
        student_obj.first_choice = row[3] # ^ but with first choice
        student_obj.second_choice = row[4] # ^ second choice
        student_obj.third_choice = row[5] # ^ third
        student_obj.fourth_choice = row[6] # ^ fourth
        student_obj.same_advisory = row[7] # ^ but with if they want to stay in the same advisory
        student_object.new_teacher = row[8] # ^ but if they are willing to have a new teacher
    
    #Add the Student name and stuff to the dictionary
        students[student_obj.email] = student_obj

        return students

def assignment(students):
  """
  Seth Coellner and Ben Slater
  This functin takes the sorted list and assigns students to their desired advisors
  the input is a list
  no outputs, the code manipulates global variables
  """

  amountOfStudents = len(students)#finds the total amount of students
  totalChoices = 4
  selectedAdvisor = 0 #the current advisor that the sudent wants
  while selectedAdvisor < totalChoices:
    currentStudent = 0 #the current student being assinged
    while currentStudent < amountOfStudents: 
      wantedAdvisor=[students[currentStudent].choices[selectedAdvisor]#sets the name of the advisor that the student wants for their current choice
      if students[currentStudent].grade == 12:#checks if the current student is a senior
        if len(advisors[wantedAdvisor].seniors) < MAX_SENIORS: #if there are less than the max seniors in the advisory
                     advisors[wantedAdvisor].seniors.insert(students[currentStudent].email) #put into list of students in the current advisor
                     assigned_students = assigned_students + students.pop(currentStudent) #pops the student from the list of all students, into the list of assigned students
      if students[currentStudent].grade == 11: #repeats for each grade
        if len(advisors[wantedAdvisor].juniors) < MAX_JUNIORS:
                     advisors[wantedAdvisor].juniors.insert(students[currentStudent].email)
                     assigned_students = assigned_students + students.pop(currentStudent)
      if students[currentStudent].grade == 10:
            if len(advisors[wantedAdvisor].sophomores) < MAX_SOPHOMORES:
                         advisors[wantedAdvisor].sophomores.insert(students[currentStudent].email)
                         assigned_students = assigned_students + students.pop(currentStudent)
      if students[currentStudent].grade == 9:
            if len(advisors[wantedAdvisor].freshmen) < MAX_FRESHMEN:
                         advisors[wantedAdvisor].freshmen.insert(students[currentStudent].email)
                         assigned_students = assigned_students + students.pop(currentStudent)
      currentStudent = currentStudent + 1
    selectedAdvisor += 1
                     
  return("finished")

"""
Tristan and Matt.
Check for anyone who has not filled the form.
"""
                     
big_list = [melon, lemon, watermelon, lime, coconut, orange, apple, cucumber, mango, strawberry, grape]
small_list = [melon, lemon, watermelon, lime, coconut]
bad_list = []

if big_list == small_list:
    print("Everyone has completed the form!")

else:
   for name in big_list:

        if name not in small_list:
            bad_list.append(name)

#output by student Mason, Jeanne and Paige.
def student_output():
    import csv
    assigned_students = students[].advisor
    email = assigned_students[]
    advisor_email = students[email].advisor
    import csv
    with open('studentlist.csv','w',newline=' ') as csvfile:
        studentwiter = csv,writer(csvfile,delimeter =' ',
                                  quotechar = "|", quoting = csv.QUOTE_MINIMAL)
        for student in students:
            studentwriter.writerow(student.name, student.email, student.advisor)
        for student in unresolved_students:
            studentwriter.writerow(unresolved_students.name, unresolved_students.email)
    return csvfile

#Eli and Dan
def sorting(students):
    copystu = dict(students)
    while i < len.copystu:
        if copystu[i].advisor == copystu[i].choices[0]:
            unassigned_students.append(copystu[i])
            del copystu[i]
        i = i + 1
        #Puts the students who chose thier previous advisor at first priority
    while i < len.copystu:
        if copystu[i].wants_new_advisor:
            unassiged_students.append(copystu[i])
            del copystu[i]
        i = i + 1
        #Sorts students who want new advisor into the list
    while i < len.copystu:
        if copystu[i].grade == 12:
            unassigned_students.append(copystu[i])
            del copystu[i]
        i = i + 1
        #Puts the Seniors as the third priority
    while i < len.copystu:
        if copystu[i].grade == 10 or 11:
            unassigned_students.append(copystu[i])
            del copystu[i]
        i = i + 1
        #Sorts through the choices of students grades 10-11, and sorts them accordingly
    while i < len.copystu:
        if copystu[i].grade == 9:
            unassigned_students.append(copystu[i])
            del copystu[i]
        i = i + 1
        #Has the freshmen as the last priority, and sorts them accordingly
    return unassigned_students

"""
Ethan and ...
output by advisor
"""
                     
import csv
with open('advisory.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    def advisor_list():
        fresh = 0
        soph = 0
        jun = 0
        sen = 0
        for ad_email in advisors:
            Advisor[ad_email].name = ad_name
            spamwriter.writerow([ad_name,'9th grade','10th grade','11th grade','12th grade','students'])
            for stud_email in students:
                if ad_email == Student[stud_email].advisor:
                    spamwriter.writerow([' ']*5 + [Student[stud_email].name])
                    if Student[stud_email].grade == 9:
                        fresh = fresh + 1
                    elif Student[stud_email].grade == 10:
                        soph = soph + 1
                    elif Student[stud_email].grade == 11:
                        jun = jun + 1
                    elif Student[stud_email].grade == 12:
                        sen = sen + 1
            spamwriter.writerow([' ', str(fresh), str(soph), str(jun), str(sen)])


