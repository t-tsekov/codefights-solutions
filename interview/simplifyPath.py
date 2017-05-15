def simplifyPath(path):
    path = path.replace("//", "/")
    dirList = path.split("/")
    dirStack = []
    for dir in dirList:
        if dir == "" or dir == ".":
            continue
        if dir == "..":
            if len(dirStack) > 0:
                dirStack.pop()
            continue

        dirStack.append(dir)

    return "/"+"/".join(dirStack)
