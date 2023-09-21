vowels = ["а", "о", "и", "ы", "у", "э", "я", "ю", "ё", "е"]

poem = input("Enter a poem: ")


def count_vowels(phrase):
    vowel_count = 0

    for char in phrase:
        if char in vowels:
            vowel_count += 1

    return vowel_count


def check_poem(poem):
    phrases = poem.split()

    first_vowel_count = count_vowels(phrases[0])

    for phrase in phrases[1:]:
        vowel_count = count_vowels(phrase)
        if vowel_count != first_vowel_count:
            return False
    return True


if check_poem(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")
