def htmlEndTagByStartTag(startTag):
    tag = startTag.strip().split(" ")[0]
    endtag = "</" + tag[1:]
    if endtag[-1] != ">":
        endtag += ">"
    return endtag

