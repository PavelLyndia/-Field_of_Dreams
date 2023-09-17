import random
frut = "apple", "apricot", "banana", "mango", "kiwi", "orange"
my_nums = int(input())
print(my_nums, "- спроб вгадати слово")
word_rand = random.choice(frut)
print(word_rand)
word_mine = '*' * len(word_rand)
print(word_mine)
while (my_nums != 0) and (word_mine != word_rand):
    new = ''
    my_word = input('Введіть літеру: ')
    if my_word != '':
        if my_word in word_rand:
            for i in range(len(word_rand)):
                if my_word == word_rand[i]:
                    new += my_word
                else:
                    new += word_mine[i]
            word_mine = new
            print(word_mine)
        else:
            my_nums -= 1
            print("Такої літери немає: ", my_nums)
