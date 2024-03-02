

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''

    l = []
    if len(sequence) == 1:
        l.append(sequence)
        return l 
    else:
        ll = []
        l = get_permutations(sequence[:-1])
        new = sequence[-1]
        for elem in l:
            for i in range(len(elem)+1):
                ll.append(elem[0:i]+ new + elem[i:])
    return ll

#print(get_permutations('Lions'))

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))