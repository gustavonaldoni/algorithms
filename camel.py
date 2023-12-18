import re

def to_camel_case(text: str, preserve_case: bool = False) -> str:
    result = ""
    
    if len(text) == 1:
        result = text.lower()
    
    elif len(text) > 1:
        text = text.strip()
        text = re.sub(r"\s+", r" ", text)
        
        words = text.split(" ")
        
        first_word = words[0]
        
        if preserve_case:
            result += f'{first_word[0].lower()}{first_word[1:]}'
        else:
            result += first_word.lower()
        
        for word in words[1:]:
            if preserve_case:
                result += f'{word[0].upper()}{word[1:]}'
            else:  
                result += word.capitalize()

    return result
   
if __name__ == "__main__":
    text = "Adriano aevedo naldoni p8RRa"
    
    print(to_camel_case(text, preserve_case=True))