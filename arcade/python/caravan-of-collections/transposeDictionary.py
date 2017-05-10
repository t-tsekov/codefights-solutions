def transposeDictionary(scriptByExtension):
    return sorted([[y,x] for x,y in scriptByExtension.items()], key = lambda x:x[0])
