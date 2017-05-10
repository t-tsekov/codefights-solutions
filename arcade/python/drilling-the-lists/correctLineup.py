def correctLineup(athletes):
    return [item for sublist in zip(athletes[1::2],athletes[0::2]) for item in sublist]
