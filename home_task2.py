from random import randint, choice
from string import ascii_lowercase
#create dictionary with random list using random library and method randint
#generate id's as letters using string library
rnd_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(randint(0,len(ascii_lowercase)))} for j in range(randint(2, 3))]
print(rnd_list)

# define two additional dict
result_dict, tmp_dict = {}, {}
for dictionary in rnd_list:
# assign each id (letter) particular values from dict
  for k, m in dictionary.items():
#setdefault() method returns the value of a key from dictionary
#using append() method to  adds a single item to existing id (e.g. k:'g' m:[12])
    tmp_dict.setdefault(k, []).append(m)

# work with temp dict to find out the biggest values from all dict if ids are duplicated in several dict
for k, m in tmp_dict.items():
# find out if values 'm' for id 'k' more than one
  if len(m) > 1:
# add '_' for duplicated id (according the task choose max value for duplicated ID) and also add +1 for index of list because countig begining from the zero
    result_dict[k+"_"+str(m.index(max(m))+1)] = max(m)
# if id is distinct (not duplicated), print result without '_index dict'
  else: result_dict[k] = m[0]
#print result dict
print(result_dict)