#Database
ecestu={"name":["sanjay","pravin","muthu","vishal","rahul","kuppusamy","selvam","prem","babu","riyash"],"rollno":["ec11","ec12","ec13","ec14","ec15","ec16","ec17","ec18","ec19","ec20"]
,"cgpa":[7.8,7.6,8.0,7.1,7.4,7.7,8.6,8.0,8.1,8.9],"arrear":[0,0,0,1,0,1,1,0,0,0],"tscore":[93,70,82,78,86,80,70,62,88,96]}
csestu={"name":["ram","nathin","siva","shankar","rithish","ajith","vijay","singh","ranveer","sidhu"],"rollno":["cs01","cs02","cs03","cs04","cs05","cs06","cs07","cs08","cs09","cs10"]
,"cgpa":[7.7,8.6,8.0,8.1,9.4,6.7,8.6,7.0,6.1,9.0],"arrear":[0,0,0,0,0,0,0,0,1,0],"tscore":[93,80,92,88,93,75,64,92,74,84]}
eeestu={"name":["kannan","kavin","john","abi","bharani","tharun","kumar","ashok","siddharth","sabu"],"rollno":["ee31","ee32","ee33","ee34","ee35","ee36","ee37","ee38","ee39","ee40"]
,"cgpa":[6.8,8.6,9.0,8.1,6.4,7.7,9.6,6.0,6.1,8.4],"arrear":[1,1,0,0,0,0,2,0,1,0],"tscore":[75,64,92,74,84,93,80,92,88,93]}
mestu={"name":["vijay","naresh","mohan","chandhru","sethu","fahad","navin","amir","daniel","narayanan"],"rollno":["me21","me22","me23","me24","me25","me26","me27","me28","me29","me30"]
,"cgpa":[7.7,9.6,6.0,6.1,8.4,6.8,8.6,9.0,8.1,6.4],"arrear":[1,0,2,1,0,2,0,1,1,0],"tscore":[80,70,62,88,96,75,64,92,74,84]}
cestu={"name":["irfan","pranav","kishore","sabari","danish","nagesh","mugesh","kenny","rushil","kannan"],"rollno":["ce41","ce42","ce43","ce44","ce45","ce46","ce47","ce48","ce49","ce50"]
,"cgpa":[6.7,8.6,7.0,6.1,8.4,7.8,9.6,8.0,7.1,7.4],"arrear":[2,0,1,1,0,1,0,2,1,0],"tscore":[63,80,62,71,78,80,70,62,88,96]}
csesol={"solution":["no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution"]}
ecesol={"solution":["no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution"]}
eeesol={"solution":["no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution"]}
mesol={"solution":["no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution"]}
cesol={"solution":["no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution","no solution"]}
coname=["Pravin","Vignesh","Nirmal","asik","Sanjay"]                
codept=["Computer Science Engineering","Electronics and Communication Engineering","Electric and Electronical Engineering","Mechanical Engineering","Civil Engineering"]                 
coid=["pravin12","vignesh13","nirmal24","asik36","sanjay37"]                   
copass=["cse@1","ece@2","eee@3","me@4","ce@5"]
circularstucse=["No Latest Circular"]
circularstuece=["No Latest Circular"]
circularstueee=["No Latest Circular"]
circularstume=["No Latest Circular"]
circularstuce=["No Latest Circular"]
circularcocse=["No Latest Circular"]
circularcoece=["No Latest Circular"]
circularcoeee=["No Latest Circular"]
circularcome=["No Latest Circular"]
circularcoce=["No Latest Circular"]
csecir=["No Latest Circular"]
ececir=["No Latest Circular"]
eeecir=["No Latest Circular"]
mecir=["No Latest Circular"]
cecir=["No Latest Circular"]
problemstatement=["no problem statement"]
problemsolution=["no problem solution"]
impdate={1:["5    -   Wipro","15   -   Infosys","29   -   Hexaware"],2:["No Interview"],3:["4    -   Qualcomm","12   -   Techslot"],4:["22   -   Redchilli Entertainment","27   -   Techinfo Solutions"]
,5:["2    -   Tech Mahindra","14   -   Tata Consultancy","21   -   RP Labs","27   -   Paloalto Networks","29   -   Nvidia"],6:["12   -   Google","22   -   Microsoft","28   -   Apple"]
,7:["16   -   Meta","21   -   AWS"],8:["No Interview"],9:["11   -   Netflix","18   -   Bosch","27   -   BYJU\'"],10:["1    -   AMD"],11:["17   -   Hella solutions","26   -   KPR infotech","30   -   JetInfo"]
,12:["17   -   Samsung","23   -   Sony"]}
adminid="KPRADMIN"
adminpass="123456"

def cologin():
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome to Coordinator Login Page :")
    idin=input("\nEnter the Username :")
    passin=input("Enter the Password :")
    for i in range(len(coid)):
        for j in range (len(copass)):
            if coid[i]==idin and copass[i]==passin :
                return coordinatorhome(i)
    print ("\nWrong username or password !")
    return backco()


def coordinatorhome(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome Coordinator",coname[i],"of",codept[i],"!\n")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    if i==0 :
        print ("\nLatest Circular (From Admin) :\n")
        print(circularcocse[-1])
    elif i==1 :
        print ("\nLatest Circular (From Admin) :\n")
        print(circularcoece[-1])
    elif i==2 :
        print ("\nLatest Circular (From Admin) :\n")
        print(circularcoeee[-1])
    elif i==3 :
        print ("\nLatest Circular (From Admin) :\n")
        print(circularcome[-1])    
    elif i==4 :
        print ("\nLatest Circular (From Admin) :\n")
        print(circularcoce[-1])
    return cohome(i)
    


def cohome(i):    
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n\nSelect Option :\n \n1.Filter Students \n2.Update Training Score \n3.Update CGPA \n4.Update HOA \n5.Publish Circular \n6.Placement Calender \n7.Students List \n8.Solution Check \n9.Individual Student Detail \n10.Exit")
    ain=int(input("\nEnter Option :"))
    
    if ain==1:
        return filter(i)
    elif ain==2:
        return tscore(i)
    elif ain==3 :
        return cgpa(i)
    elif ain==4 :
        return hoa(i)
    elif ain==5:
        return cocircular(i)
    elif ain==6 :
        return cocalender(i)
    elif ain==7 :
        return studentlist(i)
    elif ain==8 :
        return solcheck(i)
    elif ain==9 :
        return indstu(i)
    elif ain==10:
        return homepage()
    elif ain!=1 and ain!=2 and ain!=3 and ain!=4 and ain!=5 and ain!=6 and ain!=7 and ain!=8 and ain!=9 and ain!=10:
        print("\nInvalid Option ! \n\nEnter Correct Option")
        return cohome(i)
   



def solcheck(i):
    if i==0:
        return solcheckcse(i)
    elif i==1:
        return solcheckece(i)
    elif i==2:
        return solcheckeee(i)
    elif i==3:
        return solcheckme(i)
    elif i==4:
        return solcheckce(i)


def solcheckcse(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    rin=input("\nEnter Roll No :")
    for j in range(len(csestu["rollno"])):
        if csestu['rollno'][j]==rin :
            print("\nLatest Problem Statement :\n")
            print(problemstatement[-1])
            print("\nActual Problem Solution :\n")
            print(problemsolution[-1],"\n")
            print(csestu['name'][j],"\'s Solution :\n")
            print(csesol["solution"][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return solcheckcse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    



def solcheckece(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    rin=input("\nEnter Roll No :")
    for j in range(len(ecestu["rollno"])):
        if ecestu['rollno'][j]==rin :
            print("\nLatest Problem Statement :\n")
            print(problemstatement[-1])
            print("\nActual Problem Solution :\n")
            print(problemsolution[-1],"\n")
            print(ecestu['name'][j],"\'s Solution :\n")
            print(ecesol["solution"][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return solcheckece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    


def solcheckeee(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    rin=input("\nEnter Roll No :")
    for j in range(len(eeestu["rollno"])):
        if eeestu['rollno'][j]==rin :
            print("\nLatest Problem Statement :\n")
            print(problemstatement[-1])
            print("\nActual Problem Solution :\n")
            print(problemsolution[-1],"\n")
            print(eeestu['name'][j],"\'s Solution :\n")
            print(eeesol["solution"][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return solcheckeee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    

def solcheckme(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    rin=input("\nEnter Roll No :")
    for j in range(len(mestu["rollno"])):
        if mestu['rollno'][j]==rin :
            print("\nLatest Problem Statement :\n")
            print(problemstatement[-1])
            print("\nActual Problem Solution :\n")
            print(problemsolution[-1],"\n")
            print(mestu['name'][j],"\'s Solution :\n")
            print(mesol["solution"][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return solcheckme(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)


def solcheckce(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    rin=input("\nEnter Roll No :")
    for j in range(len(cestu["rollno"])):
        if cestu['rollno'][j]==rin :
            print("\nLatest Problem Statement :\n")
            print(problemstatement[-1])
            print("\nActual Problem Solution :\n")
            print(problemsolution[-1],"\n")
            print(cestu['name'][j],"\'s Solution :\n")
            print(cesol["solution"][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return solcheckce(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    



def indstu(i):
    if i==0:
        return indstucse(i)
    elif i==1:
        return indstuece(i)
    elif i==2:
        return indstueee(i)
    elif i==3:
        return indstume(i)
    elif i==4:
        return indstuce(i)


def indstucse(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(csestu["rollno"])):
        if csestu['rollno'][j]==rin :
            print("\n"" Name :",csestu['name'][j],"\n","Roll no :",csestu['rollno'][j],"\n","CGPA :",csestu['cgpa'][j],"\n","History of Arrear :",csestu['arrear'][j]
                  ,"\n","Training Score :",csestu['tscore'][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return indstucse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    

def indstuece(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(ecestu["rollno"])):
        if ecestu['rollno'][j]==rin :
            print("\n"" Name :",ecestu['name'][j],"\n","Roll no :",ecestu['rollno'][j],"\n","CGPA :",ecestu['cgpa'][j],"\n","History of Arrear :",ecestu['arrear'][j]
                  ,"\n","Training Score :",ecestu['tscore'][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return indstuece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    

def indstueee(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(eeestu["rollno"])):
        if eeestu['rollno'][j]==rin :
            print("\n"" Name :",eeestu['name'][j],"\n","Roll no :",eeestu['rollno'][j],"\n","CGPA :",eeestu['cgpa'][j],"\n","History of Arrear :",eeestu['arrear'][j]
                  ,"\n","Training Score :",eeestu['tscore'][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return indstueee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)
    

def indstume(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(mestu["rollno"])):
        if mestu['rollno'][j]==rin :
            print("\n"" Name :",mestu['name'][j],"\n","Roll no :",mestu['rollno'][j],"\n","CGPA :",mestu['cgpa'][j],"\n","History of Arrear :",mestu['arrear'][j]
                  ,"\n","Training Score :",mestu['tscore'][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return indstume(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)


def indstuce(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(cestu["rollno"])):
        if cestu['rollno'][j]==rin :
            print("\n"" Name :",cestu['name'][j],"\n","Roll no :",cestu['rollno'][j],"\n","CGPA :",cestu['cgpa'][j],"\n","History of Arrear :",cestu['arrear'][j]
                  ,"\n","Training Score :",cestu['tscore'][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
         return indstuce(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
         return cohome(i)


def studentlist(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    if i==0 :
        print("\n")
        print("Students List :\n\n")
        print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
        print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
        for j in range(len(csestu["name"])):
          print(f"{j+1 : <10}{csestu['name'][j]:^10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
        print("\n")
        return cohome(i)
        
    elif i==1:
        print("\n")
        print("Students List :\n\n")
        print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
        print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
        for j in range(len(ecestu["name"])):
          print(f"{j+1 : <10}{ecestu['name'][j]:^10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
        print("\n")
        return cohome(i)

    elif i==2:
       print("\n")
       print("Students List :\n\n")
       print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
       print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
       for j in range(len(eeestu["name"])):
         print(f"{j+1 : <10}{eeestu['name'][j]:^10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
       print("\n")
       return cohome(i)
    
    elif i==3:
           print("\n")
           print("Students List :\n\n")
           print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
           print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
           for j in range(len(mestu["name"])):
             print(f"{j+1 : <10}{mestu['name'][j]:^10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
           print("\n")
           return cohome(i)
    elif i==4:
            print("\n")
            print("Students List :\n\n")
            print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
            print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
            for j in range(len(cestu["name"])):
              print(f"{j+1 : <10}{cestu['name'][j]:^10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
            print("\n")
            return cohome(i)




def filter(i):
    if i==0 :
        return stucse(i)
    elif i==1:
        return stuece(i)
    elif i==2:
       return stueee(i)
    elif i==3:
       return stume(i)
    elif i==4:
        return stuce(i)
    

def stuece(i) :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(ecestu["name"])):
        print(f"{j+1 : <10}{ecestu['name'][j]:^10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
    print("\n")
    return filterece(i)

def filterece(i):
    print("Enter Filter Details :")
    cgpa=float(input("\nMininmum CGPA Required :"))
    hoa=int(input("\nHistory of Arrear :"))
    tscore=int(input("\nMininum Training Score Required :"))
    print("Criteria Matched Students List :\n\n")
    print(f"{'NAME':<10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(ecestu["name"])):
        if ecestu["arrear"][j]<=hoa  and ecestu["cgpa"][j]>=cgpa and ecestu["tscore"][j]>=tscore :
           print(f"{ecestu['name'][j]:<10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return filterece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)
    


def stucse(i) :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(csestu["name"])):
        print(f"{j+1 : <10}{csestu['name'][j]:^10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
    print("\n")
    return filtercse(i)


def filtercse(i):
    print("Enter Filter Details :")
    cgpa=float(input("\nMininmum CGPA Required :"))
    hoa=int(input("\nHistory of Arrear :"))
    tscore=int(input("\nMininum Training Score Required :"))
    print("Criteria Matched Students List :\n\n")
    print(f"{'NAME':<10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(csestu["name"])):
        if csestu["arrear"][j]<=hoa  and csestu["cgpa"][j]>=cgpa and csestu["tscore"][j]>=tscore :
           print(f"{csestu['name'][j]:<10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return filtercse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def stueee(i) :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(eeestu["name"])):
        print(f"{j+1 : <10}{eeestu['name'][j]:^10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
    print("\n")
    return filtereee(i)

def filtereee(i):
    print("Enter Filter Details :")
    cgpa=float(input("\nMininmum CGPA Required :"))
    hoa=int(input("\nHistory of Arrear :"))
    tscore=int(input("\nMininum Training Score Required :"))
    print("Criteria Matched Students List :\n\n")
    print(f"{'NAME':<10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(eeestu["name"])):
        if eeestu["arrear"][j]<=hoa  and eeestu["cgpa"][j]>=cgpa and eeestu["tscore"][j]>=tscore :
           print(f"{eeestu['name'][j]:<10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return filtereee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def stume(i) :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(mestu["name"])):
        print(f"{j+1 : <10}{mestu['name'][j]:^10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
    print("\n")
    return filterme(i)

def filterme(i):
    print("Enter Filter Details :")
    cgpa=float(input("\nMininmum CGPA Required :"))
    hoa=int(input("\nHistory of Arrear :"))
    tscore=int(input("\nMininum Training Score Required :"))
    print("Criteria Matched Students List :\n\n")
    print(f"{'NAME':<10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(mestu["name"])):
        if mestu["arrear"][j]<=hoa  and mestu["cgpa"][j]>=cgpa and mestu["tscore"][j]>=tscore :
           print(f"{mestu['name'][j]:<10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return filterece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def stuce(i) :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(cestu["name"])):
        print(f"{j+1 : <10}{cestu['name'][j]:^10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
    print("\n")
    return filterce(i)

def filterce(i):
    print("Enter Filter Details :")
    cgpa=float(input("\nMininmum CGPA Required :"))
    hoa=int(input("\nHistory of Arrear :"))
    tscore=int(input("\nMininum Training Score Required :"))
    print("Criteria Matched Students List :\n\n")
    print(f"{'NAME':<10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(cestu["name"])):
        if cestu["arrear"][j]<=hoa  and cestu["cgpa"][j]>=cgpa and cestu["tscore"][j]>=tscore :
           print(f"{cestu['name'][j]:<10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return filterce(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def backco():
    p="\nWant to Retry or Back home !"
    p1=p.center(50)
    print(p1)
    b="\n1 . Retry Again \n2 . Back Home "
    b1=b.center(30)
    print(b1)
    opt1=int(input("\nEnter the Option : "))
    if opt1==1 :
       return cologin()
    elif opt1==2 :
        return homepage()



def tscore(i):
    if i==0 :
        return tscse(i)
    elif i==1:
        return tsece(i)
    elif i==2:
       return tseee(i)
    elif i==3:
       return tsme(i)
    elif i==4:
        return tsce(i)



def tscse(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(csestu["name"])):
        print(f"{j+1 : <10}{csestu['name'][j]:^10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
    return tscorecse(i)


def tscorecse(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(csestu["rollno"])):
        if csestu['rollno'][j]==rin :
            print("\n"" Name :",csestu['name'][j],"\n","Roll no :",csestu['rollno'][j],"\n","CGPA :",csestu['cgpa'][j],"\n","History of Arrear :",csestu['arrear'][j]
                  ,"\n","Training Score :",csestu['tscore'][j])
    tin=int(input("\nEnter New Training Score :"))
    for k in range(len(cestu["rollno"])):
        if csestu['rollno'][k]==rin :
           csestu['tscore'][k]=tin
    print ("\nTraining score changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return tscorecse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def tsece(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(ecestu["name"])):
        print(f"{j+1 : <10}{ecestu['name'][j]:^10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
    return tscoreece(i)


def tscoreece(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(ecestu["rollno"])):
        if ecestu['rollno'][j]==rin :
            print("\n"" Name :",ecestu['name'][j],"\n","Roll no :",ecestu['rollno'][j],"\n","CGPA :",ecestu['cgpa'][j],"\n","History of Arrear :",ecestu['arrear'][j]
                  ,"\n","Training Score :",ecestu['tscore'][j])
    tin=int(input("\nEnter New Training Score :"))
    for k in range(len(ecestu["rollno"])):
        if ecestu['rollno'][k]==rin :
           ecestu['tscore'][k]=tin
    print ("\nTraining score changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return tscoreece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)
 


def tseee(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(eeestu["name"])):
        print(f"{j+1 : <10}{eeestu['name'][j]:^10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
    return tscoreeee(i)


def tscoreeee(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(eeestu["rollno"])):
        if eeestu['rollno'][j]==rin :
            print("\n"" Name :",eeestu['name'][j],"\n","Roll no :",eeestu['rollno'][j],"\n","CGPA :",eeestu['cgpa'][j],"\n","History of Arrear :",eeestu['arrear'][j]
                  ,"\n","Training Score :",eeestu['tscore'][j])
    tin=int(input("\nEnter New Training Score :"))
    for k in range(len(eeestu["rollno"])):
        if eeestu['rollno'][k]==rin :
           eeestu['tscore'][k]=tin
    print ("\nTraining score changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return tscoreeee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def tsme(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(mestu["name"])):
        print(f"{j+1 : <10}{mestu['name'][j]:^10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
    return tscoreme(i)


def tscoreme(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(mestu["rollno"])):
        if mestu['rollno'][j]==rin :
            print("\n"" Name :",mestu['name'][j],"\n","Roll no :",mestu['rollno'][j],"\n","CGPA :",mestu['cgpa'][j],"\n","History of Arrear :",mestu['arrear'][j]
                  ,"\n","Training Score :",mestu['tscore'][j])
    tin=int(input("\nEnter New Training Score :"))
    for k in range(len(mestu["rollno"])):
        if mestu['rollno'][k]==rin :
           mestu['tscore'][k]=tin
    print ("\nTraining score changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return tscoreme(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def tsce(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(cestu["name"])):
        print(f"{j+1 : <10}{cestu['name'][j]:^10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
    return tscorece(i)


def tscorece(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(cestu["rollno"])):
        if cestu['rollno'][j]==rin :
            print("\n"" Name :",cestu['name'][j],"\n","Roll no :",cestu['rollno'][j],"\n","CGPA :",cestu['cgpa'][j],"\n","History of Arrear :",cestu['arrear'][j]
                  ,"\n","Training Score :",cestu['tscore'][j])
    tin=int(input("\nEnter New Training Score :"))
    for k in range(len(cestu["rollno"])):
        if cestu['rollno'][k]==rin :
           cestu['tscore'][k]=tin
    print ("\nTraining score changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return tscorece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def cgpa(i):
    if i==0 :
        return cgcse(i)
    elif i==1:
        return cgece(i)
    elif i==2:
       return cgeee(i)
    elif i==3:
       return cgme(i)
    elif i==4:
        return cgce(i)
    

def cgcse(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(csestu["name"])):
        print(f"{j+1 : <10}{csestu['name'][j]:^10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
    return cgpacse(i)


def cgpacse(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(csestu["rollno"])):
        if csestu['rollno'][j]==rin :
            print("\n"" Name :",csestu['name'][j],"\n","Roll no :",csestu['rollno'][j],"\n","CGPA :",csestu['cgpa'][j],"\n","History of Arrear :",csestu['arrear'][j]
                  ,"\n","Training Score :",csestu['tscore'][j])
    tin=float(input("\nEnter New CGPA :"))
    for k in range(len(cestu["rollno"])):
        if csestu['rollno'][k]==rin :
           csestu['cgpa'][k]=tin
    print ("\nCGPA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return cgpacse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def cgece(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(ecestu["name"])):
        print(f"{j+1 : <10}{ecestu['name'][j]:^10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
    return cgpaece(i)


def cgpaece(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(ecestu["rollno"])):
        if ecestu['rollno'][j]==rin :
            print("\n"" Name :",ecestu['name'][j],"\n","Roll no :",ecestu['rollno'][j],"\n","CGPA :",ecestu['cgpa'][j],"\n","History of Arrear :",ecestu['arrear'][j]
                  ,"\n","Training Score :",ecestu['tscore'][j])
    tin=float(input("\nEnter New CGPA :"))
    for k in range(len(ecestu["rollno"])):
        if ecestu['rollno'][k]==rin :
           ecestu['cgpa'][k]=tin
    print ("\nCGPA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return cgpaece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)
 


def cgeee(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(eeestu["name"])):
        print(f"{j+1 : <10}{eeestu['name'][j]:^10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
    return cgpaeee(i)


def cgpaeee(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(eeestu["rollno"])):
        if eeestu['rollno'][j]==rin :
            print("\n"" Name :",eeestu['name'][j],"\n","Roll no :",eeestu['rollno'][j],"\n","CGPA :",eeestu['cgpa'][j],"\n","History of Arrear :",eeestu['arrear'][j]
                  ,"\n","Training Score :",eeestu['tscore'][j])
    tin=float(input("\nEnter New CGPA :"))
    for k in range(len(eeestu["rollno"])):
        if eeestu['rollno'][k]==rin :
           eeestu['cgpa'][k]=tin
    print ("\nCGPA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return cgpaeee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def cgme(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(mestu["name"])):
        print(f"{j+1 : <10}{mestu['name'][j]:^10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
    return cgpame(i)


def cgpame(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(mestu["rollno"])):
        if mestu['rollno'][j]==rin :
            print("\n"" Name :",mestu['name'][j],"\n","Roll no :",mestu['rollno'][j],"\n","CGPA :",mestu['cgpa'][j],"\n","History of Arrear :",mestu['arrear'][j]
                  ,"\n","Training Score :",mestu['tscore'][j])
    tin=float(input("\nEnter New CGPA :"))
    for k in range(len(mestu["rollno"])):
        if mestu['rollno'][k]==rin :
           mestu['cgpa'][k]=tin
    print ("\nCGPA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return cgpame(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def cgce(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(cestu["name"])):
        print(f"{j+1 : <10}{cestu['name'][j]:^10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
    return cgpace(i)


def cgpace(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(cestu["rollno"])):
        if cestu['rollno'][j]==rin :
            print("\n"" Name :",cestu['name'][j],"\n","Roll no :",cestu['rollno'][j],"\n","CGPA :",cestu['cgpa'][j],"\n","History of Arrear :",cestu['arrear'][j]
                  ,"\n","Training Score :",cestu['tscore'][j])
    tin=float(input("\nEnter New CGPA :"))
    for k in range(len(cestu["rollno"])):
        if cestu['rollno'][k]==rin :
           cestu['cgpa'][k]=tin
    print ("\nCGPA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return cgpace(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def hoa(i):
    if i==0 :
        return acse(i)
    elif i==1:
        return aece(i)
    elif i==2:
       return aeee(i)
    elif i==3:
       return ame(i)
    elif i==4:
        return ace(i)


def acse(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(csestu["name"])):
        print(f"{j+1 : <10}{csestu['name'][j]:^10}{csestu['rollno'][j]:^10}{csestu['cgpa'][j]:^10}{csestu['arrear'][j]:^10}{csestu['tscore'][j]:>7}")
    return hoacse(i)


def hoacse(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(csestu["rollno"])):
        if csestu['rollno'][j]==rin :
            print("\n"" Name :",csestu['name'][j],"\n","Roll no :",csestu['rollno'][j],"\n","CGPA :",csestu['cgpa'][j],"\n","History of Arrear :",csestu['arrear'][j]
                  ,"\n","Training Score :",csestu['tscore'][j])
    tin=int(input("\nEnter New HOA :"))
    for k in range(len(cestu["rollno"])):
        if csestu['rollno'][k]==rin :
           csestu['arrear'][k]=tin
    print ("\nHOA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return hoacse(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def aece(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(ecestu["name"])):
        print(f"{j+1 : <10}{ecestu['name'][j]:^10}{ecestu['rollno'][j]:^10}{ecestu['cgpa'][j]:^10}{ecestu['arrear'][j]:^10}{ecestu['tscore'][j]:>7}")
    return hoaece(i)


def hoaece(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(ecestu["rollno"])):
        if ecestu['rollno'][j]==rin :
            print("\n"" Name :",ecestu['name'][j],"\n","Roll no :",ecestu['rollno'][j],"\n","CGPA :",ecestu['cgpa'][j],"\n","History of Arrear :",ecestu['arrear'][j]
                  ,"\n","Training Score :",ecestu['tscore'][j])
    tin=int(input("\nEnter New HOA :"))
    for k in range(len(ecestu["rollno"])):
        if ecestu['rollno'][k]==rin :
           ecestu['arrear'][k]=tin
    print ("\nHOA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return hoaece(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)
 


def aeee(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(eeestu["name"])):
        print(f"{j+1 : <10}{eeestu['name'][j]:^10}{eeestu['rollno'][j]:^10}{eeestu['cgpa'][j]:^10}{eeestu['arrear'][j]:^10}{eeestu['tscore'][j]:>7}")
    return hoaeee(i)


def hoaeee(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(eeestu["rollno"])):
        if eeestu['rollno'][j]==rin :
            print("\n"" Name :",eeestu['name'][j],"\n","Roll no :",eeestu['rollno'][j],"\n","CGPA :",eeestu['cgpa'][j],"\n","History of Arrear :",eeestu['arrear'][j]
                  ,"\n","Training Score :",eeestu['tscore'][j])
    tin=int(input("\nEnter New HOA :"))
    for k in range(len(eeestu["rollno"])):
        if eeestu['rollno'][k]==rin :
           eeestu['arrear'][k]=tin
    print ("\nHOA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return hoaeee(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def ame(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(mestu["name"])):
        print(f"{j+1 : <10}{mestu['name'][j]:^10}{mestu['rollno'][j]:^10}{mestu['cgpa'][j]:^10}{mestu['arrear'][j]:^10}{mestu['tscore'][j]:>7}")
    return hoame(i)


def hoame(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(mestu["rollno"])):
        if mestu['rollno'][j]==rin :
            print("\n"" Name :",mestu['name'][j],"\n","Roll no :",mestu['rollno'][j],"\n","CGPA :",mestu['cgpa'][j],"\n","History of Arrear :",mestu['arrear'][j]
                  ,"\n","Training Score :",mestu['tscore'][j])
    tin=int(input("\nEnter New HOA :"))
    for k in range(len(mestu["rollno"])):
        if mestu['rollno'][k]==rin :
           mestu['arrear'][k]=tin
    print ("\nHOA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return hoame(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)


def ace(i):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n")
    print("Students List :\n\n")
    print(f"{'S NO':<10}{'NAME':^10}{'ROLL NO':^10}{'CGPA':^10}{'HOA':^10}{'TRAINING SCORE':>7}")
    print(f"{'-------':<10}{'-------':^10}{'-------':^10}{'-------':^10}{'-------':^10}{'-----------------':>7}")
    for j in range(len(cestu["name"])):
        print(f"{j+1 : <10}{cestu['name'][j]:^10}{cestu['rollno'][j]:^10}{cestu['cgpa'][j]:^10}{cestu['arrear'][j]:^10}{cestu['tscore'][j]:>7}")
    return hoace(i)


def hoace(i):
    rin=input("\nEnter Roll No :")
    print("\nStudent Details :")
    for j in range(len(cestu["rollno"])):
        if cestu['rollno'][j]==rin :
            print("\n"" Name :",cestu['name'][j],"\n","Roll no :",cestu['rollno'][j],"\n","CGPA :",cestu['cgpa'][j],"\n","History of Arrear :",cestu['arrear'][j]
                  ,"\n","Training Score :",cestu['tscore'][j])
    tin=int(input("\nEnter New HOA :"))
    for k in range(len(cestu["rollno"])):
        if cestu['rollno'][k]==rin :
           cestu['arrear'][k]=tin
    print ("\nHOA changed Successfully !")
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return hoace(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)



def cocircular(i):
    if i==0 :
        return ccse(i)
    elif i==1:
        return cece(i)
    elif i==2:
       return ceee(i)
    elif i==3:
       return cme(i)
    elif i==4:
        return cce(i)


def ccse(i):
     x="\n-------------------------------------------------------------------------------------------------------"
     y=x.center(50)
     print(y)
     cir=input("\nEnter Circular to be Published :\n\n")
     return circse(cir,i)


def circse(cir,i):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option \n"))
    if ciropt==1:
        csecir.append(cir)
        print("\nCircular Published Successfully")
        return cohome(i)
    elif ciropt==2:
        return cohome(i)
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return circse(cir,i)
    

def cece(i):
     x="\n-------------------------------------------------------------------------------------------------------"
     y=x.center(50)
     print(y)
     cir=input("\nEnter Circular to be Published :\n\n")
     return cirece(cir,i)


def cirece(cir,i):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option \n"))
    if ciropt==1:
        ececir.append(cir)
        print("\nCircular Published Successfully")
        return cohome(i)
    elif ciropt==2:
        return cohome(i)
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return cirece(cir,i)


def ceee(i):
     x="\n-------------------------------------------------------------------------------------------------------"
     y=x.center(50)
     print(y)
     cir=input("\nEnter Circular to be Published :\n\n")
     return cireee(cir,i)


def cireee(cir,i):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option \n"))
    if ciropt==1:
        eeecir.append(cir)
        print("\nCircular Published Successfully")
        return cohome(i)
    elif ciropt==2:
        return cohome(i)
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return cireee(cir,i)



def cme(i):
     x="\n-------------------------------------------------------------------------------------------------------"
     y=x.center(50)
     print(y)
     cir=input("\nEnter Circular to be Published :\n\n")
     return cirme(cir,i)


def cirme(cir,i):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option \n"))
    if ciropt==1:
        mecir.append(cir)
        print("\nCircular Published Successfully")
        return cohome(i)
    elif ciropt==2:
        return cohome(i)
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return cirme(cir,i)



def cce(i):
     x="\n-------------------------------------------------------------------------------------------------------"
     y=x.center(50)
     print(y)
     cir=input("\nEnter Circular to be Published :\n\n")
     return circe(cir,i)


def circe(cir,i):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option \n"))
    if ciropt==1:
        cecir.append(cir)
        print("\nCircular Published Successfully")
        return cohome(i)
    elif ciropt==2:
        return cohome(i)
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return circe(cir,i)


def homepage():
    from datetime import date
    y=str(date.today())
    z=f"Date : {y}"
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\n",z.rjust(102))
    print("\nWelcome to Login Page : ")
    print("\n1.Admin login \n2.Coordinator Login \n3.Student Login")
    hin=str(input("\nEnter Option :"))
    if hin=="1" :
        adminlogin ()
    elif hin=="2" :
        cologin ()
    elif hin=="3":
        stulogin()
    elif hin!=1 and hin!=2 and hin!=3:
        print("\nInvalid Option ! \n\nEnter Correct Option")
        return homepage()
    

def adminlogin() :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome to Admin Login Page : ")
    adid=str(input("\nEnter The Username :"))
    adpass=str(input("Enter The Password :"))
    if adid==adminid and adpass==adminpass :
       return adminhome()
    elif adminid==adid :
        print("\nWrong Password !")
        return back()
    elif adpass==adminpass :
        print("\nWrong Username !")
        return back()
    elif adid!=adminid and adpass!=adminpass :
        print("\nWrong Username and Password !")
        return back()
    

def back():
    p="\nWant to Retry or Back home !"
    p1=p.center(50)
    print(p1)
    b="\n1 . Retry Again \n2 . Back Home "
    b1=b.center(30)
    print(b1)
    opt1=int(input("\nEnter the Option : "))
    if opt1==1 :
       return adminlogin()
    elif opt1==2 :
        return homepage()
    

def adminhome () :
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome Admin !")
    print("\nSelect Option :\n \n1.Publish Circular (Students) \n2.Publish Circular (Coordinator) \n3.Upload Problem Statement \n4.Upload Solution \n5.Placement Calender \n6.Exit")
    ain=int(input("\nEnter Option :"))
    if ain==1:
        return circularstu()
    elif ain==2:
        return circularcoord()
    elif ain==3 :
        return problem()
    elif ain==4 :
        return solution()
    elif ain==5 :
        return calender()
    elif ain==6 :
        return homepage()
    elif ain!=1 and ain!=2 and ain!=3 and ain!=4 and ain!=5 and ain!=6:
        print("\nInvalid Option ! \n\nEnter Correct Option")
        return adminhome()
    

def circularstu():
    cirstu=input("\nEnter Circular to be Published :\n")
    return cirstuhome(cirstu)
    

def cirstuhome(cirstu):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option : "))
    if ciropt==1:
        return publishstu(cirstu)
    elif ciropt==2:
        return adminhome()
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return cirstuhome(cirstu)


def publishstu(cirstu):
    print("\nSelect Department :")
    print("\n1.CSE \n2.ECE \n3.EEE \n4.ME \n5.CE \n6.ALL \n")
    seldept=input("Enter Department :")
    if seldept=="1" or seldept=="cse" or seldept=="CSE" :
        circularstucse[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="2" or seldept=="ece" or seldept=="ECE" :
        circularstuece[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="3" or seldept=="eee" or seldept=="EEE" :
        circularstueee[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="4" or seldept=="me" or seldept=="ME" :
        circularstume[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="5" or seldept=="ce" or seldept=="CE" :
        circularstuce[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="6" or seldept=="all" or seldept=="ALL" :
        circularstucse[-1]=cirstu
        circularstuece[-1]=cirstu
        circularstueee[-1]=cirstu
        circularstume[-1]=cirstu
        circularstuce[-1]=cirstu
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept!="1"  and seldept!="2" and seldept!="3" and seldept!="4" and seldept!="5" and seldept!="6" :
        print("\nSelect Correct Department !")
        return publishstu(cirstu)



def circularcoord():
    circo=input("\nEnter Circular to be Published :\n")
    return circohome(circo)

def circohome(circo):
    print("\n1.Publish Circular \n2.Cancel Publish\n")
    ciropt=int(input("Select Option :"))
    if ciropt==1:
        return publishco(circo)
    elif ciropt==2:
        return adminhome()
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return circohome(circo)


def publishco(circo):
    print("\nSelect Department :")
    print("\n1.CSE \n2.ECE \n3.EEE \n4.ME \n5.CE \n6.ALL \n")
    seldept=input("Enter Department :")
    if seldept=="1" or seldept=="cse" or seldept=="CSE" :
        circularcocse[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="2" or seldept=="ece" or seldept=="ECE" :
        circularcoece[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="3" or seldept=="eee" or seldept=="EEE" :
        circularcoeee[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="4" or seldept=="me" or seldept=="ME" :
        circularcome[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="5" or seldept=="ce" or seldept=="CE" :
        circularcoce[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept=="6" or seldept=="all" or seldept=="ALL" :
        circularcocse[-1]=circo
        circularcoece[-1]=circo
        circularcoeee[-1]=circo
        circularcome[-1]=circo
        circularcoce[-1]=circo
        print("\n Circular Published Successfully ! ")
        return adminhome()
    elif seldept!="1"  and seldept!="2" and seldept!="3" and seldept!="4" and seldept!="5" and seldept!="6" :
        print("\nSelect Correct Department !")
        return publishstu(circo)
    


def problem():
    prob=input("\nEnter the Problem Statement : \n")
    return probhome(prob)

def probhome(prob):
    print("\n1.Publish Problem \n2.Cancel Publish\n")
    ciropt=int(input("Select Option :"))
    if ciropt==1:
        return publishprob(prob)
    elif ciropt==2:
        return adminhome()
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return probhome(prob)


def publishprob(prob):
    problemstatement.append(prob)
    print("\n Problem Published Successfully ! ")
    return adminhome()
    


def solution():
    print("\nLatest Problem Statement :")
    print(problemstatement[-1])
    sol=input("\nEnter the Solution : \n")
    return solhome(sol)

def solhome(sol):
    print("\n1.Publish Solution \n2.Cancel Publish\n")
    ciropt=int(input("Select Option :"))
    if ciropt==1:
        return publishsol(sol)
    elif ciropt==2:
        return adminhome()
    elif ciropt!=1 and ciropt!=2:
        print("\nSelect Correct Option !\n")
        return solhome(sol)


def publishsol(sol):
    problemsolution.append(sol)
    print("\n Solution Published Successfully ! ")
    return adminhome()
    

def cocalender(i):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for j in range(len(impdate[month])):
     print(impdate[month][j])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return calender(i)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return cohome(i)

def calender():
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return calender()
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return adminhome()


def stulogin():
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome to Student Login Page : ")
    print("\nSelect Department :")
    print("\n1.CSE \n2.ECE \n3.EEE \n4.ME \n5.CE \n6.Exit")
    seldept=input("\nEnter Department :")
    if seldept=="1" or seldept=="cse" or seldept=="CSE" :
         x="\n-------------------------------------------------------------------------------------------------------"
         y=x.center(50)
         print(y)
         stuid=input("\nEnter the Username :")
         print("\nPassword = \"Name\"+\"RollNo\"")
         stupass=input("\nEnter the Password :")
         for k in range(len(csestu["name"])):
             if csestu["rollno"][k]==stuid and csestu["name"][k]+csestu["rollno"][k]==stupass :
                 return stucsehome(k)
         print("\nWrong Username or Password !")
         return stulogin()
    elif seldept=="2" or seldept=="ece" or seldept=="ECE" :
         x="\n-------------------------------------------------------------------------------------------------------"
         y=x.center(50)
         print(y)
         stuid=input("\nEnter the Username :")
         print("\nPassword = \"Name\"+\"RollNo\"")
         stupass=input("\nEnter the Password :")
         for k in range(len(ecestu["name"])):
             if ecestu["rollno"][k]==stuid and ecestu["name"][k]+ecestu["rollno"][k]==stupass :
                 return stuecehome(k)
         print("\nWrong Username or Password !")
         return stulogin()
    elif seldept=="3" or seldept=="eee" or seldept=="EEE" :
         x="\n-------------------------------------------------------------------------------------------------------"
         y=x.center(50)
         print(y)
         stuid=input("\nEnter the Username :")
         print("\nPassword = \"Name\"+\"RollNo\"")
         stupass=input("\nEnter the Password :")
         for k in range(len(eeestu["name"])):
             if eeestu["rollno"][k]==stuid and eeestu["name"][k]+eeestu["rollno"][k]==stupass :
                 return stueeehome(k)
         print("\nWrong Username or Password !")
         return stulogin()
    elif seldept=="4" or seldept=="me" or seldept=="ME" :
         x="\n-------------------------------------------------------------------------------------------------------"
         y=x.center(50)
         print(y)
         stuid=input("\nEnter the Username :")
         print("\nPassword = \"Name\"+\"RollNo\"")
         stupass=input("\nEnter the Password :")
         for k in range(len(mestu["name"])):
             if mestu["rollno"][k]==stuid and mestu["name"][k]+mestu["rollno"][k]==stupass :
                 return stumehome(k)
         print("\nWrong Username or Password !")
         return stulogin()
    elif seldept=="5" or seldept=="ce" or seldept=="CE" :
         x="\n-------------------------------------------------------------------------------------------------------"
         y=x.center(50)
         print(y)
         stuid=input("\nEnter the Username :")
         print("\nPassword = \"Name\"+\"RollNo\"")
         stupass=input("\nEnter the Password :")
         for k in range(len(cestu["name"])):
             if cestu["rollno"][k]==stuid and cestu["name"][k]+cestu["rollno"][k]==stupass :
                 return stucehome(k)
         print("\nWrong Username or Password !")
         return stulogin()
    elif seldept=="6" or seldept=="exit" or seldept=="Exit" :
        return homepage()
    
def stucsehome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome",csestu["name"][k],"of Computer Science Engineering !")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Circular (By Admin) :")
    print("\n",circularstucse[-1])
    print("\nLatest Circular (By Coordinator) :")
    print("\n",csecir[-1])
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    return stucsemenu(k)


def stucsemenu(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nMenu :")
    print("\n1.Personal Info \n2.Answer Problem Statement \n3.View solution \n4.Placement Calender \n5.Exit")
    stin=int(input("\nEnter option :"))
    if stin==1:
        return infocse(k)
    elif stin==2:
        return solcse(k)
    elif stin==3:
        return viewsolcse(k)
    elif stin==4:
        return stucalendercse(k)
    elif stin==5:
        return homepage()
    elif stin!=1 and stin!=2 and stin!=3 and stin!=4 and stin!=5:
        print("\nInvalid Option !")
        print("\nEnter Correct Option !")
        return stucsemenu(k)
    
    

def infocse(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPersonal Info :")
    print("\n"" Name :",csestu['name'][k],"\n","Roll no :",csestu['rollno'][k],"\n","CGPA :",csestu['cgpa'][k],"\n","History of Arrear :",csestu['arrear'][k]
                  ,"\n","Training Score :",csestu['tscore'][k])
    
    return stucsemenu(k)
    

def solcse(k):
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    sol=input("\nEnter the Solution :\n")
    csesol['solution'][k]=sol
    print("\nSolution Submitted Successfully")
    
    return stucsemenu(k)

def viewsolcse(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Problem Statement :\n")
    print(problemstatement[-1])
    print("\nLatest Problem Solution :\n")
    print(problemsolution[-1])
    return stucsemenu(k)

def stucalendercse(k):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return stucalendercse(k)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return stucsemenu(k)




def stuecehome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome",ecestu["name"][k],"of Electronics and Communication Engineering !")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Circular (By Admin) :")
    print("\n",circularstuece[-1])
    print("\nLatest Circular (By Coordinator) :")
    print("\n",ececir[-1])
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    return stuecemenu(k)





def stuecemenu(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nMenu :")
    print("\n1.Personal Info \n2.Answer problem solution \n3.View solution \n4.Placement Calender \n5.Exit")
    stin=int(input("\nEnter option :"))
    if stin==1:
        return infoece(k)
    elif stin==2:
        return solece(k)
    elif stin==3:
        return viewsolece(k)
    elif stin==4:
        return stucalenderece(k)
    elif stin==5:
        return homepage()
    elif stin!=1 and stin!=2 and stin!=3 and stin!=4 and stin!=5:
        print("\nInvalid Option !")
        print("\nEnter Correct Option !")
        return stuecemenu(k)
    

def infoece(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPersonal Info :")
    print("\n"" Name :",ecestu['name'][k],"\n","Roll no :",ecestu['rollno'][k],"\n","CGPA :",ecestu['cgpa'][k],"\n","History of Arrear :",ecestu['arrear'][k]
                  ,"\n","Training Score :",ecestu['tscore'][k])
    
    return stuecemenu(k)
    

def solece(k):
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    sol=input("\nEnter the Solution :\n")
    ecesol['solution'][k]=sol
    print("\nSolution Submitted Successfully")
    
    return stuecemenu(k)


def viewsolece(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Problem Statement :\n")
    print(problemstatement[-1])
    print("\nLatest Problem Solution :\n")
    print(problemsolution[-1])
    return stuecemenu(k)

def stucalenderece(k):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return stucalenderece(k)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return stuecemenu(k)


def stueeehome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome",eeestu["name"][k],"of Electric and Electronical Engineering !")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Circular (By Admin) :")
    print("\n",circularstuece[-1])
    print("\nLatest Circular (By Coordinator) :")
    print("\n",eeecir[-1])
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    return stueeemenu(k)


def stueeemenu(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nMenu :")
    print("\n1.Personal Info \n2.Answer problem solution \n3.View solution \n4.Placement Calender \n5.Exit")
    stin=int(input("\nEnter option :"))
    if stin==1:
        return infoeee(k)
    elif stin==2:
        return soleee(k)
    elif stin==3:
        return viewsoleee(k)
    elif stin==4:
        return stucalendereee(k)
    elif stin==5:
        return homepage()
    elif stin!=1 and stin!=2 and stin!=3 and stin!=4 and stin!=5:
        print("\nInvalid Option !")
        print("\nEnter Correct Option !")
        return stueeemenu(k)
    

def infoeee(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPersonal Info :")
    print("\n"" Name :",eeestu['name'][k],"\n","Roll no :",eeestu['rollno'][k],"\n","CGPA :",eeestu['cgpa'][k],"\n","History of Arrear :",eeestu['arrear'][k]
                  ,"\n","Training Score :",eeestu['tscore'][k])
    
    return stueeemenu(k)
    

def soleee(k):
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    sol=input("\nEnter the Solution :\n")
    eeesol['solution'][k]=sol
    print("\nSolution Submitted Successfully")
    
    return stueeemenu(k)


def viewsoleee(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Problem Statement :\n")
    print(problemstatement[-1])
    print("\nLatest Problem Solution :\n")
    print(problemsolution[-1])
    return stueeemenu(k)

def stucalendereee(k):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return stucalendereee(k)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return stueeemenu(k)




def stumehome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome",mestu["name"][k],"of Mechanical Engineering !")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Circular (By Admin) :")
    print("\n",circularstuece[-1])
    print("\nLatest Circular (By Coordinator) :")
    print("\n",mecir[-1])
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    return stumemenu(k)


def stumemenu(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nMenu :")
    print("\n1.Personal Info \n2.Answer problem solution \n3.View solution \n4.Placement Calender \n5.Exit")
    stin=int(input("\nEnter option :"))
    if stin==1:
        return infome(k)
    elif stin==2:
        return solme(k)
    elif stin==3:
        return viewsolme(k)
    elif stin==4:
        return stucalenderme(k)
    elif stin==5:
        return homepage()
    elif stin!=1 and stin!=2 and stin!=3 and stin!=4 and stin!=5:
        print("\nInvalid Option !")
        print("\nEnter Correct Option !")
        return stumemenu(k)
    

def infome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPersonal Info :")
    print("\n"" Name :",mestu['name'][k],"\n","Roll no :",mestu['rollno'][k],"\n","CGPA :",mestu['cgpa'][k],"\n","History of Arrear :",mestu['arrear'][k]
                  ,"\n","Training Score :",mestu['tscore'][k])
    
    return stumemenu(k)
    

def solme(k):
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    sol=input("\nEnter the Solution :\n")
    mesol['solution'][k]=sol
    print("\nSolution Submitted Successfully")
    
    return stumemenu(k)

def viewsolme(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Problem Statement :\n")
    print(problemstatement[-1])
    print("\nLatest Problem Solution :\n")
    print(problemsolution[-1])
    return stumemenu(k)

def stucalenderme(k):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return stucalenderme(k)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return stumemenu(k)

def stucehome(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nWelcome",cestu["name"][k],"of Civil Engineering !")
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Circular (By Admin) :")
    print("\n",circularstuece[-1])
    print("\nLatest Circular (By Coordinator) :")
    print("\n",cecir[-1])
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    return stucemenu(k)


def stucemenu(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nMenu :")
    print("\n1.Personal Info \n2.Answer problem solution \n3.View solution \n4.Placement Calender \n5.Exit")
    stin=int(input("\nEnter option :"))
    if stin==1:
        return infoce(k)
    elif stin==2:
        return solce(k)
    elif stin==3:
        return viewsolce(k)
    elif stin==4:
        return stucalenderce(k)
    elif stin==5:
        return homepage()
    elif stin!=1 and stin!=2 and stin!=3 and stin!=4 and stin!=5:
        print("\nInvalid Option !")
        print("\nEnter Correct Option !")
        return stucemenu(k)
    

def infoce(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPersonal Info :")
    print("\n"" Name :",cestu['name'][k],"\n","Roll no :",cestu['rollno'][k],"\n","CGPA :",cestu['cgpa'][k],"\n","History of Arrear :",cestu['arrear'][k]
                  ,"\n","Training Score :",cestu['tscore'][k])
    
    return stucemenu(k)
    

def solce(k):
    print("\nLatest Problem Statement :")
    print("\n",problemstatement[-1])
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    sol=input("\nEnter the Solution :\n")
    cesol['solution'][k]=sol
    print("\nSolution Submitted Successfully")
    
    return stucemenu(k)

def viewsolce(k):
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nLatest Problem Statement :\n")
    print(problemstatement[-1])
    print("\nLatest Problem Solution :\n")
    print(problemsolution[-1])
    return stucemenu(k)

def stucalenderce(k):
    import calendar as cal
    x="\n-------------------------------------------------------------------------------------------------------"
    y=x.center(50)
    print(y)
    print("\nPlacement Calender ! ")
    year=2024
    month=int(input("\nPlease Enter The Month :"))
    print("\n",cal.month(year,month))
    print(f"{'Date':<10}{'Company':^1}")
    print(f"{'-----':<10}{'-------':^1}")
    for i in range(len(impdate[month])):
     print(impdate[month][i])
    con=input("\nDo You Want to Continue (Yes/No) :")
    if con=="Yes" or con=="yes" or con=="y" or con=="Y":
        return stucalenderce(k)
    elif con=="No" or con=="no" or con=="n" or con=="N":
        return stucemenu(k)


q="\n\n\t\t------------     Welcome To Placement Management System     ------------\n"
home=q.center(50)
print(home)
homepage()
