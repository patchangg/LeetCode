
def findAndReplacePattern(words, pattern):
    b = pattern
    def is_iso(a):
        return len(set(a)) == len(set(b)) == len(set(zip(a, b)))
    output = filter(is_iso, words)
    return output


# set b = pattern so we can use it in the inner function
# set turns the word into a list containing the characters in word with no duplicates
# e.g abb = [a,b] so we find any words in words that is similar e.g "mee" = [m,e]
# since they are the same thats mean they have the same pattern,so return it
# Filter checks if that is true, if true append to a true list

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
farp = findAndReplacePattern(words,pattern)
print(farp)
