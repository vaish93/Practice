sentence = "vaishu is is a tester tester"

words = sentence.split(" ")

result = []

for word in words:
    if word in result:
        pass
    else:
        result.append(word)

print(result)
print(" ".join(result))