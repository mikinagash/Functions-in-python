#1-10 test
#1
# def even(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("not even")
# even(int(input("choose number:")))

#2
# def avg():
#     x = int(input("enter number:"))
#     y = int(input("enter number:"))
#     z = int(input("enter number:"))
#     return (x + y + z) //3
# print(avg())

#3
# def count_digit(x):
#     while x != "999":
#      print(len(x))
#      x = input("enter number:\n")
# count_digit("5")

# #4
# def change(price):
#     change20 = price // 20
#     change10 = (price - change20 * 20) // 10
#     change5 = (price-change20*20 - change10*10) // 5
#     change1 = (price-change20*20-change10*10 -change5*5) //1
#     return change20,change10,change5,change1
# a = change(158)
# print(a)
#
# #5
# p6=int(input('Enter Number'))
# p8=int(input('Enter Number'))
# p7=p6**p8
# print(p7)


#6
# def above_1000(price):
#     sale = price * 0.35
#     result1 = price - sale
#     print('favorite customer, you get a discount of 35% , the new price is :')
#     return round(result1, 3)
# def sale_price():
#     price = int(input('enter price:'))
#     if price >= 1000:
#         call_function = (above_1000(price))
#         return round(call_function, 3)
#     else:
#         answer = price * 0.10
#         result2 = price - answer
#         print('you get discount of 10% , the new price is :')
#         return result2
#
# sale_price()

#program for square equation solution
#7
# import math
# a = float(input("enter a:"))
# b = float(input("enter b:"))
# c = float(input("enter c:"))
# d=b**2-4*a*c
# x1 = (-b+math.sqrt(d))/(2*a)
# x2 = (-b-math.sqrt(d))/(2*a)
# print("a=",a,"b=",b,"c=",c)
# print("first root=",x1)
# print("second root=",x2)


#9
# from math import *
# import sys
# def bigger(x,y):
#     empty_list = []
#     for i in range(1,x+1):
#         if x%i==0 and y%i==0:
#             empty_list.append(i)
#     print("you are the biggest devider -")
#     return max(empty_list)
#
#
# def smallest(x,y):
#     empty_list2 = []
#     for i in range(1,x+1):
#         if x%i==0 and y%i==0:
#             empty_list2.append(i)
#     print("you are the lowest devider -")
#     return min(empty_list2)
#
#
# def choice():
#     num1 = int(input("enter number :"))
#     num2 = int(input("enter number :"))
#     n = input("a-biggest divider b-smallest divider c-power d-result of sqrt e-exit: ")
#     if n == "a":
#         print(bigger(num1,num2))
#     elif n == 'b':
#         print(smallest(num1,num2))
#
#     elif n == "c":
#         power = num1 ** num2
#         print(power)
#     elif n == "d":
#         result = sqrt(num1)-sqrt(num2)
#         print(result)
#     elif n == "e":
#         return
#     else:
#         sys.stderr.write("Invalid choise")
# choice()

#q11
# def customers():
#     customers_id = int(input("what is your customer id ?"))
#     goods_in_year = int(input("what is your goods in year ?"))
#     bills_in_time = int(input("did you pay biils in time ? 1-yes 2-no"))
#     seniorty_in_company = int(input("what is your seniorty in the company?"))
#     if goods_in_year > 8000 and bills_in_time == 1 or seniorty_in_company >5:
#          print(customers_id,"You deserve special care ")
#     elif bills_in_time == 1:
#         print(customers_id,"You deserve special care")
#     elif goods_in_year > 8000 and bills_in_time == 1 and seniorty_in_company >= 5:
#         print(customers_id, "You spacial custome ! You deserve special care ")
#customers()

