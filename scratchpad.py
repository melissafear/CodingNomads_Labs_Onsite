import markovify

with open ('war and peace.txt', 'r') as fin:
    corpus = fin.read()

model = markovify.text(corpus)

print(model.make_short_sentence(140))

for i in range(5):
    print(model.make_sentence())