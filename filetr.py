# filetr.py

from translator.first_module import Translate
from configparser import ConfigParser

def read_config(config_file):
    config = ConfigParser()
    config.read(config_file)
    file_name = config.get('FileInfo', 'FileName')
    dest_lang = config.get('TranslationInfo', 'DestinationLanguage')
    output_option = config.get('TranslationInfo', 'OutputOption')
    char_limit = config.getint('TextLimit', 'CharacterLimit')
    word_limit = config.getint('TextLimit', 'WordLimit')
    sentence_limit = config.getint('TextLimit', 'SentenceLimit')
    return file_name, dest_lang, output_option, char_limit, word_limit, sentence_limit

def translate_file(file_name, dest_lang, output_option, char_limit, word_limit, sentence_limit):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            # Check text limits
            if len(text) > char_limit or len(text.split()) > word_limit or text.count('.') > sentence_limit:
                return "Перевищено ліміт тексту"
            else:
                translation = Translate(text, 'auto', dest_lang)
                if output_option == 'file':
                    with open('translated_text.txt', 'w', encoding='utf-8') as translated_file:
                        translated_file.write(translation)
                    return "Ok"
                elif output_option == 'screen':
                    print(translation)
                    return "Ok"
                else:
                    return "Неправильний варіант виводу"
    except Exception as e:
        return str(e)

def main():
    try:
        file_name, dest_lang, output_option, char_limit, word_limit, sentence_limit = read_config('config.ini')
        result = translate_file(file_name, dest_lang, output_option, char_limit, word_limit, sentence_limit)
        print(result)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
