

def main():
    name=str(input("Enter the File name: "))
    f=open(name,'r')
    text=f.read()
    print(text)
    words=text.split()
    print(words)


    counts=dict()
    for word in words:
        print(word)
        count+=1
    print(count)
    #bigcount=None
    #bigword=None

    #for word.count in count.items():
    #    if bigcount is None or count > bigcount:
     #       bigword=word
     #       bigcount=count
    # print(bigcount,bigword)


main()