#existing library
import random
#create changeble list
a_list = []
# define range of list
#a_list=random.sample(range(0,1000),100)
for i in range(100):
# use method appent add to the list 1000 values. raindit-existing method in random library
    a_list.append(random.randint(0, 1000))

# start sorting. Set for variable k index numbers to the each value of a_list (from 0 to 99)
for k in range(len(a_list)):
    #set for variable j value k+1 for a_list
    for j in range(k + 1, len(a_list)):
# comparison k and j what the biggest?
        if a_list[k] > a_list[j]:
# change place if one bigger than other one
           a_list[k], a_list[j] = a_list[j], a_list[k]

print (a_list)

# define variables for sum even and odd values for using in average counting
even_sum, odd_sum = 0, 0
for num in a_list:
    # sum of even
    if num % 2 == 0:
        even_sum += num
    # sum of odd
    else:
        odd_sum += num

print("Sum of Even numbers in the list: ", even_sum)
print("Sum of Odd numbers in the list: ", odd_sum)
# define variables for count even and odd values for using in average counting
even_count, odd_count = 0, 0
for cnt in a_list:
    # count of even
    if cnt % 2 == 0:
        even_count += 1
    # count of odd
    else:
        odd_count += 1

print("Count of Even numbers in the list: ", even_count)
print("Count of Odd numbers in the list: ", odd_count)

#average count
averg_even = even_sum/even_count
averg_odd = odd_sum/odd_count

print("Average for Even numbers in the list: ", averg_even)
print("Average for Odd numbers in the list: ", averg_odd)


