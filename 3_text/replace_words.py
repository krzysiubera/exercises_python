file_path = "text_files/sample.txt"
replaced_words = {
    'and': 'or',
    'never': 'always',
    'why': 'whose'
}

with open(file_path, 'r') as in_file:
    input_text = in_file.read()

new_text_words = []
for word in input_text.split():
    if word in replaced_words.keys():
        new_text_words.append(replaced_words[word])
    else:
        new_text_words.append(word)

result = " ".join(new_text_words)
print(result)
