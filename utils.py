def secoud_longest_string(lst_strings):
    if len(lst_strings) < 2: 
        return lst_strings[0] # valami ilyesmi eseteleg raise
    else: 
        sorted_strings = sorted(lst_strings, key=len, reverse= True)
    return sorted_strings[1]