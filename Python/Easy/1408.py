
def stringMatching(words):
    output = []
    for word in words:
        for w in words:
            if word != w and word in w:
                output.append(word)
    return set(output)

words = ["mass","as","hero","superhero"]
subStrings = stringMatching(words)
print(subStrings)
