n = int(input())
pupils = []
known_languages = set()
lingua_franca = set()

for i in range(n):
    m = int(input())
    pupil_knowledge = []

    for j in range(m):
        lang = input()
        known_languages.add(lang)
        pupil_knowledge.append(lang)

    if i == 0:
        lingua_franca = set(pupil_knowledge)
    else:
        lingua_franca = lingua_franca.intersection(set(pupil_knowledge))

print(len(lingua_franca))
for lang in lingua_franca:
    print(lang)

print(len(known_languages))
for lang in known_languages:
    print(lang)
