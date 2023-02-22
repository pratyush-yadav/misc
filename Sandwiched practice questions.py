login=input('Enter Password: ')
if login=='12345':
    print('Login Successful...\n')
    loop=2
    while loop==2:
        print('\nPress 1 for Assignment')
        print('Press 2 for Calculator')
        print('Press 3 for Raja mantri chor police')
        print('Press 4 for Other')
        print('Press 5 to Exit')
        option=int(input('\nWhat do you want to try? '))
        while option not in [1,2,3,4,5]:
            print('\nIncorrect input !\n')
            test=input('Do you want to try again? (y/n) ')
            if test in ['y','Y','']:
                option=int(input('\nWhat do you want to try? '))
            else:
                break
        if option==1:
            loop=1
            while loop==1:   
                print("\n\nWelcome to Assignment!\n\n\n")
                print('Q.01 Write a program that accepts two integers and print their sum.')
                print('Q.02 Write a program that accepts radius of a circle and prints its Area and Perimeter.')
                print('Q.03 Write a program that inputs a student’s marks in five subjects (out of 100) and prints the Total, Percentage and Grade.')
                print('Q.04 Write a program to compute area and perimeter of square.')
                print('Q.05 Write a program to compute area and perimeter of triangle.')
                print('Q.06 Write a program to compute simple interest and Amount.')
                print('Q.07 Write a program to compute Compound interest and Amount.')
                print('Q.08 Write a program to read two numbers and prints their quotient and remainder.')
                print('Q.09 Write a program to find whether a given number is even or odd?')
                print('Q.10 Write a program to find largest among three integers.')
                print('Q.11 Write a program to find lowest among three integers.')
                print('Q.12 Write a Program to perform arithmetic calculation using switch. This program inputs two operands and an operator then displays the calculated result.')
                print('Q.13 Write a Program to print first n Natural numbers and their sum.')
                print('Q.14 Write a Program to calculate factorial of an integer using while loop.')
                print('Q.15 Write a Program to check whether the given number is palindrome or not.')
                print('Q.16 Write a program to print Multiplication Table of a given number.')
                print('Q.17 Write a program to print Fibonacci series. i.e. 0 1 1 2 3 5 8 …')
                print('Q.18 Write a program to print following patterns on screen :')
                print('')
                print('(a)')
                print('*')
                print('* *')
                print('* * *')
                print('* * * *')
                print('* * * * *')
                print('')
                print('(b)')
                print('1')
                print('1 2')
                print('1 2 3')
                print('1 2 3 4')
                print('1 2 3 4 5')
                print('')
                print('(c)')
                print('5 4 3 2 1')
                print('4 3 2 1')
                print('3 2 1')
                print('2 1')
                print('1')
                print('')
                print('(d)')
                print('1')
                print('2 3')
                print('4 5 6')
                print('7 8 9 10')
                print('')
                print('Q.19 Given two integers x and n, compute x rest to power n. ')
                print('Q.20 Write a program to count number of digits in a given Number.')
                print('Q.21 Write a program to print the sum of Digits of a given Number.')
                print('Q.22 Write a program to convert Celsius to Fahrenheit and Fahrenheit to Celsius.')
                print('Q.23 Write a program to check the given Number is Prime or Composite.')
                print('Q.24 Write a program to generate the series of Prime numbers within a given range.')
                print('Q.25 Write a program to check the given number is Palindrome number or not.')
                print('Q.26 Write a program that inputs cost price and selling price for 10 items. The program then prints if the overall profit occurred or loss occurred.')
                print('Q.27 Write a program that asks the user for a year and prints out whether it is a leap year or not.')
                print('Q.28 Number Guessing Game-This program generates a random number between 1 and 100 and continuously asks the user to guess the number, giving hints along the way.')
                print('Q.29 Write a program to input some numbers repeatedly and print their sum. The program ends when the users say no more to enter (normal termination) or program aborts when the number entered is less than zero.')
                print('Q.30 Write a program to accept Transactions made in day and items sold in day for a week and then print average sales made per transaction.')
                question=int(input('\n\nEnter question number:  '))
                print('\n')
                if question==1:
                    print('Q.01 Write a program that accepts two integers and print their sum.\n')
                    a=int(input('Enter first number: '))
                    b=int(input('Enter second number: '))
                    print('\nsum of',a,'and',b,'is',a+b)
                elif question==2:
                    print('Q.02 Write a program that accepts radius of a circle and prints its Area and Perimeter.\n')
                    r=float(input('Enter radius of circle: '))
                    print('\nArea of circle is',3.14*r*r)
                    print('Perimeter of circle is',2*3.14*r)
                elif question==3:
                    print('Q.03 Write a program that inputs a student’s marks in five subjects (out of 100) and prints the Total, Percentage and Grade.\n')
                    print("Enter marks (out of 100)")
                    a=float(input('English: '))
                    b=float(input('Accountancy: '))
                    c=float(input('Business Studies: '))
                    d=float(input('Economics: '))
                    e=float(input('Informatics Practices: '))
                    total=a+b+c+d+e
                    percentage=total/5
                    if percentage>=81:
                        grade='A'
                    elif percentage>=61:
                        grade='B'
                    elif percentage>=41:
                        grade='C'
                    elif percentage>=33:
                        grade='D'
                    elif percentage<33:
                        grade='E'
                    print('\nTotal marks: ',total)
                    print('Percentage: ',percentage,'%')
                    print('Grade: ',grade)
                elif question==4:
                    print('Q.04 Write a program to compute area and perimeter of square.\n')
                    side=float(input('Enter side of square: '))
                    print('\nArea of square: ',side*side)
                    print('Perimeter of square: ',4*side)
                elif question==5:
                    print('Q.05 Write a program to compute area and perimeter of triangle.\n')
                    s1=float(input('Enter first side: '))
                    s2=float(input('Enter second side: '))
                    s3=float(input('Enter third side: '))
                    base=float(input('Enter base: '))
                    height=float(input('Enter height: '))
                    print('\nArea: ',0.5*base*height)
                    print('Perimeter: ',s1+s2+s3)
                elif question==6:
                    print('Q.06 Write a program to compute simple interest and Amount.\n')
                    P=float(input('Enter principal amount: '))
                    R=float(input('Enter rate of interest: '))
                    T=float(input('Enter time (in years): '))
                    interest=(P*R*T)/100
                    print('\nSimple interest: ',interest)
                    print('Total amount: ',P+interest)
                elif question==7:
                    print('Q.07 Write a program to compute Compound interest and Amount.\n')
                    P=float(input('Enter principal amount: '))
                    R=float(input('Enter rate of interest: '))
                    n=float(input('Enter time (in years): '))
                    ci=P*(1+R/100)**n
                    print('\ncompound interest: ',ci-P)
                    print('Total amount: ',ci)
                elif question==8:
                    print('Q.08 Write a program to read two numbers and prints their quotient and remainder.\n')
                    a=float(input('Enter first number: '))
                    b=float(input('Enter second number: '))
                    print('\nQutient of',a,'and',b,'is',a/b)
                    print('Remainder of',a,'and',b,'is',a%b)
                elif question==9:
                    print('Q.09 Write a program to find whether a given number is even or odd?\n')
                    a=int(input('Enter any number: '))
                    print()
                    if a%2==0:
                        print(a,'is an even number.')
                    else:
                        print(a,'is an odd number.')
                elif question==10:
                    print('Q.10 Write a program to find largest among three integers.\n')
                    a=int(input('Enter first number: '))
                    b=int(input('Enter second number: '))
                    c=int(input('Enter third number: '))
                    print()
                    if a>b and a>c:
                        print(a,'is the largest number.')
                    elif b>a and b>c:
                        print(b,'is the largest number.')        
                    elif c>a and c>b:
                        print(c,'is the largest number.')
                    else:
                        print('Confused!')
                elif question==11:
                    print('Q.11 Write a program to find lowest among three integers.\n')
                    a=int(input('Enter first number: '))
                    b=int(input('Enter second number: '))
                    c=int(input('Enter third number: '))
                    print()
                    if a<b and a<c:
                        print(a,'is the smallest number')
                    elif b<a and b<c:
                        print(b,'is the smallest number')
                    elif c<a and c<b:
                        print(c,'is the smallest number')
                    else:
                        print('Confused!')
                elif question==12:
                    print('Q.12 Write a Program to perform arithmetic calculation using switch. This program inputs two operands and an operator then displays the calculated result.\n')
                    operator=input('Enter operator( + - * / ) : ')
                    op1=int(input('Enter first operand: '))
                    op2=int(input('Enter second operand: '))
                    if operator=='+':
                        print('Answer: ',op1+op2)
                    elif operator=='-':
                        print('Answer: ',op1-op2)
                    elif operator=='*':
                        print('Answer: ',op1*op2)
                    elif operator=='/':
                        print('Answer: ',op1/op2)
                    else:
                        print('Invalid operator!')
                elif question==13:
                    print('Q.13 Write a Program to print first n Natural numbers and their sum.\n')
                    n=int(input('Enter range: '))
                    Sum=0
                    for i in range(1,n+1):
                        print(i)
                        Sum+=i
                    print('Sum of first',n,'natural numbers: ',Sum)
                elif question==14:
                    print('Q.14 Write a Program to calculate factorial of an integer using while loop.\n')
                    n=int(input('Enter any number: '))
                    a=n-1
                    m=n
                    while a>0:
                        n=n*a
                        a=a-1
                    print(str(m)+'! =',n)
                elif question==15:
                    print('Q.15 Write a Program to check whether the given number is palindrome or not.\n')
                    n=int(input('Enter any number: '))
                    reverse=0
                    orignal=n
                    while n>0:
                        reverse*=10
                        last=n%10
                        reverse+=last
                        n//=10
                    if orignal==reverse:
                        print(orignal,'is a palindrome')
                    else:
                        print(orignal,'is not a palindrome')
                elif question==16:
                    print('Q.16 Write a program to print Multiplication Table of a given number.\n')
                    n=int(input('Enter any number: '))
                    for i in range(1,11):
                        print(n,'x',i,'=',n*i)
                elif question==17:
                    print('Q.17 Write a program to print Fibonacci series. i.e. 0 1 1 2 3 5 8 …\n')
                    n=int(input('Enter number: '))
                    a=0
                    b=1
                    print(a)
                    print(b)
                    count=1
                    while count<=n:
                        print(a+b)
                        c=a+b
                        a=b
                        b=c
                        count+=1
                elif question==18:
                    print('Q.18 Write a program to print following patterns on screen :')
                    print('(a)')
                    for i in range(1,6):
                        print('*'*i)
                    print('(b)')
                    for i in range(1,6):
                        for j in range(1,i+1):
                            print(j,end=' ')
                        print()
                    print('(c)')
                    for i in range(5,0,-1):
                        for j in range(i,0,-1):
                            print(j,end=' ')
                        print()
                    print('(d)')
                    n=1
                    for i in range(1,5):
                        for j in range(1,i+1):
                            print(n,end=' ')
                            n+=1
                        print()
                elif question==19:
                    print('Q.19 Given two integers x and n, compute x rest to power n.\n')
                    x=int(input('Enter base(x): '))
                    n=int(input('Enter power(n): '))
                    print(x,'raised to power',n,'=',x**n)
                elif question==20:
                    print('Q.20 Write a program to count number of digits in a given Number.\n')
                    n=int(input('Enter any number: '))
                    count=0
                    while n!=0:
                        n//=10
                        count+=1
                    print('Number of digits: ',count)
                elif question==21:
                    print('Q.21 Write a program to print the sum of Digits of a given Number.\n')
                    n=int(input('Enter any number: '))
                    sum=0
                    while n!=0:
                        digit=n%10
                        n//=10
                        sum+=digit
                    print('Sum: ',sum)
                elif question==22:
                    print('Q.22 Write a program to convert Celsius to Fahrenheit and Fahrenheit to Celsius.\n')
                    print('Press 1 to convert celsius to fahrenheit')
                    print('Press 2 to convert fahrenheit to celsius')
                    option=int(input('\nWhat do you want to do? '))
                    if option==1:
                        c=float(input('Enter temprature (in celsius): '))
                        f=(9/5*c)+32
                        print(c,'c =',f,'f')
                    elif option==2:
                        f=float(input('Enter temprature (in fahrenheit): '))
                        c=(5*(f-32))/9
                        print(f,'f =',c,'c')
                    else:
                        print('Invalid input!')
                elif question==23:
                    print('Q.23 Write a program to check the given Number is Prime or Composite.\n')
                    n=int(input('Enter any number: '))
                    if n==0 or n==1:
                        print(n,'is neither prime nor composite')
                    else:
                        factor=0
                        for i in range(1,n+1):
                            if n%i==0:
                                factor+=1
                        if factor==2:
                            print(n,'is a prime number')
                        else:
                            print(n,'is a composite number')
                elif question==24:
                    print('Q.24 Write a program to generate the series of Prime numbers within a given range.\n')
                    a=int(input('Enter starting point: '))
                    b=int(input('Enter ending point: '))
                    for i in range(a,b+1):
                        factor=0
                        for j in range(1,i+1):
                            if i%j==0:
                                factor+=1
                        if factor==2:
                            print(i,end=' ')
                elif question==25:
                    print('Q.25 Write a program to check the given number is Palindrome number or not.\n')
                    orignal=int(input('enter any number: '))
                    n=orignal
                    reverse=0
                    while n!=0:
                        reverse*=10
                        last=n%10
                        reverse+=last
                        n//=10
                    if reverse==orignal:
                        print(orignal,'is a palindrome number')
                    else:
                        print(orignal,'is not a palindrome number')
                elif question==26:
                    print('Q.26 Write a program that inputs cost price and selling price for 10 items. The program then prints if the overall profit occurred or loss occurred.\n')
                    sum_costprice=sum_sellingprice=0
                    for i in range(1,11):
                        i=str(i)
                        cost=int(input('Enter cost price of item'+i+': '))
                        selling=int(input('Enter selling price of item'+i+': '))
                        sum_costprice+=cost
                        sum_sellingprice+=selling
                    difference=sum_sellingprice-sum_costprice
                    if difference>0:
                        print('Profit occurred: ',difference)
                    elif difference<0:
                        print('Loss occurred: ',difference)
                    else:
                        print('No profit, No loss')
                elif question==27:
                    print('Q.27 Write a program that asks the user for a year and prints out whether it is a leap year or not.\n')
                    year=int(input('Enter any year: '))
                    if year%4==0:
                        print(year,'is a leap year')
                    else:
                        print(year,'is not a leap year')
                elif question==28:
                    print('Q.28 Number Guessing Game-This program generates a random number between 1 and 100 and continuously asks the user to guess the number, giving hints along the way.\n')
                    test=1
                    random=((id(test))%100)+1
                    check=int(input('Enter any number: '))
                    while check!=random:
                        if check>random:
                            check=int(input('Enter smaller number: '))
                        else:
                            check=int(input('Enter larger number: '))
                    print('You got it right!')
                elif question==29:
                    print('Q.29 Write a program to input some numbers repeatedly and print their sum. The program ends when the users say no more to enter (normal termination) or program aborts when the number entered is less than zero.\n')
                    n=sum=0
                    while n==int(n):
                        n=input('Enter any number: ')
                        try:
                            n=int(n)
                            if n<0:
                                break
                            else:
                                sum+=n
                        except:
                            print('Sum: ',sum)
                            break
                elif question==30:
                    print('Q.30 Write a program to accept Transactions made in day and items sold in day for a week and then print average sales made per transaction.\n')
                    sum_items=sum_transactions=count=0
                    while count<7:
                        print('Day',count+1)
                        transactions=int(input('Enter transactions made: '))
                        items=int(input('Enter items sold: '))
                        sum_items+=items
                        sum_transactions+=transactions
                        count+=1
                    average=sum_items/sum_transactions
                    print('Average sales made per transaction: ',average)
                else:
                    print('Incorrect question number!\n')
                print('\n\nPress 1 to try again')
                print('Press 2 to enter main menu')
                loop=int(input("\n=>"))
        elif option==2:
            loop=1
            while loop==1:
                expression=input('\nExpreession: ')
                operator_index=answer=index_1=index_2=0
                operand_1=operand_2='0'
                len_exp=len(expression)
                for operator in expression:
                    if operator in('+','-','*','/','%','^'):
                        break
                    else:
                        operator_index+=1
                for index_1 in range(0,operator_index):
                    operand_1+=expression[index_1]
                for index_2 in range(operator_index+1,len_exp):
                    operand_2+=expression[index_2]
                operand_1,operand_2=int(operand_1),int(operand_2)
                if operator=='+':
                    answer=operand_1+operand_2
                if operator=='-':
                    answer=operand_1-operand_2
                if operator=='*':
                    answer=operand_1*operand_2
                if operator=='/':
                    answer=operand_1/operand_2
                if operator=='%':
                    answer=operand_1%operand_2
                if operator=='^':
                    answer=operand_1**operand_2
                print('Answer: ',answer)
                print('\n\nPress 1 to continue')
                print('Press 2 to enter main menu')
                loop=int(input("\n=>"))
        elif option==3:
            loop=1
            while loop==1:            
                import random as R
                import time
                print('*'*45)
                print('******* Raja - Mantri - Chor - Police *******')
                print('*'*45)
                name=input('\nEnter your name: ')
                input('\n\nPress enter to start distributing cheats.....\n\n')
                cheats=['Raja','Mantri','Chor','Police']
                score=[]
                final_score=[]
                score_a=score_b=score_c=score_d=0
                play='y'
                while play in ['Y','y','']:
                    a=b=c=d=R.randint(1,4)
                    while b==a:
                        b=R.randint(1,4)
                    while c==a or c==b:
                        c=R.randint(1,4)
                    while d==a or d==b or d==c:
                        d=R.randint(1,4)
                    for random in range(4):
                        if a==random+1:
                            if random==0:
                                raja='a'
                            if random==1:
                                mantri='a'
                            if random==2:
                                chor='a'
                            if random==3:
                                police='a'
                            a=cheats[random]
                        if b==random+1:
                            if random==0:
                                raja='b'
                            if random==1:
                                mantri='b'
                            if random==2:
                                chor='b'
                            if random==3:
                                police='b'
                            b=cheats[random]    
                        if c==random+1:
                            if random==0:
                                raja='c'
                            if random==1:
                                mantri='c'
                            if random==2:
                                chor='c'
                            if random==3:
                                police='c'
                            c=cheats[random]
                        if d==random+1:
                            if random==0:
                                raja=name
                            if random==1:
                                mantri=name
                            if random==2:
                                chor=name
                            if random==3:
                                police=name
                            d=cheats[random]
                    print('Distributing Cheats...\n')
                    time.sleep(2)
                    if d=='Raja':
                        print('Raja      => ',raja,'\nMantri  = ',mantri,'\nChor      =  ?\nPolice    =  ?\n')
                    elif d=='Mantri':
                        print('Raja      = ',raja,'\nMantri  => ',mantri,'\nChor      =  ?\nPolice    =  ?\n')
                    elif d=='Chor':
                        print('Raja      = ',raja,'\nMantri  = ',mantri,'\nChor     => ',chor,'\nPolice   = ',police,'\n')
                    elif d=='Police':
                        print('Raja      = ',raja,'\nMantri  = ',mantri,'\nChor     = ',chor,'\nPolice   => ',police,'\n')
                    if d=='Mantri':
                        op_1=R.randint(1,2)
                        if op_1==1:
                            op_1=chor
                            op_2=police
                        else:
                            op_1=police
                            op_2=chor
                        time.sleep(1)
                        print('Who is Chor (',op_1,'/',op_2,') ? ')
                        guess=input()
                        time.sleep(1)
                        if guess==chor:
                            print('You got it right.\n')
                            score_mantri=500
                            score_chor=0
                        else:
                            print('You guessed it wrong.\n')
                            score_mantri=0
                            score_chor=500
                    else:
                        time.sleep(1)
                        guess=R.randint(1,2)
                        if guess==1:
                            print('Mantri got it right.\n')
                            score_mantri=500
                            score_chor=0
                        else:
                            print('Mantri guessed it wrong.\n')
                            score_mantri=0
                            score_chor=500
                    for player in [a,b,c,d]:
                        if player=='Raja':
                            score.append(1000)
                        if player=='Mantri':
                            score.append(score_mantri)
                        if player=='Chor':
                            score.append(score_chor)
                        if player=='Police':
                            score.append(100)
                    time.sleep(2)
                    print('*'*43)
                    print('a','b','c',name,sep='\t')
                    for i in score:
                        print(i,end='\t')
                    print('\n*******************************************')
                    final_score.append(score)
                    score=[]
                    time.sleep(1)
                    play=input('\nDo you want to play next hand? (y/n)  ')
                    if play not in['y','Y','']:
                        for i in final_score:
                            score_a+=i[0]
                            score_b+=i[1]
                            score_c+=i[2]
                            score_d+=i[3]
                        if score_a>score_b and score_a>score_c and score_a>score_d:
                            winner='a'
                        elif score_b>score_a and score_b>score_c and score_b>score_d:
                            winner='b'
                        elif score_c>score_a and score_c>score_b and score_c>score_d:
                            winner='c'
                        elif score_d>score_a and score_d>score_b and score_d>score_c:
                            winner=name
                        else:
                            input('Play 1 more round to decide winner.\n')
                            play='y'
                time.sleep(2)
                print('\n\n\n*******************************************')
                print('*************** Final Scores **************')
                print('*******************************************\n')
                print('a','b','c',name,sep='\t',end='\n\n')
                for i in final_score:
                    for j in i:
                        print(j,end='\t')
                    print()
                print('______________________________')
                print(score_a,score_b,score_c,score_d,sep='\t',end='\n\n')
                print('\n*******************************************')
                print('*******************************************\n\n\n')
                time.sleep(2)
                print('Winner  =  ',winner)
                time.sleep(2)
                input('\n\n\nThank you! Play again.\n\n')
                print('\n\nPress 1 to Play again')
                print('Press 2 to enter main menu')
                loop=int(input("\n=>"))
        elif option==4:
            loop=1
            while loop==1:
                print('\nOld practice..\n')
                print("\nPress '1' to Swap values of 2 variables")
                print("Press '2' to Check whether the person is eligible for voting")
                print("Press '3' to Check whether the Number is Even or Odd")
                print("Press '4' to Check whether the Number is Positive or Negative")
                print("Press '5' to find the Smallest and Largest number among 3 given numbers")
                print("Press '6' to Calculate Area & Circumference of Circle")
                print("Press '7' to Calculate Area & Perimeter of Square")
                print("Press '8' to Calculate Area & Perimeter of Rectangle")
                print("Press '9' to Prepare GST Invoice")
                print("Press '10' to Calculate Total Marks, Percentage & Grades\n")
                IN=input('What do you want to try? ')
                if IN=='1':
                    print('\nSwap values of 2 variables\n')
                    var1=input('Enter Value of a: ')
                    var2=input('Enter Value of b: ')
                    var1,var2=var2,var1
                    print('\nNew a: ',var1,'\nNew b: ',var2)
                elif IN=='2':
                    print('\nCheck whether the person is eligible for voting\n')
                    age=float(input('Enter your age: '))
                    if age>=18:
                        print('\nYou are eligible for voting.')
                    else:
                        print('\nYou are not eligible for voting.')
                elif IN=='3':
                    print('\nCheck whether the Number is Even or Odd\n')
                    a=float(input('Enter Any Number: '))
                    if a==int(a):
                        a=int(a)
                        if a%2==0:
                            print('\n',a,'is an Even Number.')
                        elif a%2==1:
                            print('\n',a,'is an Odd Number.')
                        else:
                            print('\n',a,'is neither Even nor Odd.')
                    else:
                        print('non integer numbers are neither Even nor Odd!')
                elif IN=='4':
                    print('\nCheck whether the Number is Positive or Negative\n')
                    a=float(input('Enter Any Number: '))
                    if a==int(a):
                        a=int(a)#if a is an integer then this statement will convert float(a) to int(a)
                    else:
                        a=a
                    if a>0:
                        print('\n',a,'is a Positive Number.')
                    elif a<0:
                            print('\n',a,'is a Negative Number.')
                    else:
                        print('\n',a,'is neither Positive nor Negative.')
                elif IN=='5':
                    print('\nTo find the Smallest and the Largest numbers among 3 given numbers\n')
                    a=float(input('Enter First number: '))
                    b=float(input('Enter Second number: '))
                    c=float(input('Enter Third number: '))
                    if a==int(a):
                        a=int(a)
                    if b==int(b):
                        b=int(b)
                    if c==int(c):
                        c=int(c)
                    if a<b and a<c:
                        print('\nSmallest number: ',a)
                    elif b<a and b<c:
                        print('\nSmallest number: ',b)
                    elif c<a and c<b:
                        print('\nSmallest number: ',c)
                    else:
                        print('\nSmallest number: Confused!')
                    if a>b and a>c:
                        print('Largest number: ',a)
                    elif b>a  and b>c:
                        print('Largest number: ',b)
                    elif c>a and c>b:
                        print('Largest number: ',c)
                    else:
                        print('Largest number: Confused!')
                elif IN=='6':
                    print('\nCalculate Area & Circumference of Circle\n')
                    r=float(input('Enter Radius of Circle: '))
                    print('Area of circle: ',round(3.14*r*r,2),'\nCircumference of circle: ',round(2*3.14*r,2))
                elif IN=='7':
                    print('\nCalculate Area & Perimeter of Square\n')
                    s=float(input('Enter Side of Square: '))
                    print('Area of Square: ',round(s*s,2),'\nPerimeter of Square: ',round(4*s,2))
                elif IN=='8':
                    print('\nCalculate Area & Perimeter of Rectangle\n')
                    l=float(input('Enter Length of Rectangle: '))
                    b=float(input('Enter Breadth of Rectangle: '))
                    print('Area of Rectangle: ',round(l*b,2),'\nPerimeter of Rectangle: ',round(2*(l+b),2))
                elif IN=='9':
                    print('\nPrepare GST Invoice\n')
                    item=input('Enter Name of Item: ')
                    price=float(input('Enter Price of Item: '))
                    qty=int(input('Enter Quantity of Item: '))
                    gst=int(input('Enter Rate of GST (%): '))
                    P=round(price*qty,2)
                    cgst=sgst=round(P*gst/200,2)
                    print('\n\n\tINVOICE\n')
                    print('Item: ',item)
                    print('Price: ',P)
                    print('CGST @',gst/2,'%: ',cgst)
                    print('SGST @',gst/2,'%: ',sgst)
                    print('Total Price: ',round(P+cgst+sgst,2))
                elif IN=='10':
                    print('\nCalculate Total Marks, Percentage & Grades\n')
                    s1=float(input('Enter Marks of English: '))
                    s2=float(input('Enter Marks of Accountancy: '))
                    s3=float(input('Enter Marks of Business Studies: '))
                    s4=float(input('Enter Marks of Economics: '))
                    s5=float(input('Enter Marks of Informatics Practices: '))
                    total=s1+s2+s3+s4+s5#s=Subject
                    if s1>=0 and s1<=100 and s2>=0 and s2<=100 and s3>=0 and s3<=100 and s4>=0 and s4<=100 and s5>=0 and s5<=100:
                        print('\nTotal Marks : ',total,'\nPercentage : ',total/5,'%')
                        if total/5>=91:
                            g='A1'
                        elif total/5>=81:
                            g='A2'
                        elif total/5>=71:
                            g='B1'
                        elif total/5>=61:
                            g='B2'
                        elif total/5>=51:
                            g='C1'
                        elif total/5>=41:
                            g='C2'
                        elif total/5>=33:
                            g='D'
                        else:
                            g='FAIL, Better Luck Next Time...'
                        print('Grade: ',g)
                    else:
                        print('\nInvalid Marks!\nCheck the Marks and try again.')
                else:
                    print('Invalid Input!')
                print('\n\nPress 1 to Play again')
                print('Press 2 to enter main menu')
                loop=int(input("\n=>"))
        elif option==5:
                exit()
else:
    print('Incorrect Password')
input('\n\nPress enter to exit...')
