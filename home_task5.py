from datetime import datetime

class Publishing:
    def __init__(self, text):
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

        class News(Publishing):
            print("News_____________")

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M")
        print(date_time)
        a = News(val)

        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nNews-------------------------\n{a.i}.\n{city},{date_time}")
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
        days_left = due_date - now_date
        print(days_left)

        ad = Advertisement(val)

        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nPrivate Ad ------------------\n{ad.i}.\nActual until: {due_date}, {days_left.days} days left")
        f.close()

    if val == 3:
        val = str(input("Share your funny mood with us here: "))

        # ending = str("Stay tuned for our next jokes")

        class Jokes(Publishing):
            print("Joke of the day ------------")

            def __init__(self, text, default_ending="Stay tuned for our next jokes"):
                Publishing.__init__(self, text=text)
                self.j = default_ending

        jk = Jokes(val)

        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nJoke of the day -------------\n{jk.i}.\n{jk.j}")
        f.close()

        # class Jokes(Publishing):
        #     print("Joke of the day ------------")
        # jk = Jokes(val)
        #
        # f = open(r"C:\WORK\Test.txt", "a")
        # f.write(f"\n\nJoke of the day ------------\n{jk.i}.\n{ending}")
        # f.close()


if __name__ == '__main__':
    main()