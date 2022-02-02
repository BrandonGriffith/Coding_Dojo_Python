import wikipedia

def wiki_summary(data):
    data1 = wikipedia.search(data, results=3)
    if (data == "New York" or data == "new york"):
            data1 = ["New York (state)"]
    try:
        data1 = wikipedia.summary(data1[0])
    except(wikipedia.exceptions.DisambiguationError,wikipedia.exceptions.PageError):
        data1 = wikipedia.summary(data1[1])
    return data1



