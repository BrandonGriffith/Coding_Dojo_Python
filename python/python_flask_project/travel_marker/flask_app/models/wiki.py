import wikipedia

def wiki_summary(data):
    data1 = wikipedia.search(data, results=3)
    try:
        print(data1)
        data1 = wikipedia.summary(data1[0])
    except(wikipedia.exceptions.DisambiguationError,wikipedia.exceptions.PageError):
        try:
            data1 = wikipedia.summary(data1[1])
        except(wikipedia.exceptions.DisambiguationError,wikipedia.exceptions.PageError):
            data1 = wikipedia.summary("New York (state)")
    return data1

