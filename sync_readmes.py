import os
from deep_translator import GoogleTranslator

# Mapping of file suffixes to Google Translator language codes
langs = {
    'ko': 'ko',
    'es': 'es',
    'zh_Hans': 'zh-CN',
    'zh_Hant': 'zh-TW',
    'ar': 'ar',
    'de': 'de',
    'fr': 'fr',
    'hi': 'hi',
    'id': 'id',
    'it': 'it',
    'ja': 'ja',
    'pt': 'pt',
    'ru': 'ru',
    'th': 'th',
    'tr': 'tr',
    'vi': 'vi'
}

def translate_markdown(text, target_lang):
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        chunks = text.split('\n\n')
        translated_chunks = []
        for chunk in chunks:
            if not chunk.strip():
                translated_chunks.append("")
                continue
            if chunk.startswith('```') or chunk.startswith('<div'):
                translated_chunks.append(chunk)
            elif chunk.startswith('[![') or '|----------|------|' in chunk:
                translated_chunks.append(chunk)
            else:
                translated = translator.translate(chunk)
                # Handle NoneType return
                if translated is None:
                    translated = chunk
                translated_chunks.append(translated)
        return '\n\n'.join([str(c) for c in translated_chunks if c is not None])
    except Exception as e:
        print(f"Error translating to {target_lang}: {e}")
        return text

with open('README.md', 'r', encoding='utf-8') as f:
    en_content = f.read()

parts = en_content.split('---', 1)
top_html = parts[0] + '---\n\n'
body_text = parts[1].strip()

for suffix, lang_code in langs.items():
    print(f"Translating for {suffix} ({lang_code})...")
    translated_body = translate_markdown(body_text, lang_code)
    
    final_content = top_html + translated_body
    final_content = final_content.replace('] (', '](').replace('] ( ', '](')
    final_content = final_content.replace('** ', '**').replace(' **', '**')
    
    filename = f'README.{suffix}.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Updated {filename}")

print("All localized READMEs updated.")
