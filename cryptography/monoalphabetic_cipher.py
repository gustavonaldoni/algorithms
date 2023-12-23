import string

ENGLISH_ALPHABET_UPPER = string.ascii_uppercase
ENGLISH_ALPHABET_LOWER = string.ascii_lowercase

CHARACTERS_TO_IGNORE = (" ", "\n", "\t")


def monoalphabetic_cipher(
    text: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
) -> str:
    result = ""

    for character in text:
        if character in CHARACTERS_TO_IGNORE:
            result += character
        else:
            position_on_alphabet = alphabet.find(character)
            cipher_character = key[position_on_alphabet]

            result += cipher_character

    return result


def monoalphabetic_decipher(
    text: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
) -> str:
    result = ""

    for character in text:
        if character in CHARACTERS_TO_IGNORE:
            result += character
        else:
            position_on_key = key.find(character)
            cipher_character = alphabet[position_on_key]

            result += cipher_character

    return result


if __name__ == "__main__":
    print(monoalphabetic_cipher("MEET ME LATER", "DKVQFIBJWPESCXHTMYAUOLRGZN"))
    print(monoalphabetic_decipher("CFFU CF SDUFY", "DKVQFIBJWPESCXHTMYAUOLRGZN"))
