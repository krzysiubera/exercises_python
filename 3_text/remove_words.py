file_path = "text_files/sample.txt"
words_to_remove = ['and', 'never', 'why']

with open(file_path, 'r') as in_file:
    input_text = in_file.read()

input_words = input_text.split()
new_words = [word for word in input_words if word not in words_to_remove]
new_text = " ".join(new_words)
print(new_text)
