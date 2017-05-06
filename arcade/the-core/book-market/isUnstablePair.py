def isUnstablePair(filename1, filename2):
    if (filename1 <= filename2 and filename1.lower() > filename2.lower()) or (filename2 <= filename1 and filename2.lower() > filename1.lower()):
        return True
    return False

