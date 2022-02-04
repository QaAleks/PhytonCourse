import re
import string
old_text ="""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
count=0
for i in old_text:
#find out whitespace
# or we may use: if (i.isspace()):
   if   i==' ' or i=='\n' or i=='\t':
      count=count+1
print('Count of Whitespace in default text is:',count)
#make all text lowercase
low_case=old_text.lower()
#make first word capitalize
cap_first_char= low_case.capitalize()
#replace iz to is in case it needs (not inside the words)
replace_iz = cap_first_char.replace("“iz”", " “iz”").replace(" iz ", " is ")

# make a senteces with a last words
#find out words with dots
words_with_dots = re.findall(r'\w*\.', cap_first_char)
#print(words_with_dots)
#join words with dots to make a sentence
join_words=(' '.join(words_with_dots))
#del dots inside the sentence and put dot in the end
del_dots=join_words.replace('.','')+'.'
#Capitalize first word in new sentence
cap_first_word=del_dots.capitalize()
#print(cap_first_word)


#split big text on a separate sentences
split_text= re.findall('[^.!?\t]+[.:\n\n!?](?:\s)', replace_iz)
#make first word apper in each sentence
upper_case = [k[0].upper() + k[1:] for k in split_text]
#help step to make a list for merge
cap_first_word = cap_first_word.split(".")
#put sentence in a correct plase
correct_place = upper_case[0:][:5] + ["\n\t"] + cap_first_word[0:][:1] + [". "] + ["\n\n\t"] + upper_case[5:]

#collect all sentenses to a final text
final_text= ''.join(correct_place)
print(final_text)

