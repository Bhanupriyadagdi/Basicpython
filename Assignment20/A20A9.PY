#===WAPP to create a function to check whether a string is a pangram or not:
def pangram(s):
    for e in range(97,123):
        if chr(e) not in s:
            print("given string is not pangram",chr(e))
            break
    else:
        print("given string is pangram")


pangram("The quick brown fox jumps over the lazy dog")



