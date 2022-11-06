from collections import Counter

def canConstruct(ransomNote, magazine):
    mc = Counter(magazine)
    rc = Counter(ransomNote)
    for c, count in rc.items():
        if count > mc[c]:
            return False
    return True

ransomNote = "a"
magazine = "b"
noteInMagazine = canConstruct(ransomNote,magazine)
print(noteInMagazine)
