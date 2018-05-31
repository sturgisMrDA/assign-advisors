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
