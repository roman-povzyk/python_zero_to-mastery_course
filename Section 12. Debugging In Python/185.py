from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('text.txt', 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('text_ja.txt', 'w') as file:
            file.write(translation)
except FileExistsError as e:
    print('check your file path')
