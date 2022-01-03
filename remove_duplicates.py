def remove_duplicates(str):
    map = {}
    s_len=len(str)
    i=0
    while i<s_len:
        if str[i] in map:
            del(str[i])
            s_len -= 1
        else:
            map[str[i]]=1
            i += 1
    return
