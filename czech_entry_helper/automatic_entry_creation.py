from typing import Literal
from wordfreq import zipf_frequency

from czech_entry_helper.czech_comparatives import form_adj_comparative, form_adv_comparative
import pyperclip
import re
from typing import Match


# Function to add double square brackets around words
def surround_with_brackets(match: Match[str]) -> str:
    word = match.group(0)
    return f"[[{word}]]"


def create_wiktionary_entry(
    word: str,
    pos: Literal["adv", "adj", "verb"],
    definition: str,
    form_comp: bool = False,
):
    wikitext = """==Czech==

===Pronunciation===
* {{cs-IPA}}

"""
    if pos == "adj":
        wikitext += "===Adjective===\n"
        comp = form_adj_comparative(word)
        if zipf_frequency(comp, "cs") > 0.0 or form_comp:
            wikitext += f"{{{{cs-adj|{comp}}}}}"
        else:
            wikitext += "{{cs-adj}}"
        wikitext += "\n\n"
        if " " in definition or "," in definition:
            # Surround each word in definition with double square brackets
            wikitext += "# " + re.sub(r'\b\w+\b', surround_with_brackets, definition)
        else:
            wikitext += f"# [[{definition}]]"
        wikitext += "\n\n====Declension====\n"
        wikitext += "{{cs-adecl}}"
    elif pos == "adv":
        wikitext += "===Adverb===\n"
        comp = form_adv_comparative(word)
        if (zipf_frequency(comp, "cs") > 0.0 and comp != word) or form_comp:
            wikitext += f"{{{{cs-adv|{comp}|{f"nej{comp}"}}}}}"
        else:
            wikitext += "{{cs-adv}}"
        wikitext += "\n\n"
        wikitext += "# " + re.sub(r'\b\w+\b', surround_with_brackets, definition)  

    print(wikitext)
    pyperclip.copy(wikitext)

def create_noun_wiktionary_entry(
    word: str,
    definition: str,
    gender: Literal["m", "f", "n"],
    animacy: Literal["an", "in"] = "in"
):
    if gender == "m":
        if animacy == "an":
            noun_section_gender = "m-an"
            declension_section_gender = "m.an"
        else:
            noun_section_gender = "m-in"
            declension_section_gender = "m"
    else:
        noun_section_gender = declension_section_gender = gender
    wikitext = f"""==Czech==

===Pronunciation===
* {{{{cs-IPA}}}}

===Noun===
{{{{cs-noun|{noun_section_gender}}}}}

# {re.sub(r'\b\w+\b', surround_with_brackets, definition)}

====Declension====
{{{{cs-ndecl|{declension_section_gender}}}}}"""

    print(wikitext)
    pyperclip.copy(wikitext)


# print(count_occurence_of_word("budu <-> pomáhat"))
