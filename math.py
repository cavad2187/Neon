import math


print("Neon K Proqramına Xoş Gəlmisiniz")

a=int(input("a Əmsalını Qeyd Edin: "))
b = int(input("b Əmsalını Qeyd Edin: "))
c = int(input("Sərbəst Həddi Qeyd Edin: "))

d = (b*b)-(4*a*c)

if (d>0):
    x1 = math.floor((-b - math.sqrt(d))/(2*a))
    x2 = math.floor((-b + math.sqrt(d))/(2*a))
    print("Diskliminat 0-dan Böyük Olduğuna Görə Tənliyin 2 Kökü Var.")
    print("Tənliyin Kökləri: ",x1,x2)
elif (d==0):
    xb = math.floor((-b)/(2*a))
    print("Diskliminat 0-a Bərabər Olduğuna Görə x1=x2")
    print("Tənliyin Kökü: ",xb)

else:

    print("T'nliyin Kökü Yoxdur :(")
