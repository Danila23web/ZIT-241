def reverse_words_in_sentence(sentence):

    reversed_sentence = " ".join(sentence.split()[::-1])
    return reversed_sentence

sentence = "Юпитер третий или Индуро"

reversed_sentence = reverse_words_in_sentence(sentence)
print("Исходная строка:", sentence)
print("Измененная строка:", reversed_sentence)
