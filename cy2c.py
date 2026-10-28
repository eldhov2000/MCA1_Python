word=input("Enter word:")
vowels=['a','e','i','o','u']
list=[]
for x in word:
    if(x in vowels and x not in list):
     list.append(x)
print("vowels present in the given word is:",list)