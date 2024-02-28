from googletrans import Translator
import streamlit as st
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def main():
    st.title("Multi-Language Translator")
    text = st.text_input("Enter the text to translate")
    source_lang = st.text_input("Enter the source language (leave empty for auto-detection)")
    target_lang = st.text_input("Enter the target language: ")
    if st.button("Translate"):
        if not source_lang:
            source_lang = 'auto'

        translated_text = translate_text(text, target_lang)
        speak(translated_text)
        st.success({translated_text})

if __name__ == "__main__":
    main()
