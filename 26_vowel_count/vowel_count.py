def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
 
    freq_map = {}
    for let in phrase.lower():
        if let in set("aeiou"):
            freq_map[let] = freq_map.get(let, 0)+1
    return freq_map
