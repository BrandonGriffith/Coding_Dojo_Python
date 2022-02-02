import wikipedia

def wiki_summary(data):
    data1 = wikipedia.search(data, results=3)
    try:
        data1 = wikipedia.summary(data1[0])
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        if (data1[0] == "new york sity"):
            data1 = ['',"New York (state)"]
        data1 = wikipedia.summary(data1[1])
    return data1



