filename = "examples.txt"
palindrome_file = "palindromes.txt"
non_palindrome_file = "non_palindrome.txt"
punctuation = " .,'?"

open(palindrome_file, "w")
open(non_palindrome_file, "w")
#1 we need to open the file and start reading line by line

with open(filename) as fp:
    #2 read line by line
    for line in fp:
        # save the original line
        orig_line = line.rstrip()
        #print(line)
        #need to sanitize the line by removing punctuation
        line = line.lower()
        #use a fot to go one by one in punctuation and replace with ""
        for p in punctuation:
            line = line.replace(p, "")
        line = line.rstrip() #this removed the enter at the end
        # check if palindrome
        if line == line [::-1]:
            print(f"{orig_line} is a palindrome")
            with open(palindrome_file, "w") as palindrome_fp:
                palindrome_fp.write(f"{orig_line}\n")
        else:
            print(f"{orig_line} is not a palindrome")
            with open(non_palindrome_file, "w") as non_palindrome_fp:
                non_palindrome_fp.write(f"{orig_line}\n")
        print(line)

