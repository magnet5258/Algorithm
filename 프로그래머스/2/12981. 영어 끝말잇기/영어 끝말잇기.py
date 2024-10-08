def solution(n, words):
    used_words = set()
    previous_word = ""
    for i in range(len(words)):
        current_word = words[i]
        player = (i % n) + 1
        turn = (i // n) + 1

        if current_word in used_words or (previous_word and previous_word[-1] != current_word[0]):
            return [player, turn]
        used_words.add(current_word)
        previous_word = current_word

    return [0, 0]
