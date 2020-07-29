def interleave(s1, s2):
    return ''.join([''.join(list(n)) for n in  zip(s1,s2)])
print(interleave("hi","ha"))

def triple_and_filter(lis):
    return [x**3 for x in filter(lambda x: x%4==0,lis)]


'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(lis):
    return [' '.join([item['first'],item['last']]) for item in lis]