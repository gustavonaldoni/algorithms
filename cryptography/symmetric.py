import string

ENGLISH_ALPHABET_UPPER = string.ascii_uppercase
ENGLISH_ALPHABET_LOWER = string.ascii_lowercase

CHARACTERS_TO_IGNORE = (" ", "\n", "\t")


class SymmetricCryptography:
    def ceaser_cipher(
        self, text: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
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

            new_position_on_alphabet = (
                old_position_on_alphabet + key
            ) % alphabet_length

            cipher_character = alphabet[new_position_on_alphabet]

            result += cipher_character

        return result

    def ceaser_decipher(
        self, text: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
        return self.ceaser_cipher(text, (-1) * key, alphabet)

    def monoalphabetic_cipher(
        self, text: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
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
        self, text: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
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
    sc = SymmetricCryptography()

    print(sc.ceaser_cipher("ABCZ", 2))
    print(sc.ceaser_cipher("CDEB", -2))
    
    print(sc.monoalphabetic_cipher("MEET ME LATER", "DKVQFIBJWPESCXHTMYAUOLRGZN"))
    print(sc.monoalphabetic_decipher("CFFU CF SDUFY", "DKVQFIBJWPESCXHTMYAUOLRGZN"))
