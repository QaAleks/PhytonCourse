#existing library
import random
#create changeble list
a_list = []
# define range of list
#a_list=random.sample(range(0,1000),100)
for i in range(100):
# use method appent add to the list 1000 values. raindit-existing method in random library
    a_list.append(random.randint(0, 1000))

#
for k in range(len(a_list)):
    for j in range(k + 1, len(a_list)):
# comparison k and j what the biggest
        if a_list[k] > a_list[j]:
# change place if one bigger than other one
           a_list[k], a_list[j] = a_list[j], a_list[k]

print (a_list)

# define counters
even_sum, odd_sum = 0, 0
for num in a_list:
    # even numbers
    if num % 2 == 0:
        even_sum += num
    # odd numbers
    else:
        odd_sum += num

print("Sum of Even numbers in the list: ", even_sum)
print("Sum of Odd numbers in the list: ", odd_sum)

even_count, odd_count = 0, 0
for cnt in a_list:
    # even numbers
    if cnt % 2 == 0:
        even_count += 1
    # odd numbers
    else:
        odd_count += 1

print("Count of Even numbers in the list: ", even_count)
print("Count of Odd numbers in the list: ", odd_count)

averg_even = even_sum/even_count
averg_odd = odd_sum/odd_count

print("Average for Even numbers in the list: ", averg_even)
print("Average for Odd numbers in the list: ", averg_odd)


