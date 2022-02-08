import re
import string

old_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

def count_whitespaces(input_text):
    count_s = 0
    for i in input_text:
        if i==' ' or i=='\n' or i=='\t':
            count_s=count_s+1
    return count_s
print('Count of Whitespace in default text is:',count_whitespaces(old_text))

def work_with_txt(text_t):
    low_case = old_text.lower()
    cap_first_char = low_case.capitalize()
    replace_iz = cap_first_char.replace("“iz”", " “iz”").replace(" iz ", " is ")

    words_with_dots = re.findall(r'\w*\.', cap_first_char)
    join_words = (' '.join(words_with_dots))
    del_dots = join_words.replace('.', '') + '.'
    cap_first_word = del_dots.capitalize()

    split_text = re.findall('[^.!?\t]+[.:\n\n!?](?:\s)', replace_iz)
    upper_case = [k[0].upper() + k[1:] for k in split_text]
    cap_first_word = cap_first_word.split(".")
    correct_place = upper_case[0:][:5] + ["\n\t"] + cap_first_word[0:][:1] + [". "] + ["\n\n\t"] + upper_case[5:]

    # collect all sentenses to a final text
    return ''.join(correct_place)

print(work_with_txt(old_text))