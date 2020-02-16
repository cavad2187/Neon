import math


print("Neon K Proqramına Xoş Gəlmisiniz")



str = input("Tərəf ilə olan düsturu seçmək istəyirsinizsə t hərfinə basın diaqonallarla istəyirsinizsə d düyməsinə basın: ")

if (str == "t"):
    a = int(input("Tərəfi Qeyd Edin: "))
    h = int(input("Hündürlüyü Qeyd Edin: "))
    s = a*h
    print("S = ",s)
elif(str == "d"):
    d1 = int(input("Birinci Dioqnalı Qeyd Edin: "))
    d2 = int(input("İkinci Dioqnalı Qeyd Edin: "))
    sd = (d1*d2)//2
    print("S = ",sd)
else:
    print("Undefined")
