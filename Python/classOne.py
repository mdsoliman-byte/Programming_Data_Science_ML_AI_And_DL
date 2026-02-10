#variable : variable_name = "data"
name = "Soliman"
age = 26
education = "BSC"
marride_status = False
waith = 54.60
birthYear = 1999
birthMonth = "April"
birthDay = "04"
address = "Barishal , Bhola , Charfassion , 8340"

#print("Hay im , {} my age {}, i sturdy in {}".format(name,age,education))

#variable Type 
nameIsString = type(name)
ageIsInteger = type(age)
marride_statusIsBoolean = type(marride_status)
waithIsFloat = type(waith)
#print("Name : {}, Age : {}, Marrid Status : {}, Waith : {}".format(nameIsString,ageIsInteger, marride_statusIsBoolean,waithIsFloat))


# Basic Math Operation
dataA = 125
dataB = 10
addition = dataA + dataB
subtraction = dataA - dataB
multiplication = dataA * dataB
division = dataA / dataB
florDevision = dataA // dataB
modulus = dataA % dataB
exponentation = dataA ** dataB
#print("Addition {}\nSubtraction {}\nMultiplication {}\nDivision {}\nFlor Division {}\nModulus {}\nExponentation {} ".format(addition, subtraction,multiplication,division,florDevision,modulus,exponentation))

#Expenses Calculation
food = 3000
lifeStyle = 2000
flateRant = 6000
totalExpences =round((food + lifeStyle + flateRant) / 2)
print("My Tottal Expenses {} ".format(totalExpences))
