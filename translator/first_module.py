from googletrans import Translator

def Translate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str) -> str:
    translator = Translator()
    try:
        lang = translator.detect(text)
        if set == "lang":
            return lang.lang
        elif set == "confidence":
            return str(lang.confidence)
        else:
            return f"Мова: {lang.lang}, Достовірність: {lang.confidence}"
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
        table_header = f"{'N':<4} {'Language':<15} {'ISO-639 code':<10} {'Text':<30}"
        separator = "-" * len(table_header)
        print(separator)
        print(table_header)
        print(separator)
        languages = [
            ("Ukrainian", "uk"),
        ]
        for index, (language, code) in enumerate(languages, start=1):
            translated_text = Translate(text, "en", code)
            print(f"{index:<4} {language:<15} {code:<10} {translated_text[:30]:<30}")
        return "Ok"
    elif out == "file":
        return "Ok"
    else:
        return "Неправильний варіант виводу"
