f =open("./user_records.txt")
data = f.readlines()
print(data)
f.close()


import re              #firstname   lastname    age      country
# pattern = re.compile('([A-Za-z]+)\s([A-Za-z]+), (\d+), ([A-Za-z ]+)')
pattern = re.compile('(\d+), ([A-Za-z ]+)')
# the_pattern = pattern.findall(data)
# print(the_pattern)
invalid=0
valid= 0
for x in data:
    found = pattern.search(x)
    if found:
        print(f'Age: {found.group(1)}, Country: {found.group(2)}')
        valid += 1
    else:
        print(f'invalid')
        invalid +=1
        
print(f' invalid = {invalid}')
print(f' valid = {valid}')