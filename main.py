name = input("Enter Your Name: ")
fav_num1 = int(input("Number 1: "))
fav_num2 = int(input("Number 2: "))
fav_num3 = int(input("Number 3: "))
fav_num_list = []
fav_num_status = []
fav_num_square = []


sum = fav_num1 + fav_num2 + fav_num3
#  to check prime
prime = True
for i in range(2,sum):
      if(sum<2):
            prime = False
            break
      else:
         if  sum % i == 0:
            prime = False
            break
       
fav_num_list.append(fav_num1)
fav_num_list.append(fav_num2)
fav_num_list.append(fav_num3)

for num in fav_num_list:
      fav_num_status.append((num, "even" if num % 2 == 0  else "odd"))
      fav_num_square.append((num , num*num))
print(f"Welcome {name}! lets figure out your favorite numbers") 
for num in fav_num_status:
      print(f"The number {num[0]} is {num[1]} ")
for num in fav_num_square:
      print(f"The number is {num[0]} and its square ({num[0],num[1]})")
print(f"The sum of favorite's number is {sum} ")
print(f"The sum {sum} is {"prime" if(prime) else  "Not-Prime"}.")


