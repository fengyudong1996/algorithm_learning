def longest_sub(str1,str2):
    word_1 = list(str1)
    word_2 = list(str2)
    word_table = {}

    the_sub_len = float("-inf")
    the_sub_last = None

    for w1 in range(len(word_1)):
        word_table[w1] = {}
        for w2 in range(len(word_2)):
            word_table[w1][w2] = 0
            if w1 == 0 or w2 == 0:
                continue
            if word_1[w1] == word_2[w2]:
                word_table[w1][w2] = word_table[w1-1][w2-1] + 1

            if word_table[w1][w2] > the_sub_len:
                the_sub_len = word_table[w1][w2]
                the_sub_last = w1 + 1

    return str1[the_sub_last-the_sub_len:the_sub_last]


if __name__ == '__main__':
    print(longest_sub("hish", "fish"))

    pass




