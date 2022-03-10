filename = "text.txt"

#the first way of reading from a file
fp = open(filename) #by default it is opened for reading
print(fp.read())
fp.close()

#second way of reading from a file
with open(filename) as fp:
    for line in fp:
        line = line.replace("\n", "")

        print(f"Line: {line}")
        #at the end, the file will be closed automatically

