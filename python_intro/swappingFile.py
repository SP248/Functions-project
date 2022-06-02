def swapFileData():
    file1 = input("Enter first file name")
    file2 = input("Enter second file name")
    file_1 = open(file1)
    file_2 = open(file2)

    data_a = file_1.read()
    data_b = file_2.read()

    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)
        
swapFileData()
    
