# # print("Hello"+ input("what is your name "))
# # name= input("enter your name ")
# # lenght=len(name)
# # print(lenght)


# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])

# print (8/3)

# score= 5
# height=8
# iswining=True

# print (f" your score is {score}, and height{height}")
# a = int("5") / int(2.7)
# print(type(a))


# if year % 4 == 0:
#     if year%100==0:
#         if year %400==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")    
#     else: 
#             print("Leap year.")   
# else: 
#     print("Not leap year.")


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


new_name1=name1.lower()
new_name2=name2.lower()

sum1=new_name1.count('l')+new_name1.count('o')+new_name1.count('v')+new_name1.count('e')

sum2=new_name2.count('l')+new_name2.count('o')+new_name2.count('v')+new_name2.count('e')
scale=str(sum1)+str(sum2)

if int(scale) <10 or int(scale)> 90 :
    print(f"Your score is {scale}, you go together like coke and mentos.")
elif int(scale) <50 or int(scale)> 40:
   print(f"Your score is {scale}, you go together like coke and mentos.")
else : 
       print(f"Your score is {scale}.")

print('''
*******************************************************************************
"Dip the Apples in the Honey"

                   |
                  |  |
                     |
                 _ /_
            |   ( `' )
             |   `~~'
           |         |
            _ /_   |  |  -Lee Lawrence-
           ( `' )  _\ _
       __---`~~'--( `' )--__
      |||||||||||||||||||||||
       |  _ _ _  __   ___  |
       |  \_|_/  __|_   |  |
        \_________________/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction= input("You are in cross off the way which way you choose? left or right? ")


if direction =="left" :
  bout=input("you waiting on the river side?swim or wait  ")
  if bout =="wait":
    door = input("you reach to the three door end what you will choose?Red or Blue or Yellow ")
    if door=="Red":
      print("Burned by fire.Game Over")
    elif door=="Blue":
      print("Eaten by beasts.Game Over")
    elif door=="Yellow":
      print("You Win!")
    else:
      print("Game Over")
    
  else:
      print("Attacked by trout.Game Over")

else:
  print("Fall into a hole.Game Over")