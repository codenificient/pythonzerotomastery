try:
    with open('test3.txt', mode='w') as my_file:
        print(my_file.write('I forgot this was possible'))
except FileNotFoundError as err:
    print('check your file path, silly!')
    raise err



from translate import Translator
translator = Translator(to_lang='ja')

try:
    with open('test3.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print('check your file path, silly!')
    raise err