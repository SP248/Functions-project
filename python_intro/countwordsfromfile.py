def countwordsfromfile():
    filename = input("Enter the Filename")
    numberofwords = 0
    file = open(filename,"r")
    for i in file:
        words = i.split()
        numberofwords = numberofwords+len(words)
    print("numberofwords")
    print(numberofwords)
countwordsfromfile()