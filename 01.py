words = input()
i = 0
for word in words.split("%"):
    lucky_word = set(word)
    if len(lucky_word & set("nohtyP")) <= 2:
        i += 1
print(i)