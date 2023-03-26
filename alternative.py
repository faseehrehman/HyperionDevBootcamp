s = ("Hello World")
new_s = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))
print(new_s)


original = ("I am learning to code")

words = original.split()

alternating_words = [word.lower() if i % 2 != 0 else word.upper() for i, word in enumerate(words)]

#Join the string together

result = " ".join(alternating_words)

print(result)