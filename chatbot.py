import deepl
import os
import pandas as pd
from dotenv import load_dotenv

# Load the DeepL API key from the .env file
load_dotenv()
api_key = os.getenv("DEEPL_API_KEY")

# Initialize DeepL translator
translator = deepl.Translator(api_key)

def translate_text(text, source_lang, target_langs):
    translations = {}
    for target_lang in target_langs:
        try:
            # Translate the text using DeepL API for each target language
            result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
            translations[target_lang] = result.text
        except Exception as e:
            translations[target_lang] = f"Error: {e}"
    return translations

def detect_language(text):
    from langdetect import detect
    try:
        return detect(text)
    except Exception as e:
        return None

def chatbot():
    print("Welcome to your translation bot! Type 'exit' to end this session.")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            print("See you!")
            break
        
        # Ask if the user wants to provide the source language
        specify_source = input("Do you want to specify the source language? (yes/no): ").strip().lower()
        
        if specify_source == "yes":
            source_language = input("Enter the source language code (e.g., 'en' for English): ").strip()
        else:
            # Detect source language
            source_language = detect_language(user_message)
            if not source_language:
                print("Could not detect language. Please provide the source language code.")
                source_language = input("Enter the source language code (e.g., 'en' for English): ").strip()
        
        # Ask for multiple target languages
        target_languages = input("Enter comma-separated target language codes (e.g., 'es,fr,de'): ").split(',')
        
        # Translate the message to multiple languages
        translations = translate_text(user_message, source_language, target_languages)
        
        for lang, translation in translations.items():
            print(f"Translation to {lang}: {translation}")

if __name__ == "__main__":
    chatbot()