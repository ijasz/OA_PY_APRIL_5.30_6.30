s1 = int(input("Enter mark for physics:"))
s2 = int(input("Enter mark for Chemistry:"))
s3 = int(input("Enter mark for Biology:"))
s4 = int(input("Enter mark for Maths:"))
s5 = int(input("Enter mark for Computer:"))
Total = s1+s2+s3+s4+s5
per = Total/5
if (per >= 90):
    print("Grade = A+")
elif (per >= 80):
    print("Grade = A")
elif (per >= 70):
    print("Grade = B")
elif (per >= 60):
    print("Grade = C")
elif (per >= 50):
    print("Grade = D")
elif (per >= 40):
    print("Grade = E")
else:
    print("Grade = F")
