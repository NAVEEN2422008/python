def countWordFromFile():
    FileName=input("Enter the File name")
    f=open(FileName,'r')
    numberOfWords=0
    for line in f :
        word=line.split()
        numberOfWords=numberOfWords+len(word)
        print("Number of words =")
        print(numberOfWords)
        
countWordFromFile()

