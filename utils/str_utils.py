from random import randint

ALPHABETS = {
    'cyr': {
        'all': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'vowels': 'аеёиоуыэюя',
        'consonants': 'бвгджзйклмнпрстфхцчшщ'
    },
    'lat': {
        'all': 'abcdefghijklmnopqrstuvwxyz',
        'vowels': 'aeiouy',
        'consonants': 'bcdfghjklmnpqrstvwxyz'
    }
}


def generate_sentence(words_count: int, alphabet_type: str = 'cyr') -> str:
    """
    Generate random sentence with length word_count
    :param words_count: int - Count of words in sentence
    :param alphabet_type: str - Type of alphabet, cyr or lat
    :return:
    """
    max_word_len = 15
    min_word_len = 5
    vowels = ALPHABETS[alphabet_type]['vowels']
    consonants = ALPHABETS[alphabet_type]['consonants']
    c_len = len(consonants) - 1
    v_len = len(vowels) - 1
    words = []
    for idx in range(words_count):
        letters = [
            (consonants[randint(0, c_len)] if i % 2 == 0 else vowels[randint(0, v_len)])
            for i in range(randint(min_word_len, max_word_len))
        ]
        words.append(''.join(letters))
    sentence = ' '.join(words)
    sentence = sentence[0].upper() + sentence[1:]
    return '{}.'.format(sentence)


if __name__ == '__main__':
    print(generate_sentence(10))
    print(generate_sentence(10, alphabet_type='lat'))
