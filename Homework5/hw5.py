#1----------------------------
h = int(input("Enter how many kg Haim takes>>>"))
n = int(input("Enter how many kg Nastya takes>>>"))
al = int(input("Enter how many kg Alex takes>>>"))
an = int(input("Enter how many kg Anna takes>>>"))
def haim(h):
    return  float((h + n + al + an) / 100 *h)
def nastya(n):
    return float((h + n + al + an) / 100 *n)
def alex(al):
    return float((h + n + al + an) / 100 *al)
def anna(an):
    return float((h + n + al + an) / 100 *an)
res1 = haim(h)
res2 = nastya(n)
res3 = alex(al)
res4 = anna(an)
total = h+n+al+an
res5 = total/4
print(f"Total apples in family {total}kg\nHaim got {h}kg\nNastya got {n}kg\n"
      f"Alex got {al}kg\nAnna got {an}kg\nAverage for each - {res5}kg")
#2---------------

nastya_hours = input("Enter Nastya`s work hours>>>")
nastya_wage = input("Enter Nastya`s hour wage>>>")
nastya_tax = input("Enter Nastya`s tax level>>>")
alex_hours = input("Enter Alex`s work hours>>>")
alex_wage = input("Enter Alex`s hour wage>>>")
alex_tax = input("Enter Alex`s tax level>>>")
def salary(a: float, b: float, c:float) -> str:
    return (f"{(a*b)*(1-c/100):.2f}")
res1 = salary(float(alex_hours), float(alex_wage),float(alex_tax))
res2 = salary(float(nastya_hours), float(nastya_wage),float(nastya_tax))
print(f"Alex`s salary - {res1}\nNastya`s salary - {res2}")

#3---------------

nastya_hours = input("Enter Nastya`s work hours>>>")
nastya_wage = input("Enter Nastya`s hour wage>>>")
nastya_tax = input("Enter Nastya`s tax level>>>")
nastya_bonus = input("Enter Nastya`s bonus>>>")
alex_hours = input("Enter Alex`s work hours>>>")
alex_wage = input("Enter Alex`s hour wage>>>")
alex_tax = input("Enter Alex`s tax level>>>")
alex_bonus = input("Enter Alex`s bonus>>>")
def salaryAdv(a: float, b: float, c:float, d: float) -> str:
   # return (f"{(a*b)},{c/100*(a*b)}, {(a*b)-c/100*(a*b)}, "
   #         f"{((a*b)-c/100*(a*b))*d/100}")
    return (f"{(a*b)*(1-c/100)*(1+d/100):.2f}")
res1 = salaryAdv(float(alex_hours), float(alex_wage),float(alex_tax),float(alex_bonus))
res2 = salaryAdv(float(nastya_hours), float(nastya_wage),float(nastya_tax),float(nastya_bonus))
print(f"Alex`s salary - {res1}\nNastya`s salary - {res2}")
