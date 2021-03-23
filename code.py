# unit converter

num1 = input('Enter the unit value: ')
unit1 = input('Unit you want it convert from:  ')
unit2 = input('Unit you want it convert to: ')

if unit1 == "cm" and unit2 == "m":
    result = float(num1) / 100
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "mm" and unit2 == "cm":
    result = float(num1) / 10
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "m" and unit2 == "cm":
    result = float(num1) * 100
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "cm" and unit2 == "mm":
    result = float(num1) * 10
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "mm" and unit2 == "m":
    result = float(num1) / 1000
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "m" and unit2 == "mm":
    result = float(num1) * 1000
    print("RESULT: ", num1, unit1, "=", result, unit2)
elif unit1 == "km" and unit2 == "m":
    result = float(num1) * 1000
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "m" and unit2 == "km":
    result = float(num1) / 1000
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "mm" and unit2 == "km":
    result = float(num1) / 1000000
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "ft" and unit2 == "cm":
    result = float(num1) * 30.48
    print("RESULT: ", num1, unit1, "=", result, unit2)
elif unit1 == "ft" and unit2 == "mm":
    result = float(num1) * 304.8
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "ft" and unit2 == "inch":
    result = float(num1) * 12
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "inch" and unit2 == "cm":
    result = float(num1) * 2.54
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
elif unit1 == "inch" and unit2 == "mm":
    result = float(num1) * 25.4
    print("RESULT: ",num1 ,unit1 ,"=",result , unit2)
