message=input("Describe yourself:")
print(message)
wordCount=1
count=0
for i in message:
    print(i)
    count=count+1
    
    if(i==" "):
        wordCount=wordCount+1
print("totalCharacters=",count)
print("totalWords=",wordCount)