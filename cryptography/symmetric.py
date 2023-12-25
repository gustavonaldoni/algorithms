import string

ENGLISH_ALPHABET_UPPER = string.ascii_uppercase
ENGLISH_ALPHABET_LOWER = string.ascii_lowercase

CHARACTERS_TO_IGNORE = (" ", "\n", "\t")


class SymmetricCryptography:
    def ceaser_cipher(
        self, plaintext: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
        result = ""
        alphabet_length = len(alphabet)

        if key > alphabet_length:
            key = key % alphabet_length

        for character in plaintext:
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
        self, ciphertext: str, key: int, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
        return self.ceaser_cipher(ciphertext, (-1) * key, alphabet)

    def monoalphabetic_cipher(
        self, plaintext: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
        result = ""

        for character in plaintext:
            if character in CHARACTERS_TO_IGNORE:
                result += character
            else:
                position_on_alphabet = alphabet.find(character)
                cipher_character = key[position_on_alphabet]

                result += cipher_character

        return result

    def monoalphabetic_decipher(
        self, ciphertext: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER
    ) -> str:
        result = ""

        for character in ciphertext:
            if character in CHARACTERS_TO_IGNORE:
                result += character
            else:
                position_on_key = key.find(character)
                decipher_character = alphabet[position_on_key]

                result += decipher_character

        return result
    
    def vigenere_cipher(self, plaintext: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER) -> str:
        result = ""
        
        alphabet_length = len(alphabet)
        key_length = len(key)
        
        index = 0
        
        for character in plaintext:
            if character in CHARACTERS_TO_IGNORE:
                result += character
            else:
                character_position_on_alphabet = alphabet.find(character)
                key_position_on_alphabet = alphabet.find(key[index % key_length])
                
                cipher_character = alphabet[(character_position_on_alphabet + key_position_on_alphabet) % alphabet_length]
                
                result += cipher_character
                
                index += 1
        
        return result
    
    def vigenere_decipher(self, ciphertext: str, key: str, alphabet: str = ENGLISH_ALPHABET_UPPER) -> str:
        result = ""
        
        alphabet_length = len(alphabet)
        key_length = len(key)
        
        index = 0
        
        for character in ciphertext:
            if character in CHARACTERS_TO_IGNORE:
                result += character
            else:
                character_position_on_alphabet = alphabet.find(character)
                key_position_on_alphabet = alphabet.find(key[index % key_length])
                
                decipher_character = alphabet[(character_position_on_alphabet - key_position_on_alphabet) % alphabet_length]
                
                result += decipher_character
                
                index += 1
        
        return result
    
    def _clean_plaintext(self, plaintext: str) -> str:
        """Remove all characters that needs to be ignored on the plaintext. 
           These characters are defined on CHARACTERS_TO_IGNORE constant.

        Args:
            plaintext (str): the plaintext to remove the characters from.

        Returns:
            str: the plaintext with all characters to ignore removed.
        """

        for character_to_ignore in CHARACTERS_TO_IGNORE:
            plaintext = plaintext.replace(character_to_ignore, "")
            
        return plaintext
    
    def get_column_from_text(self, text: str, number_of_rows: int, number_of_columns: int, column: int) -> str:
        result = ""
        
        for i in range(number_of_rows):
            result += text[i * number_of_columns + column]
            
        return result
    
    def permutation_cipher(self, plaintext: str, key: list[int], fill_character: str = " ") -> str:
        ciphertext = ""
        
        clean_plaintext = self._clean_plaintext(plaintext)
        clean_plaintext_length = len(clean_plaintext)
        
        number_of_columns = len(key)
        
        # Filling the clean_plaintext to form a complete matrix
        remainder = clean_plaintext_length % number_of_columns
        
        if remainder != 0:
            clean_plaintext += fill_character * (number_of_columns - remainder)
            clean_plaintext_length = len(clean_plaintext)
        
        number_of_rows = clean_plaintext_length // number_of_columns
        
        # Completing the ciphertext on the correct order
        key_map = {key[column]: column for column in range(number_of_columns)}
        
        for column in range(number_of_columns):
            ciphertext += self.get_column_from_text(clean_plaintext, number_of_rows, number_of_columns, key_map[column])
        
        ciphertext = ciphertext.replace(fill_character, "")
        
        return ciphertext

    def permutation_decipher(self, ciphertext: str, key: list[int]) -> str:
        pass


if __name__ == "__main__":
    sc = SymmetricCryptography()
    
    print(sc.ceaser_cipher(plaintext="ABCZ", key=2))
    print(sc.ceaser_decipher(ciphertext="CDEB", key=2))
    
    print(sc.monoalphabetic_cipher(plaintext="MEET ME LATER", key="DKVQFIBJWPESCXHTMYAUOLRGZN"))
    print(sc.monoalphabetic_decipher(ciphertext="CFFU CF SDUFY", key="DKVQFIBJWPESCXHTMYAUOLRGZN"))

    print(sc.vigenere_cipher(plaintext="MEET ME LATER", key="LEMON"))
    print(sc.vigenere_decipher(ciphertext="XIQH ZP PMHRC", key="LEMON"))
    
    print(sc.permutation_cipher(plaintext="MEET ME LATER", key=[3, 2, 0, 1]))