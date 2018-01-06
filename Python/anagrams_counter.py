from collections import Counter
def deletions(word1, word2):
    c_word1 = Counter(word1)
    c_word2 = Counter(word2)
    c_word1.subtract(c_word2)
    return sum(abs(i) for i in c_word1.values())
t = int(input())
while t>0:
    word1 = input()
    word2 = input()
    print(deletions(word1,word2))
    t -= 1