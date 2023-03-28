import string

caption = input("Enter a caption: ")
caption = list(caption)
updated = ""
if caption[len(caption)-1] == '?' or caption[len(caption)-1] == '!':
    pass
elif caption[len(caption)-1] == ',':
    caption[len(caption)-1] = '.'
elif caption[len(caption)-1] == '.':
    if caption[len(caption)-2] == '.':
        if caption[len(caption)-3] != '.':
            caption.pop()

for letter in caption:
    updated += letter

print(f"Caption is {updated}")