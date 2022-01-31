from random import randint, choice
from string import ascii_lowercase
#create dictionary with random list using random library and method randint
#generate id's as letters using string library
rnd_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 3))]
print(rnd_list)

result_dict, tmp_dict = {}, {}
for dictionary in rnd_list:
 # assign each id particaular values from dict
  for k, m in dictionary.items():
    tmp_dict.setdefault(k, []).append(m)

# Define the biggest values from all dict if ids are duplicated in several dict
for k, m in tmp_dict.items():
  if len(m) > 1:
    result_dict[k+"_"+str(m.index(max(m))+1)] = max(m)
# if id is distinct (not duplicated), print it without '_index dict'
  else: result_dict[k] = m[0]

print(result_dict)