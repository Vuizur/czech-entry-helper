import json


def adjective_to_adverb(word: str) -> str:
    if word.endswith("lý") or word.endswith("sý"):
        return word[:-1] + "e"
    elif word.endswith("rý"):
        return word[:-2] + "ře"
    elif word.endswith("cí"): # Mostly these adverbs don't exist though
        return word[:-1] + "e"
    elif word.endswith("í"):
        return word[:-1] + "ě"
    elif word.endswith("chý"):
        return word[:-3] + "še"
    elif word.endswith("cký") or word.endswith("ský"):
        return word[:-2] + "ky"
    elif word.endswith("ký"):
        return word[:-2] + "ce"
    elif word.endswith("ý"):
        return word[:-1] + "ě"
    else:
        raise ValueError(f"Adjective {word} does not end in a known suffix")


with open("kaikki.org-dictionary-Czech.json", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data["pos"] == "adj" and "forms" in data:
            if data["word"].endswith("cí") and not data["word"].endswith("jící"):
                print(data["word"])
            #for form in data["forms"]:

                #break
                #    #if form["form"] != adjective_to_adverb(data["word"]):
                #    if data["word"].endswith("cí"):
                #        print(data["word"])
                #        print(form["form"])
                #        print(adjective_to_adverb(data["word"]))
                #    break
#