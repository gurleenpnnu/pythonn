

# function defination
# def avg():
#     a = int(input('enter the number: '))
#     b = int(input('enter the number: '))
#     c = int(input('enter the number: '))

#     avrg = (a+b+c)/3
#     print(avrg)
# # function call
# avg()
# avg()


# def goodday(name,ending="tysm"):
   
#     print(f"good dayy, {name}")
#     print(ending)
#     return "done"

# a=goodday('harry')
# print(a)
# goodday('divya',"thanks")


# recursion

# def factorial():
#     if (n==1 or n==0):
#         return 1
#     return n*factorial(n-1)


# n = int(input("enter no.: "))
# print(f"The factorial of{n} is {factorial(n-1)}")


# c to f 
# def f_to_c():

#    return (c*1.8)+32

# c = float(input("enter temperature in c: "))
# print(f_to_c())
# print(f"{round(f_to_c,2)}")

# def sum(n):


#     if n==1:
#         return 1

#     return sum(n-1) + 1



# print(sum(8))


# def pttrn(n):
#     if n==0:
#         return 
#     print("*"*n)
#     pttrn(n-1)

# pttrn(3)
# pttrn(5)

def rem(l,word):
    n = []

    for item in l:
        if not(item==word):
            n.append(item.strip(word))

l = ["harry","hardik","rhon","jack"]
print(rem(l,"ik"))