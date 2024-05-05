from translator.first_module import Translate, LangDetect, CodeLang, LanguageList

def main():
    print("Переклад тексту:")
    text = input("Введіть текст для перекладу: ")
    src_lang = input("Введіть мову тексту (ISO-639 code): ")
    dest_lang = input("Введіть мову для перекладу (ISO-639 code): ")
    translation = Translate(text, src_lang, dest_lang)
    print(f"Переклад: {translation}")

    print("\nВизначити мову:")
    text_to_detect = input("Введіть текст, щоб визначити мову: ")
    set_option = input("Введіть встановлений параметр (lang/confidence/all): ")
    detected_lang = LangDetect(text_to_detect, set_option)
    print(f"Мова: {detected_lang}")

if __name__ == "__main__":
    main()
