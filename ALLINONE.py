def multipy():
    x = int(input("Enter the first number:  "))
    y = int(input("Enter the second number: "))
    z = x*y
    print(f"The product of both the numbers is : {z}")
    
def division():
    a = int(input("Enter the Divisor:  "))
    b = int(input("Enter the dividend: "))
    c = a/b
    print(f"The quotient is : {c}")
    
def bmi():
    d = float(input("Enter your weight in Kilograms : "))
    e = float(input("Enter your height in meters    : "))
    f = d/(e**2)
    print(f"Your calculated Body Mass index is : {f}")
    if f<18.5:
        print("You're slightly underweight to be fit you need a few pound to you weight, just a suggestion")
    elif 18.5<f<24.9:
        print("your Body Mass Index is in the healthy range , keep exercising , be fit! :-) ")
    elif f>24.9:
        print("You're overweight as per your Body Mass index")
        
def mtofeet():
    g = float(input("Enter the length in meters : "))
    h = g*3.28
    print(f"The entered length in feets will be : {h}")
    
    
def kgtopound():
    k = float(input("Enter the weight in kgs : "))
    l = k*2.20
    print(f"The enterd weight in pounds will be : {l}")
    

def calorie():    
    q = str(input("If you are a woman press 'w' if you're a man press 'm' :"))
    if q=="w":
        o = float(input("Enter your body weight in kgs : "))
        p = float(input("Enter your height in cm       : "))
        r = float(input("Enter your age in years       : "))
        s = (10*o)+(6.25*p)-(5*r)-161
        print(f"Your maintainance calories are around : {s},")
         

        
    elif q=="m":
        t = float(input("Enter your body weight in kgs : "))
        u = float(input("Enter your height in cm       : "))
        v = float(input("Enter your age in years       : "))
        w = (10*t)+(6.25*u)-(5*v)+5
        print(f"Your maintainance calories are around : {w}")
        
def compint():
    a1 = float(input("Enter the amount of principal amount                            : "))
    b1 = float(input("Enter the time in years                                         : "))
    c1 = float(input("Enter the percentage of interest also known as rate of interest : "))
    d1 = (a1*b1*c1)/100
    print(f"The compound interest will be: {d1}")     

def avgmks():
    e1 = int(input("Enter the number of subjects       : "))
    i=1
    h1=0
    while i<=e1:
        f1 = float(input("Enter the obtained marks in the subject                                  : "))
        f2 = 0
        f2 = f2 + f1
        g1 = float(input("Enter the maximum marks that can be obtained in that subject             : "))
        g2 = 0
        g2 = g2 + g1
        i=i+1
    h1 = (f2/g2)*100
        
    print(f"The percentage obtained in the examinations is {h1}%")
    if h1<70:
        print("Thats quite low for a student like you , work harder")
    elif 70<h1<90:
        print("Thats a good percentage , keep up")
    elif h1>90:
        print("WELL DONE!! Thats an impressive result")
        
def rupee_to_doll():
    x = str(input("If you want to add the current value of dollars then press \"c\" if not then press \"n\" "))
    print("If you don't write the current value our servers will take 1 USD as 81 INR")
    if x=="c":
        cur_doll = float(input("Enter the current price of dollars in rupees        : "))
        amt_rupe = float(input("Enter the amount of money you want to convert       : "))
        tot = cur_doll*amt_rupe
        print(f"The entered amount in rupees will be                               : {tot}")
    elif x=="n":
        amt = float(input("Enter the amount in rupees you want to convert           : "))
        phil = amt*81
        print(f"The entered amount in rupees will be                                : {phil}")
        
def kinematics():
    print("Kinematics is a branch of classical mechanics that deals with motion without considering the cause of the force")
    print("There are numerous types of problems that are present in kinematics")
    print("Don't worry we'll try our best to solve most of them which can be simple solved, below given are the types of questions")
    que_typ = str(input(" Free fall \t\t\t\t\t\t\t\t\t\t\t\t press\"F\" \n Time taken by Moving objects with constant accelaration to reach the destination \t\t\t press\"M\"\n  "))
    if que_typ=="F":
        print("This part will cover the part where an object is dropped from a height \"h\" , \nWith acceleration due to gravity being \"g\" = 9.8 ,\nInitial velocity will be taken as zero ,\nThe air resistance will be taken as negligible ")
        h = float(input("\n\nEnter the value of h                                   : "))
        vf = 2*9.8*h
        fv = vf**(1/2)
        print(f"\n\nTHE FINAL VELOCITY OF THE OBJECT BEFORE TOUCHING THE GROUND WILL BE {fv}")
    elif que_typ=="M":
        print("   This part will cover the problem related to a moving object")
        print("   In the case of constant accelaration we solve the question for time taken to cover a distance")
        ini = float(input("Enter the value of initial velocity of the object (in met/sec)                          : "))
        acc = float(input("Enter the value of constant accelaration thatthe object is experiencing (in met/sec^2)  : "))
        dis = float(input("Enter the value of the distance upto whichthe object will move (in meters)              : "))
        tim = (((2*dis)/(acc))-(ini/acc))**(1/2)
        print(f"\n\nThe time taken to cover that distance with a constant accelaration will be : {tim} seconds")
    print("We'll add more questions with time please suggest us different types of questions to help us improve and be more efficient")
    

        

print("         ______________________________________________________________________")
print("          WELCOME TO THE SPECIAL CALCULATOR WHICH CALCULATES ALMOST EVERYTHING")
print("To Get Started Select Anything You Want To Use our Service For")
print("To multiply two numbers.............................................select \"A\" ")
print("To divide two numbers...............................................select \"B\" ")
print("To calculate your BMI...............................................select \"C\" ")
print("To convert meter into feet..........................................select \"D\" ")
print("To convert kg into pound............................................select \"E\" ")
print("To calculate your maintainance calories.............................select \"F\" ")
print("To calculate compound interest......................................select \"G\" ")
print("To calculate average marks..........................................select \"H\" ")
print("To convert rupees into dollar.......................................select \"I\" ")
print("To solve problems related to kinematics.............................select \"J\" ")

A = str(input())
if A=="A":
    multipy()
elif A=="B,":
    division()
elif A=="C":
    bmi()
elif A=="D":
    mtofeet()
elif A=="E":
    kgtopound()
elif A=="F":
    calorie()
elif A=="G":
    compint()
elif A=="H":
    avgmks()
elif A=="I":
    rupee_to_doll()
elif A=="J":
    kinematics()
print("......................................................THANKS FOR USING OUR SERVICE......................................................")