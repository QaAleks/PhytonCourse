import json
from datetime import datetime
import csv
import xml.etree.ElementTree as ET
import sqlite3

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


class FromFileToFile:

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


class WordsCount:

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
            # k = set(all_letter)
            # print(k)

            count_all_letter = len(all_letter)
            # print(count_all_letter)

            count_uppercase = 0
            for i in all_letter:
                cnt = all_letter.count(i)
                if i.isupper():
                    count_uppercase += 1
                list_number_letter.append(i)
                list_letter_count.append(cnt)
                prst_rnd = round(cnt / count_all_letter * 100, 2)
                list_persentage.append(prst_rnd)

            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(measures_csv, fieldnames=headers, delimiter=';')
            writer.writeheader()
            writer.writerow(
                {'letter': list_number_letter, 'count_all': list_letter_count, 'count_uppercase': count_uppercase,
                 'percentage': list_persentage})


class FromJson:
    def read_from_json(self):
        with open(r"Test.txt", "a") as input_text: #open('json_file.json', 'r') as j,
            # a = j.read()
            conv_to_dict = json.load(open('json_file.json'))
            for y in range(len(conv_to_dict)):
                try:
                    if conv_to_dict[y]["type"].lower() == "news":
                        # type = conv_to_dict['type']
                        text = conv_to_dict[y]['text']
                        city = conv_to_dict[y]['location']
                        n = News(text_news=text, city=city)
                        n.write_news()
                        # print(n)
                    elif conv_to_dict[y]['type'].lower() == 'joke':
                        text = conv_to_dict[y]['text']
                        n = Jokes(text_joke=text)
                        n.write_joke()
                    elif conv_to_dict[y]['type'].lower() == 'advertisement':
                        text = conv_to_dict[y]['text']
                        f_date = conv_to_dict[y]['future_date']
                        ff_date = datetime.strptime(f_date,"%Y-%m-%d")
                        ff_date = ff_date.date()
                        n = Advertisement(text_ad=text, future_date=ff_date)
                        n.write_ads()

                    # else:
                    #     print("Sorry, it is not correct data in the file")
                except:
                    print("Sorry, I didn't understand that.")

            print(conv_to_dict)

class FromXML:
    def read_from_xml(self):
        with open(r"Test.txt", "a") as input_text:
            get_tree = ET.parse('output_file.xml')
            get_root = get_tree.getroot()
            for article in get_root.findall('PublishArticle'):
                try:
                    if article.get('name').lower() == "news":
                        text = article.find('TypeData').find('Info').text
                        city = article.find('TypeData').find('Location').text
                        n = News(text_news=text, city=city)
                        n.write_news()
                    elif article.get('name').lower() == 'advertising':
                        text = article.find('TypeData').find('Adv_Info').text
                        date = article.find('TypeData').find('Adv_Date').text
                        ff_date = datetime.strptime(date, "%Y-%m-%d")
                        ff_date = ff_date.date()
                        n = Advertisement(text_ad=text, future_date=ff_date)
                        n.write_ads()
                    elif article.get('name').lower() == 'joke':
                        text = article.find('TypeData').find('Joke_Info').text
                        jk = Jokes(text_joke=text)
                        jk.write_joke()
                except:
                    print("Sorry, I didn't understand that.")

            print(get_root)

class ForDB:
    def __init__(self):
        self.connection = sqlite3.connect('test_db.db')
        self.cursor = self.connection.cursor()
        self.news = 'Some text news'
        self.location = 'Kyiv'
        self.adds = 'Some text for add'
        self.due_date = '2022-09-09'
        self.joke = 'Some text of joke'
        self.cursor.execute('create table if not exists news_table(news text, location text)')
        self.cursor.execute('create table if not exists adds_table(adds text, due_date date)')
        self.cursor.execute('create table if not exists jokes_table(joke text )')

    def insert_to_db(self):
        self.cursor.execute(f"select news from news_table where news = '{self.news}'")
        if self.cursor.fetchone() is not None: #self.news}:
            print(f'\nYou are trying to load a duplicat value for NEWS')
        else:
            self.cursor.execute(f"insert into news_table values('{self.news}','{self.location}')")

        self.cursor.execute('select * from news_table')
        a = self.cursor.fetchall()


        self.cursor.execute(f"select adds from adds_table where adds = '{self.adds}'")
        if self.cursor.fetchone() is not None:
            print(f'\nYou are trying to load a duplicat value for ADDs')
        else:
            self.cursor.execute(f"insert into adds_table values('{self.adds}','{self.due_date}')")

        self.cursor.execute('select * from adds_table')
        b = self.cursor.fetchall()


        self.cursor.execute(f"select joke from jokes_table where joke = '{self.joke}'")
        if self.cursor.fetchone() is not None:
            print(f'\nYou are trying to load a duplicat value for JOKE')
        else:
            self.cursor.execute(f"insert into jokes_table values('{self.joke}')")

        self.cursor.execute('select * from jokes_table')
        c = self.cursor.fetchall()

        return a, b, c



    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()






