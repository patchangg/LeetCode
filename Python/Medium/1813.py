from collections import deque

def areSentencesSimilar(sentence1, sentence2):
    s1 = deque(sentence1.split())
    s2 = deque(sentence2.split())
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    while s1 and s1[0] == s2[0]:
        s1.popleft()
        s2.popleft()
    while s1 and s1[-1] == s2[-1]:
        s1.pop()
        s2.pop()
    return not s1

# Split both sentences and put them into a deque.
# Check if the prefix and suffix of the shortest sentence can be found in the
# prefix and suffix of the longer setence to see if they are similar.
# O(1), O(n) space
sentence1 = "My name is Haley"
sentence2 = "My Haley"
areSimilar = areSentencesSimilar(sentence1,sentence2)
print(areSimilar)
