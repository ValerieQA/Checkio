def checkio(text, words):
    n = 0
    for word in words:
        if word in text.lower():
            n+=1
    return n

count_words = lambda text, words: sum(1 for word in words if word in text.lower())



print checkio("How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"})