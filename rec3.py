text=input("Enter the text:")
w=text.split()
for word in w:
    print(word,":",w.count(word))