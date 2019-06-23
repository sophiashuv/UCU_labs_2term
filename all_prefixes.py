def all_prefixes(word):
    """
    (str) -> (set/None)
    The function returns all prefixes of the word
    """
    if isinstance(word, str):
        a = set()
        for i in range(len(word)):
            a.add(word[:i + 1])
        return a
    return None

