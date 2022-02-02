import re
import string
old_text ="""homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ“ with correct “is“, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

count=0
for i in old_text:
   if  i==' ' or i=='\n' or i=='\t':
      count=count+1
print('Count of Whitespace in default text is:',count)
#for cng_quotes in old_text:
#    old_text.replace('“', '"')
cng_quotes=old_text.replace('“','"')
low_case=cng_quotes.lower()
cap_first_char= low_case.capitalize()
#
last = re.split(r'[\s]', cap_first_char)  # list of words
# result = re.findall(r'\w*',cap_first_char)
print(' '.join('\b*\.\b',last))



# lst_words = re.search(r'\w+\.', last)
#print(last)
# print(lst_words)

