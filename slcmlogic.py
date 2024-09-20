tcc=int(input("Enter the total number of classes conducted: "))
tca=int(input("Enter the total number of classes attended: "))
tctbc=100
rc=int((75*tctbc)/100)
a=rc-tca #no of classes the student has to attend 
rem=tctbc-tcc #no of classes that can be conducted
if rem<a:
    print("You have attendence shortage!! contact your HOD")
elif rem>a:
    print("Your current attendance Percentage is",(tca/tcc)*100,"\n You can bunk",rem-a,"classes out of",rem,"classes")
elif a==rem:
    print("You have to attend all the classes in the remaining",rem,"classes to maintain 75% attendence")