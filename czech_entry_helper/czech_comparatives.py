from wordfreq import zipf_frequency
import json


# http://cokdybysme.net/pdfs/compsuper.pdf
def form_adj_comparative(word: str) -> str:
    # Adjectives that end in -oký and -eký also take a -ší comparative, but first drop the -oký or -eký ending:
    if word.endswith("oký") or word.endswith("eký"):
        return word[:-3] + "ší"
    elif word.endswith("ý") or word.endswith("í"):
        return word[:-1] + "ější"
    else:
        return word + "ější"

def form_adv_comparative(word: str) -> str:
    if word.endswith("ě") or word.endswith("e") or word.endswith("í"):
        return word + "ji"
    else:
        print("Warning: adverb does not end in -ě, -e, or -í")
        return word

def has_comparative(form_dict: dict[str, str | list[str]]):
    # print(form_dict)
    if any("tags" in form and form["tags"] == ["comparative"] for form in form_dict):
        return True
    return False


def print_non_adjectives_ending_in_ejší():
    with open("kaikki.org-dictionary-Czech.json", "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if data["word"].endswith("ější") and data["pos"] != "adj":
                print(data["word"])


def search_adjectives_without_comparatives():
    num_possible_edits = 0
    with open("kaikki.org-dictionary-Czech.json", "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if data["pos"] == "adj" and "forms" in data:
                if (
                    not has_comparative(data["forms"])
                    and zipf_frequency(form_adj_comparative(data["word"]), "cs") > 0.0
                ):
                    print(data["word"])
                    print(form_adj_comparative(data["word"]))
                    print(zipf_frequency(form_adj_comparative(data["word"]), "cs"))
                    # now print nej + comparative
                    print("nej" + form_adj_comparative(data["word"]))
                    print(zipf_frequency("nej" + form_adj_comparative(data["word"]), "cs"))
                    num_possible_edits += 1
        print(num_possible_edits)


# comp = form_comparative("děsivý")
# print(comp)
# print(zipf_frequency("comp", "cs"))
#search_adjectives_without_comparatives()
print_non_adjectives_ending_in_ejší()

#c = form_comparative("špičatý")
#print(c)
#print(zipf_frequency(c, "cs"))
#print("nej" + c)
#print(zipf_frequency("rád", "cs"))
