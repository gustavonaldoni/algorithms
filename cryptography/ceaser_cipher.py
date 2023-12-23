import string

ENGLISH_ALPHABET_UPPER = string.ascii_uppercase
ENGLISH_ALPHABET_LOWER = string.ascii_lowercase

CHARACTERS_TO_IGNORE = (" ", "\n", "\t")


def ceaser_cipher(text: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER) -> str:
    result = ""
    alphabet_length = len(alphabet)

    if key > alphabet_length:
        key = key % alphabet_length

    for character in text:
        if character in CHARACTERS_TO_IGNORE:
            result += character
            continue

        old_position_on_alphabet = alphabet.find(character)

        if old_position_on_alphabet == -1:
            raise ValueError(
                f"The character {character} does not belong to the alphabet."
            )

        new_position_on_alphabet = (old_position_on_alphabet + key) % alphabet_length

        cipher_character = alphabet[new_position_on_alphabet]

        result += cipher_character

    return result


def ceaser_decipher(text: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER) -> str:
    return ceaser_cipher(text, (-1) * key, alphabet)


if __name__ == "__main__":
    print(ceaser_cipher("ABCZ6", 2))
    print(ceaser_cipher("CDEB", -2))
