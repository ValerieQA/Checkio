from string import ascii_lowercase

def checkio(text):
    letters = [x for x in text.lower() if x in ascii_lowercase]
    counts = sorted({x: letters.count(x) for x in letters}.items(), key=lambda x: x[1], reverse=True)
    wanted_count = counts[0][1]
    wanted = sorted([x[0] for x in counts if x[1] == wanted_count])[0]
    return wanted

print checkio("Hello World!")

checkio = lambda t: max(__import__('string').ascii_lowercase, key=t.lower().count)

print checkio("Hello World!")

def smth(words):
    d = {}
    for word in words:
        if word in d:
            d[word] +=1
        if word not in d:
            d[word] = 1
    a = max(d, key = d.get)

    return a



print smth("jkhg kjdhfgggggg joioror dzsfgshgggg")