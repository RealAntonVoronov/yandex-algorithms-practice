g, s = [int(x) for x in input().split()]
word = input()
seq = input()
res = 0

char_range = [min(ord('a'), ord('A')), max(ord('z'), ord('Z'))]
vocab = [0] * (char_range[1] - char_range[0] + 1)

for char in word:
    vocab[ord(char) - char_range[0]] += 1

piece = seq[:g]
piece_vocab = [0] * (char_range[1] - char_range[0] + 1)
for char in piece:
    piece_vocab[ord(char) - char_range[0]] += 1

n_equal = 0
for i in range(len(piece_vocab)):
    if piece_vocab[i] == vocab[i] and vocab[i] != 0:
        n_equal += 1

h = len(set(word))
if n_equal == h:
    res += 1

for i in range(g, len(seq)):
    letter = seq[i - g]
    letter_id = ord(letter) - char_range[0]
    letter_count = vocab[letter_id]
    piece_vocab[letter_id] -= 1
    if vocab[letter_id] != 0 and piece_vocab[letter_id] == letter_count:
        n_equal += 1
    elif vocab[letter_id] != 0 and piece_vocab[letter_id] + 1 == letter_count:
        n_equal -= 1

    letter = seq[i]
    letter_id = ord(letter) - char_range[0]
    letter_count = vocab[letter_id]
    piece_vocab[letter_id] += 1

    if vocab[letter_id] != 0 and piece_vocab[letter_id] == letter_count:
        n_equal += 1
    elif vocab[letter_id] != 0 and piece_vocab[letter_id] - 1 == letter_count:
        n_equal -= 1

    if n_equal == h:
        res += 1

print(res)