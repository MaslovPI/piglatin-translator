import argparse


def main():
    parser = argparse.ArgumentParser(description="Piglatin translator")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    prompt = args.user_prompt

    words = prompt.split()
    new_words = []
    for word in words:
        first_letter = word[0].lower()
        if is_consonant(first_letter):
            new_word = word[1:] + first_letter + "ay"
        else:
            new_word = word + "ay"
        new_words.append(new_word)
    print(" ".join(new_words))


def is_consonant(letter):
    vowels = ["a", "o", "u", "i", "e"]
    return letter not in vowels


if __name__ == "__main__":
    main()
