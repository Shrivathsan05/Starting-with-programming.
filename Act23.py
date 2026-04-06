#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
#Take input for the student wheter he can take the exam or not.
MedicalCause = input ( "Did you heve a Medical Cause? (Y/N): " ) . strip ( ) . upper ( )
if MedicalCause == "Y" :
    print ( "YOU ARE ALLOWED!" )
else : 
    Attendance = int ( input ( "Enter the attendance of the student: " ) )
    if Attendance >= 75 : 
        print ( "ALLOWED!" )
    else : 
        print ( "NOT ALLOWED!" )

