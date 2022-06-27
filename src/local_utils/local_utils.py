import csv
import pandas as pd
from readability import Readability


def sanitize_string(string):
    """We're dealing with csvs, so we want to get rid of the punctuation."""
    return string.replace(",", "").replace('"', "").replace("\n", "").replace("\t", "")


def flesch_complexity(text):
    """_summary_

    Flesch Formula = Reading Ease score = 206.835 - (1.015 * ASL) - (84.6 * ASW) where 
        ASL = average sentence length (number of words divided by number of sentences)
        ASW = average word length in syllables (number of syllables divided by number of words)
    
        Higher scores indicate the text is _easier_ to read. Scores between 0-30 are generally
        understood by college graduates. Scores over 90 indicate approximately a 5th grade reading level.
    Args:
        text (_type_): _description_
    """
    return Readability(text).flesch().score


def write_data(object_list, file_name):
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        for obj in object_list:
            writer.writerow([obj.asdict().items()])

def main():
    pass

if __name__ == "__main__":
    main()