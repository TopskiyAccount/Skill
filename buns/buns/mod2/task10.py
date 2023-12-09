input_str = input()
words = input_str.split()

result = ""
for word in words:
    if len(word) > 0:
        result += word[-1]

print(result)
