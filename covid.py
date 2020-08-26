#python 3.7.1

# corona is a dangerous disease, we must adhere
# this is a simple task code 
# which is to enter yes or no to some questions 
# about the symptoms of this virus
# and the code will give you the results in order.
# enjoy (:
import time
re = 1
while re:
  def ans():
    ansy = "yes","Yes","yEs","yES","YeS","yeS","1","YES"
    ansn = "no","No","nO","2","NO"
    print("~"*45)
    name = input("Enter Your Name ")
    print("~"*45)
    print("Welcome "+name)
    print("")
    time.sleep(0.5)
    print("I'am Advance Coronavirus Program\nbuild with python")
    print("")
    time.sleep(0.5)
    live = input("Where are you living? ")
    time.sleep(0.5)
    print("")
    print("What is the number of infected \npeople in " +live+"?")
    print("")
    print("1 = Less than 1000\n2 = Above 1000\n3 = Higher than 10,000\n4 = Wide spread")
    case = input("Select Number : ")
    print("")
    if case == "1":
      print("You should wear a mask when going out\nkeep a distance with people\nand also wash your hands well\nafter touching surfaces")
      print("and,Do not touch your face\nuntil you wash your hands ")
    elif case == "2":
      print("Adhere to the health\nconditions to avoid infection\nto avoid the spread of the epidemic\nin a larger scale")
      print("And try not to go out to absolutely necessary")
    elif case == "3":
      print("Try to stay away from the elderly\ntake the necessary precautions and \ntreat everyone around you as infected so \nthat you can resist this pandemic")
    elif case == "4":
      print("Stay at home, and if any of the symptoms\nappear on you\nget a check-up as\nsoon as possible")
    else:
      print("Wrong Input")
    print("")
    time.sleep(1)
    print("Now, I will ask you some questions\nto know your condition")
    print("yes or no")
    print("")
    time.sleep(1)
    q1 = input("Do you suffer from a headache? ")
    time.sleep(0.5)
    q2 = input("Are you having a fever? ")
    time.sleep(0.5)
    q3 = input("Do you have a dry cough / sneeze? ")
    time.sleep(0.5)
    q4 = input("Do you have a sore throat? ")
    print("")
    print("If you find the results have completed at\nleast 30%, take a Covid 19 test")
    print("")
    time.sleep(1)
    q5 = input("Finally,Do you have all the \nsymptoms I mentioned earlier? ")
    print("")
    time.sleep(0.5)
    if q1 in ansy:
      print("Q1 : Result / Risk : 10%")
    elif q1 in ansn:
      print("Q1 : No Risk")
    else:
      print("Wrong Input")
    time.sleep(0.5)
    if q2 in ansy:
      print("Q2 : Result / Risk : 20%")
    elif q2 in ansn:
      print("Q2 : No Risk")
    else:
      print("Wrong Input")
    time.sleep(0.5)
    if q3 in ansy:
      print("Q3 : Result / Risk : 40%")
    elif q3 in ansn:
      print("Q3 : No Risk")
    else:
      print("Wrong Input")
    time.sleep(0.5)
    if q4 in ansy:
      print("Q4 : Result / Risk : 30%")
    elif q4 in ansn:
      print("Q4 : No Risk")
    else:
      print("Wrong Input")
    time.sleep(0.5)
    print("")
    if q5 in ansy:
      print("Go to the hospital as soon as\npossible for a Covid 19 test\nas per your entries")
    elif q5 in ansn:
      print("Q5 : Good")
    else:
      print("Wrong Input")    
    print("")
  ans()
  re = int(input("Enter 1 to Restart Programe or 0 To Stop it "))
print("")
print("Thank You For Using This Program")
print("If You Like It Leave Star Please (:")
# end
