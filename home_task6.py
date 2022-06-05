from datetime import datetime
import os


class Publishing:
    def __init__(self, text):
        self.i = text

class News(Publishing):

    def __init__(self, text_news, city):
        Publishing.__init__(self, text=text_news)
        self.z = city

    def pubdays(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M")
        return date_time

    def write_news(self):
        f = open(r"Test.txt", "a")
        f.write(f"\n\nNews-------------------------\n{self.i}.\n{self.z},{self.pubdays()}")
        f.close()

class Advertisement(Publishing):
    def __init__(self, text_ad, future_date):
        Publishing.__init__(self, text=text_ad)
        self.w = future_date

    def count_days(self):
        now = datetime.now()
        now_date = now.date()
        days_left = self.w - now_date
        return days_left

    def write_ads(self):
        f = open(r"Test.txt", "a")
        f.write(f"\n\nAdvertisement-------------------------\n{self.i}.\n{self.w},{self.count_days()}")
        f.close()


class Jokes(Publishing):

    def __init__(self, text_joke, default_ending="Stay tuned for our next jokes"):
        Publishing.__init__(self, text=text_joke)
        self.j = default_ending

    def write_joke(self):
        f = open(r"Test.txt", "a")
        f.write(f"\n\nJoke of the day -------------\n{self.i}.\n{self.j}")
        f.close()

class FromFileToFile :

    def input_from_file(self):
        with open("input_text.txt", "r") as source_file, open(r"Test.txt", "a") as input_text:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            input_text.write("\n" + date_time + "\n")
            for line in source_file:
                low_case = line.lower()
                cap_first_char = low_case.capitalize()
                input_text.write(cap_first_char)
                print(line)
            source_file.close()
            input_text.close()

            os.remove("input_text.txt")

def main():
    while True:
        try:
            first_select=int(input('Please Enter 1 if you want add data Manually,'
                                   '\nOR Enter 2 if you want add data from the file:'))
        except ValueError:
            print("Wrong input")
            continue
        if first_select not in [1, 2]:
            print("Please enter correct number")
            continue
        else:
            print(first_select)
            break
    if first_select == 1:

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
            a = News(val, city)
            a.pubdays()
            a.write_news()
            print("Private News ------------------")
            print(f"{a.i}\n{a.z},{a.pubdays()}")

        if val == 2:
            val = str(input("Type your Advertisement text here: "))
            while True:
                due_date = str(input("Type Ad due date here(mm/dd/yyyy): "))
                try:
                    due_date = datetime.strptime(due_date, '%m/%d/%Y').date()
                    break
                except ValueError:
                    print("This is not in the right format")

            ad = Advertisement(val, due_date)
            ad.count_days()
            ad.write_ads()
            print(f"\n\nPrivate Ad ------------------\n{ad.i}.\nActual until: {due_date}, {ad.count_days()} days left")

        if val == 3:
            val = str(input("Share your funny mood with us here: "))

            jk = Jokes(val)
            jk.write_joke()

            print(f"\n\nJoke of the day -------------\n{jk.i}.\n{jk.j}")

    if first_select == 2:
        print("The following text added to the file:\n")
        input_from_file = FromFileToFile()
        input_from_file.input_from_file()

if __name__ == '__main__':
    main()