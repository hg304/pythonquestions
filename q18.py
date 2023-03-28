text = input("Enter a name: ")
formatted = ""

for i in range(len(text)):
    if text[i] == " ":
        if i == len(text)-1:
            break
        if text[i+1] != " " and text[i-1] != " ":
            formatted += text[i]
    else:
        formatted += text[i]

print(formatted)