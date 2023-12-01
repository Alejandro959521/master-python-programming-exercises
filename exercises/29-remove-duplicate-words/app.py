
# s = input()
# words = [word.strip() for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))
# print(set(words))
# print(list(set(words)))

def remove_duplicate_words(s):
    words = [word.strip() for word in s.split(" ")]
    return (" ".join(sorted(list(set(words)))))

text=input()
print(remove_duplicate_words(text))