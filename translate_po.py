import os
import subprocess
from deep_translator import GoogleTranslator

SUPPORTED_LOCALES = ['ko', 'ja', 'zh_Hans', 'zh_Hant', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ru', 'tr', 'id', 'vi', 'th']

# Map Babel locale to deep_translator language codes
LANG_MAP = {
    'ko': 'ko',
    'ja': 'ja',
    'zh_Hans': 'zh-CN',
    'zh_Hant': 'zh-TW',
    'es': 'es',
    'fr': 'fr',
    'de': 'de',
    'it': 'it',
    'pt': 'pt',
    'ar': 'ar',
    'hi': 'hi',
    'ru': 'ru',
    'tr': 'tr',
    'id': 'id',
    'vi': 'vi',
    'th': 'th'
}

def init_locale(locale):
    print(f"Initializing {locale}...")
    subprocess.run(["pybabel", "init", "-i", "messages.pot", "-d", "translations", "-l", locale], check=False)

def translate_po(locale):
    po_file = os.path.join('translations', locale, 'LC_MESSAGES', 'messages.po')
    if not os.path.exists(po_file):
        return

    print(f"Translating {po_file} to {locale}...")
    target_lang = LANG_MAP.get(locale, locale)
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
    except Exception as e:
        print(f"Skipping {locale} due to translator setup error: {e}")
        return

    with open(po_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    msgid = ""
    in_msgid = False
    in_msgstr = False
    
    for line in lines:
        if line.startswith('msgid '):
            msgid = line[7:-2] # remove msgid "" and newline
            out_lines.append(line)
            in_msgid = True
            in_msgstr = False
        elif line.startswith('msgstr '):
            in_msgid = False
            in_msgstr = True
            
            # If there's an actual message ID to translate
            if msgid and msgid != "":
                try:
                    translated = translator.translate(msgid)
                    out_lines.append(f'msgstr "{translated}"\n')
                except Exception as e:
                    print(f"Failed translating: {msgid} - {e}")
                    out_lines.append(line)
            else:
                out_lines.append(line)
        else:
            out_lines.append(line)

    with open(po_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

if __name__ == "__main__":
    for loc in SUPPORTED_LOCALES:
        init_locale(loc)
        translate_po(loc)
    print("Translation complete!")
