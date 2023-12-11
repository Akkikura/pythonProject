def count_characters(text, characters):
    character_count = {}
    for char in characters:
        count = text.count(char)
        character_count[char] = count
    return character_count
