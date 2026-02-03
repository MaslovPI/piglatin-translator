import argparse
import string


def main():
    parser = argparse.ArgumentParser(description="Piglatin translator")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    prompt = args.user_prompt

    words = prompt.split()
    new_words = [translate_with_puctuation(word) for word in words]
    print(" ".join(new_words))


def translate_with_puctuation(text):
    if not text:
        return ""

    stripped = text.rstrip(string.punctuation)
    punctuation_saved = text[len(stripped) :]

    is_initially_capital = text[0].isupper()

    stripped_lower = stripped.lower()
    translated = translate(stripped_lower)

    if is_initially_capital:
        translated = translated.capitalize()

    return translated + punctuation_saved


def translate(word) -> str:
    first_letter = word[0]
    return word[1:] + first_letter + "ay" if is_consonant(first_letter) else word + "ay"


def is_consonant(letter):
    vowels = ["a", "o", "u", "i", "e"]
    return letter not in vowels


if __name__ == "__main__":
    main()
