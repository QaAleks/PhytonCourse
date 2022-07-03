from datetime import datetime
from ht_classes import News, Jokes, Advertisement, FromFileToFile, WordsCount, FromJson, FromXML

from collections import Counter
import csv


def main():
    while True:
        try:
            first_select = int(input('Please Enter 1 if you want add data Manually,'
                                   '\nEnter 2 if you want add data from the file'
                                   '\nEnter 3 if you want to analize .csv file:'
                                   '\nEnter 4 if you want to load .json file:'
                                    '\nEnter 5 if you want to load .xml file:'))
        except ValueError:
            print("Wrong input")
            continue
        if first_select not in [1, 2, 3, 4, 5]:
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

    if first_select == 4:
        read_from_json = FromJson()
        read_from_json.read_from_json()

    if first_select == 5:
        read_from_xml = FromXML()
        read_from_xml.read_from_xml()





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