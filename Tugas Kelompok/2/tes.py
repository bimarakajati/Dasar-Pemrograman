# lst = [ ] 
# n = int(input("Enter number of elements : ")) 

# for i in range(0, n): 
# 	ele = [input(), int(input())] 
# 	lst.append(ele) 
	
# print(lst)

# listLen = int(input("Enter the number of sublist "))

# print("\n")
# finalList = [[int(input("Enter number: ")) for _ in range(listLen)] for _ in range(listLen)]
# print("List is")
# print(finalList)

# # Program menentukan Bil Prima
# # kamus
# batas = int(input('Masukan batas: '))
# i = 0
# # algoritma
# while(i < batas):
#     if (i%2 == 0) : 
#         print (i, 'adalah bilangan Genap')
#     else:
#         print(i, 'adalah bilangan Ganjil')
#     i += 1

# print ('Program Selesai!')

# # Program menentukan Bil Prima
# # kamus
# batas = int(input('Masukan batas: '))
# i = 2
# # algoritma
# while(i < batas):
#     j = 2
#     while(j <= (i/j)):
#         if (i%j == 0):
#             break
#         j += 1
#     if (j > i/j) : 
#         print (i, 'adalah bilangan prima')
#     i += 1

# print ('Good bye!')

# # Program menentukan Bil Prima
# # kamus
# batas = int(input('Masukan batas: '))
# i = 2
# # algoritma
# while(i < batas):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): 
#             break
#         j = j + 1
#     if (j > i/j) : 
#         print (i, 'adalah bilangan prima')
#     i = i + 1

# print ('Good bye!')

from typing import List, Any
from collections import OrderedDict


class Personal_Budget:
    week: int
    wk_income: [int]
    wk_expenses: [{str: int}]
    wk_savings: [int]

    def __init__(self):
       
        self.week = 1
        self.week_info = OrderedDict()
        self.set_week(1)

    def set_week(self, week):
        for previous_week in range(self.week, week-1):
            self.week_info[previous_week] = {'wk_income': 0, "wk_expenses": {}, "wk_savings": 0}
        self.week = week
        self.week_info[week] = {'wk_income': 0, "wk_expenses": {}, "wk_savings":0}

    def add_weekly_inc(self, wk_inc):
        self.week_info[self.week]['wk_income'] = wk_inc

    def set_weekly_sav(self, wk_sav):
        self.week_info[self.week]['wk_savings'] = wk_sav

    def add_weekly_exp(self, item: str, amount: int):
        try:
            self.week_info[self.week]["wk_expenses"][item] += amount
        except KeyError:
            self.week_info[self.week]["wk_expenses"][item] = amount


    def statement(self, week):
        print(self.week_info)
        # Statement contains: Total income, Total expense, (T_income - T_expense) and (T_income - T_expense - T_savings)
        statement_arr = []
        # statement_arr = [[12, 13, 14, 56], [12, 54, 78, 90]]
        total_arr = [0,0,0,0]

        for iweek,week_info in self.week_info.items():
            if iweek > week:
                break
            income = week_info['wk_income']
            expense = sum(week_info['wk_expenses'].values())
            savings = week_info['wk_savings']
            cash = income - expense
            spendable = cash - savings

            total_arr[0] += income
            total_arr[1] += expense
            total_arr[2] += cash
            total_arr[3] += spendable

            weekly_statement = [income,expense,cash,spendable]
            statement_arr.append(weekly_statement)
        with open("personal_budget.txt", "w") as file:
            file.write("Total Income:" + str(total_arr[0]) + "\n" + "Total Expenses:" + str(total_arr[1]) + "\n" + "Cash in hand:" + str(total_arr[2]) + "\n" + "Amount Spendable:" + str(total_arr[3]))




        print(statement_arr)

    def view_statement(self):
        f = open("personal_budget.txt", "r")
        read = f.read()
        print("\n", read)
        return read


def main():
    pb = Personal_Budget()
    week = 0
    print("This program is going to help you plan your monthly budget")
    k = input("Hit the <Enter> key or type 'end' to stop the program: ")
    while k != 'end':
        week += 1
        pb.set_week(week)
        wk_inc = input("Enter you income for the week here: ")
        pb.add_weekly_inc(int(wk_inc))

        wk_sav = input("How much of your income do you plan to save this week: ")
        pb.set_weekly_sav(int(wk_sav))

        print("Are you going to enter an expense?")
        ans = input("Yes or No: ")
        ans = ans.lower()

        while ans == "yes" or ans == "y":
            amount_1 = input("How much did you spend (example: 2.00): ")
            expense = input("What did you spend this money on (example: 'Bread'):")
            pb.add_weekly_exp(expense, int(amount_1))
            print("Are you going to enter an expense?")
            ans = input("Yes or No: ")
            ans = ans.lower()

        k = input("Hit the <Enter> key or type 'end' to stop the program: ")
        pb.statement(3)
        pb.view_statement()


main()