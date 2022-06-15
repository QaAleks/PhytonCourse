from datetime import datetime
from collections import Counter
import csv


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
        f = open(r"C:\WORK\Test.txt", "a")
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
        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nAdvertisement-------------------------\n{self.i}.\n{self.w},{self.count_days()}")
        f.close()


class Jokes(Publishing):

    def __init__(self, text_joke, default_ending="Stay tuned for our next jokes"):
        Publishing.__init__(self, text=text_joke)
        self.j = default_ending

    def write_joke(self):
        f = open(r"C:\WORK\Test.txt", "a")
        f.write(f"\n\nJoke of the day -------------\n{self.i}.\n{self.j}")
        f.close()

class FromFileToFile :

    def input_from_file(self):
        with open("C:\WORK\input_text.txt", "r") as source_file, open(r"C:\WORK\Test.txt", "a") as input_text:
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

class WordsCount :

    def count_words_in_file(self, all_words=[]):
        with open('count_words.csv', 'w') as count_csv_file:
            file_for_count_w = open(r"Test.txt", "r")
            read_data = file_for_count_w.read().lower().split()
            # counts = str(Counter(read_data))
            # counts = ''.join(Counter(map(str, read_data)).elements())
            # counts = Counter(read_data)
            # json_object = json.dumps(counts, indent='\n')
            for i in read_data:
                read_data.count(i)
                all_words.append(f'{i} - {read_data.count(i)}')

            writer = csv.writer(count_csv_file, delimiter='\n')
            writer.writerow(all_words)
            print(all_words)
            # writer.writerow(json_object)


    def other_measures(self, list_number_letter=[], list_letter_count=[], list_persentage: object = []):
        with open('other_measures.csv', 'w') as measures_csv:
            file_for_count_w = open(r"Test.txt", "r")
            read_data = file_for_count_w.read()
            # writer.writerow({'letter': 'A', 'count_all': '15', 'count_uppercase': '8', 'percentage': '12'})
            # print(read_data)
            all_letter = ''
            for rd in read_data:
                for p in rd:
                    if rd.isalpha():
                        all_letter += p
            print(all_letter)

            count_all_letter = len(all_letter)
            print(count_all_letter)

            count_uppercase = 0
            for i in all_letter:
                cnt = all_letter.count(i)
                if i.isupper():
                    count_uppercase += 1
                list_number_letter.append(i)
                list_letter_count.append(cnt)
                prst_rnd = round(cnt / count_all_letter * 100,2)
                list_persentage.append(prst_rnd)

            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(measures_csv, fieldnames=headers, delimiter=';')
            writer.writeheader()
            writer.writerow({'letter': list_number_letter, 'count_all': list_letter_count, 'count_uppercase':count_uppercase, 'percentage': list_persentage})

def main():
    while True:
        try:
            first_select=int(input('Please Enter 1 if you want add data Manually,'
                                   '\nEnter 2 if you want add data from the file'
                                   '\nEnter 3 if you want to analize .csv file:'))
        except ValueError:
            print("Wrong input")
            continue
        if first_select not in [1, 2, 3]:
            print("Please enter correct number")
            continue
        else:
            # print(first_select)
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

    if first_select == 3:
        count_words_in_file = WordsCount()
        count_words_in_file.count_words_in_file()
        other_measures = WordsCount()
        other_measures.other_measures()



        # # def count_words (self):
        # file_for_count_w = open(r"Test.txt", "r")
        # read_data = file_for_count_w.read()
        # per_word = read_data.split()
        # # print(per_word)
        # print('Total Words:', len(per_word))


        # from collections import Counter
        # words = []
        #
        # load words to list
        # with open(r"Test.txt", "r") as fp:
        #     per_word = fp.split()
        #     for line in per_word:
        #         if line != ' ':
        #             words.append(line.lower().rstrip())
        #
        # make a dictionary from the 'words' list
        # cnt = Counter(words)

        # print out the key, value pairs
        # for k, v in cnt.items():
        #     print('the count of ' + k + ' is: ' + str(v))



if __name__ == '__main__':
    main()