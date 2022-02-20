#
# now = datetime.now()
# date_time = now.strftime("%m/%d/%Y, %H:%M")
#
#
# class SelectTopic:
#     def __init__(self):
#         self.entered_value = input(
#             'Enter 1 if you want to add NEWS,\nEnter 2 if you want to add Private Ad,\nEnter 3 if you want to add Joke value,\nType here and click Enter: ')
#
# a = SelectTopic()
# print(a.entered_value)
# num = a.entered_value
from datetime import datetime

class Publishing:
    def __init__(self,  text):
        self.i = text

def main():

    while True:
        try:
            val = int(input(
                'Enter 1 if you want to add NEWS,\nEnter 2 if you want to add Private Ad,\nEnter 3 if you want to add Joke value,\nType here and click Enter: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if val not in [1, 2, 3]:
            print("Please enter correct number")
            continue
        else:
            print(val)
            break

    if val == 1:
        val = str(input("Type your News text here: "))
        city = str(input("Type location (e.g. London): "))



        # if val==3:
        #     a.jokes

        class News(Publishing):
            print("News_____________")

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M")
        print(date_time)
        a = News(val)

        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nNews----------------------\n{a.i}.\n{city},{date_time}")
        f.close()

    if val == 2:
        val = str(input("Type your Advertisement text here: "))
        while True:
            due_date = str(input("Type Ad due date here(mm/dd/yyyy): "))
            try:
                due_date = datetime.strptime(due_date, '%m/%d/%Y').date()
                break
            except ValueError:
                print("This is not in the right format")

        class Advertisement(Publishing):
            print("Private Ad ------------------")

        now = datetime.now()
        now_date = now.date()
        days_left = due_date-now_date
        print(days_left)

        ad = Advertisement(val)

        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nPrivate Ad ------------------\n{ad.i}.\nActual until: {due_date}, {days_left.days} days left")
        f.close()

if __name__ == '__main__':
    main()

# print(a.entered_value)







# f = open(r"C:\WORK\Test.txt","a")
# # f.write('\n\n')
# f.write("\n\ntest try4")
# f.close()

# # print(f.read())

# while True:
#     num = input("Please enter a number ")
#     try:
#         val = int(num)
#         print("Input is an integer number.")
#         print("Input number is: ", val)
#         break;
#     except ValueError:
#         try:
#             float(num)
#             print("Input is an float number.")
#             print("Input number is: ", val)
#             break;
#         except ValueError:
#             print("This is not a number. Please enter a valid number")

# from datetime import datetime
#
# now = datetime.now()
# date_time = now.strftime("%m/%d/%Y, %H:%M")

#
# class SelectTopic:
#     def __init__(self):
#         self.entered_value = int(input(
#             'Enter 1 if you want to add NEWS,\nEnter 2 if you want to add Private Ad,\nEnter 3 if you want to add Joke value,\nType here and click Enter: '))


# a = SelectTopic()
# print(a.entered_value)