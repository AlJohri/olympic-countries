import re, csv, collections

# http://norvig.com/spell-correct.html
# https://en.wikipedia.org/wiki/2016_Summer_Olympics_Parade_of_Nations
# https://en.wikipedia.org/wiki/Comparison_of_IOC,_FIFA,_and_ISO_3166_country_codes

from data import reversed_national_olympic_committees, national_olympic_committees
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
    word = word.lower().replace(".", "")
    if len(word) == 3 or word in ['us', 'uk']:
        candidates = known([word])
    elif len(word) <= 2:
        raise Exception("too short")
    else:
        candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]

    if len(candidates) == 0:
        raise Exception("no candidates found for %s" % word)
    return max(candidates, key=NWORDS.get)

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def root():
    return ("<pre>"
                "Example Usage:\n\n"
                    "\t" + request.url.rstrip("/") + "/russssia\n"
                    "\t" + request.url.rstrip("/") + "/azerbyejan\n"
                    "\t" + request.url.rstrip("/") + "/refuugeee\n"
                    "\t" + request.url.rstrip("/") + "/amurica\n"
                    "\t" + request.url.rstrip("/") + "/amerika\n"
                    "\t" + request.url.rstrip("/") + "/us\n"
                    "\t" + request.url.rstrip("/") + "/uk\n"
                    "\t" + request.url.rstrip("/") + "/usa\n"
                    "\t" + request.url.rstrip("/") + "/u.s.a.\n"
                    "\t" + request.url.rstrip("/") + "/britain\n"
                    "\t" + request.url.rstrip("/") + "/great%20britain\n"
                    "\t" + request.url.rstrip("/") + "/russssia\n"
                    "\t" + request.url.rstrip("/") + "/azerbyejan\n"
                    "\t" + request.url.rstrip("/") + "/kazakstan\n"
                    "\t" + request.url.rstrip("/") + "/kazakistan\n"
                    "\t" + request.url.rstrip("/") + "/kergizstan\n"
                    "\t" + request.url.rstrip("/") + "/kirgystan\n"
                    "\t" + request.url.rstrip("/") + "/tajeekistan\n"
                    "\t" + request.url.rstrip("/") + "/leechtenstein\n"
                    "\t" + request.url.rstrip("/") + "/germaany\n"
                    "\t" + request.url.rstrip("/") + "/germiny\n"
                    "\t" + request.url.rstrip("/") + "/leethuania\n"
                    "\t" + request.url.rstrip("/") + "/lithiania\n"
                    "\t" + request.url.rstrip("/") + "/lithuany\n"
                    "\t" + request.url.rstrip("/") + "/keeribati\n"
                    "\t" + request.url.rstrip("/") + "/kireebati\n"
                    "\t" + request.url.rstrip("/") + "/kiribeti\n"
                    "\t" + request.url.rstrip("/") + "/maldivees\n"
                    "\t" + request.url.rstrip("/") + "/laos\n"
                    "\t" + request.url.rstrip("/") + "/trinidad\n"
                    "\t" + request.url.rstrip("/") + "/tobago\n"
                    "\t" + request.url.rstrip("/") + "/yugoslavia\n"
                    "\t" + request.url.rstrip("/") + "/macedonia\n"
                    "\t" + request.url.rstrip("/") + "/south%20korea\n"
                    "\t" + request.url.rstrip("/") + "/north%20korea\n"
                    "\t" + request.url.rstrip("/") + "/korea\n"
                    "\t" + request.url.rstrip("/") + "/sudan\n"
                    "\t" + request.url.rstrip("/") + "/south%20sudan\n"
                    "\t" + request.url.rstrip("/") + "/congo\n"
                    "\t" + request.url.rstrip("/") + "/democratic%20congo\n"
                    "\t" + request.url.rstrip("/") + "/djibouti\n"
                    "\t" + request.url.rstrip("/") + "/jibouti\n"
                    "\t" + request.url.rstrip("/") + "/jibooti\n"
                    "\n"
                    "requires some work\n\n"
                    "\t" + request.url.rstrip("/") + "/guinea\n"
                    "\t" + request.url.rstrip("/") + "/guini\n"
                    "\t" + request.url.rstrip("/") + "/equitorial%20guinea\n"
                    "\t" + request.url.rstrip("/") + "/guinea-bissau\n"
                    "\t" + request.url.rstrip("/") + "/papua%20new%20guinea\n"
                    "\t" + request.url.rstrip("/") + "/mozambiqe\n"
            "</pre>")

@app.route("/<country_input>")
def hello(country_input=None):
    try:
        country_output = correct(country_input)
    except Exception as e:
        return jsonify({"error": str(e)})

    try:
        country_code = reversed_national_olympic_committees[country_output].upper()
    except KeyError as e:
        return jsonify({"error": "%s not found" % country_output})
    return jsonify({
        "country": national_olympic_committees[country_code][0],
        "code": country_code
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
