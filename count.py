s='this is python class at 9:25 AM'

vowels=0
consonants=0
digit=0
whitespace=0

for p in s:
    if p.lower() in ['a','e','i','o','u']:
       vowels+=1

    elif p.isalpha():
         consonants+=1
    elif p.isdigit():
         digit+=1
    elif p in [' ','\t','\n']:
         whitespace+=1

print('number is whitespace',whitespace)
print('number is vowels',vowels)
print('number is consonants',consonants)
print('number is digit',digit)
