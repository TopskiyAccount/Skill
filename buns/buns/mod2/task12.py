input_str = input()
cleaned_str = ""
for char in input_str:
           if char.isdigit() or char == "+":
                cleaned_str += char
print(cleaned_str)
