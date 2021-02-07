import random

# Load phrases
def load_data():
    with open("./ipsum_generator/data.txt") as f:
        phrases = [line.lower().rstrip() for line in f.readlines()]
    return phrases


# Get a phrase at random
def get_phrase():
    phrases = load_data()
    phrase = random.choice(phrases)
    return f"{phrase} "


def create_sentence():
    sentence = ""
    number_of_phrases = random.randint(3, 6)
    for i in range(number_of_phrases):
        sentence += get_phrase()
        if not i + 1 == number_of_phrases:
            if random.randint(1, 5) == 1:
                sentence = sentence.rstrip()
                sentence += ", "
        else:
            if sentence[-1] == "?":
                return sentence.rstrip()
            else:
                return f"{sentence.rstrip().capitalize()}."


# Create a paragraph
def create_paragraph():
    number_of_sentences = random.randint(12, 20)
    para = ""
    for i in range(number_of_sentences):
        if not "." in para:
            para += create_sentence()
        else:
            para += f" {create_sentence()}"

    return para


def create_text(number_of_paragraphs):
    text = ""
    for i in range(number_of_paragraphs):
        text += f"{create_paragraph()}\n\n"

    return text.rstrip()
