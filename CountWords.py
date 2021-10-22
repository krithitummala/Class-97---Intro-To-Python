intro = input("Enter your introduction :")
print(intro)
characterCount = 0
wordCount = 1
for i in intro:
    characterCount = characterCount+1
    if(i == " "):
        wordCount = wordCount+1
print("characterCount is")
print(characterCount)
print("Word Count is" + str(wordCount))