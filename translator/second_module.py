from deep_translator import GoogleTranslator
from langdetect import detect

def Translate(text: str, src: str, dest: str) -> str:
    try:
        translated_text = GoogleTranslator(source=src, target=dest).translate(text)
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str) -> str:
    try:
        lang = detect(text)
        return lang
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang_codes = {
        "Ukrainian": "uk",
    }
    if lang in lang_codes:
        return lang_codes[lang]
    elif lang in lang_codes.values():
        return next(key for key, value in lang_codes.items() if value == lang)
    else:
        return "Невірна мова"

def LanguageList(out: str, text: str) -> str:
    if out == "screen":
        # Виведення таблиці на екран
        table_header = f"{'N':<4} {'Language':<15} {'ISO-639 code':<10} {'Text':<30}"
        separator = "-" * len(table_header)
        print(separator)
        print(table_header)
        print(separator)
        # Можна також використовувати перебір словника lang_codes для виведення всіх мов
        languages = [
            ("Ukrainian", "uk"),
        ]
        for index, (language, code) in enumerate(languages, start=1):
            translated_text = Translate(text, "en", code)
            print(f"{index:<4} {language:<15} {code:<10} {translated_text[:30]:<30}")
        return "Ok"
    elif out == "file":
        try:
            with open("language_list.txt", "w") as file:
                table_header = f"{'N':<4} {'Language':<15} {'ISO-639 code':<10} {'Text':<30}\n"
                file.write(table_header)
                separator = "-" * len(table_header)
                file.write(separator + "\n")
                languages = [
                    ("Ukrainian", "uk"),
                ]
                for index, (language, code) in enumerate(languages, start=1):
                    translated_text = Translate(text, "en", code)
                    line = f"{index:<4} {language:<15} {code:<10} {translated_text[:30]:<30}\n"
                    file.write(line)
            return "Ok"
        except Exception as e:
            return str(e)
    else:
        return "Неправильний варіант виводу"
