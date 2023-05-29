from googletrans import Translator
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'ne pas donner de clés'

@app.route("/translate_lang", methods=["POST"])
def translate_lang():
    if request.method == "POST":
        sentence = str(request.form["sentence"])
        code = str(request.form["code"])

        translator = Translator()
        translated_sentence = translator.translate(sentence, src="fr", dest=code)
        translated = translated_sentence.text

        return render_template("index2.html", language_selected=code, sentence=sentence, translated_res=translated)
    

@app.route("/reset_translation", methods=["POST"])
def reset_translation():
    return render_template("index2.html")


@app.route("/")
def index():
    lang = [
        {"name": "Afrikaans", "code": "af"},
        {"name": "Amharique", "code": "am"},
        {"name": "Arabe", "code": "ar"},
        {"name": "Basque", "code": "eu"},
        {"name": "Bengali", "code": "bn"},
        {"name": "Anglais (Royaume-Uni)", "code": "en-GB"},
        {"name": "Portugais (Brésil)", "code": "pt-BR"},
        {"name": "Bulgare", "code": "bg"},
        {"name": "Catalan", "code": "ca"},
        {"name": "Cherokee", "code": "chr"},
        {"name": "Croate", "code": "hr"},
        {"name": "Tchèque", "code": "cs"},
        {"name": "Danois", "code": "da"},
        {"name": "Néerlandais", "code": "nl"},
        {"name": "Anglais (États-Unis)", "code": "en"},
        {"name": "Estonien", "code": "et"},
        {"name": "Tagalog", "code": "fil"},
        {"name": "Finnois", "code": "fi"},
        {"name": "Français", "code": "fr"},
        {"name": "Allemand", "code": "de"},
        {"name": "Grec", "code": "el"},
        {"name": "Gujarati", "code": "gu"},
        {"name": "Hébreu", "code": "iw"},
        {"name": "Hindi", "code": "hi"},
        {"name": "Hongrois", "code": "hu"},
        {"name": "Islandais", "code": "is"},
        {"name": "Indonésien", "code": "id"},
        {"name": "Italien", "code": "it"},
        {"name": "Japonais", "code": "ja"},
        {"name": "Kannada", "code": "kn"},
        {"name": "Coréen", "code": "ko"},
        {"name": "Letton", "code": "lv"},
        {"name": "Lituanien", "code": "lt"},
        {"name": "Malaisien", "code": "ms"},
        {"name": "Malayâlam", "code": "ml"},
        {"name": "Marathi", "code": "mr"},
        {"name": "Norvégien", "code": "no"},
        {"name": "Polonais", "code": "pl"},
        {"name": "Portugais (Portugal)", "code": "pt-PT"},
        {"name": "Roumain", "code": "ro"},
        {"name": "Russe", "code": "ru"},
        {"name": "Serbe", "code": "sr"},
        {"name": "Chinois (RPC)", "code": "zh-CN"},
        {"name": "Slovaque", "code": "sk"},
        {"name": "Slovène", "code": "sl"},
        {"name": "Espagnol", "code": "es"},
        {"name": "Swahili", "code": "sw"},
        {"name": "Suédois", "code": "sv"},
        {"name": "Tamoul", "code": "ta"},
        {"name": "Télougou", "code": "te"},
        {"name": "Thaï", "code": "th"},
        {"name": "Chinois (Taïwan)", "code": "zh-TW"},
        {"name": "Turc", "code": "tr"},
        {"name": "Urdu", "code": "ur"},
        {"name": "Ukrainien", "code": "uk"},
        {"name": "Vietnamien", "code": "vi"},
        {"name": "Gallois", "code": "cy"}
    ]

    return render_template("index2.html", languages=lang)

if __name__ == "__main__":
    app.run(debug=True)
