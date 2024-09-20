tcc=int(input("Enter the no. of classes conducted:")) #tcc=total classes conducted
tca=int(input("Enter the no. of classes attended:")) #tca=total classes attended
if tca>tcc:
    print("Invalid input. Classes attended cannot be greater than classes conducted")
    exit()
tctbc=100 #total classes to be conducted
rc=(75*tctbc)/100 #required classes to maintain 75% attendence
a=rc-tca #no of classes the student has to attend 
rem=tctbc-tcc #no of classes that can be conducted
if tcc==tca==0:
    print("Your Current Attendence Percentage: 0")
else:
    print("Your Current Attendence Percentage:",round((tca/tcc)*100,2))
    if rem<a:
        print("You have attendence shortage!! contact your HOD")
    elif rem>a:
        print("You can afford to take leaves for",int(rem-a),"classes out of",rem,"classes")
    elif a==rem:
        print("You have to attend all the classes in the remaining",rem,"classes to maintain 75% attendence")