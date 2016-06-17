import re, csv, collections

# http://norvig.com/spell-correct.html
# https://en.wikipedia.org/wiki/2016_Summer_Olympics_Parade_of_Nations
# https://en.wikipedia.org/wiki/Comparison_of_IOC,_FIFA,_and_ISO_3166_country_codes

from data import reversed_national_olympic_committees
country_names = list(reversed_national_olympic_committees.keys())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(country_names)
alphabet = 'abcdefghijklmnopqrstuvwxyz' # TODO: deal with unicode / diacritics

def edits1(word):
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or    known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def root():
    return ("<pre>"
                "Example Usage: /russssia \n"
                "Example Usage: /azerbyejan \n"
            "</pre>")

@app.route("/<country_input>")
def hello(country_input=None):
    country_output = correct(country_input)
    try:
        country_code = reversed_national_olympic_committees[country_output]
    except KeyError as e:
        return jsonify({"error": "%s not found" % country_output})
    return jsonify({"country": country_output, "code": country_code})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
