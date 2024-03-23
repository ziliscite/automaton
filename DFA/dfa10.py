from models import DFA

#DFA accepts every string of {a, b} with an odd number of 'a'
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'A',
        ('B', 'a'): 'A', ('B', 'b'): 'B'
        }, q0='A', F={'B'})

    L = [
        'a', 'b', 'ab', 'ba', 'aab', 'abb', 'aba', 'baa', 'bba', 'bbb',
        'aaab', 'aabb', 'abaa', 'abba', 'abbb', 'baab', 'baba', 'babb', 'bbaa', 'bbab',
        'bbba', 'aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa',
        'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb', 'aaaaa', 'aaaab', 'aaaba',
        'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb',
        'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab',
        'babba', 'babbb', 'bbaaa', 'bbaab', 'bbaba', 'bbabb', 'bbbaa', 'bbbab', 'bbbba',
        'bbbbb', 'aaaaaa', 'aaaaab', 'aaaaba', 'aaaabb', 'aaabaa', 'aaabab', 'aaabba', 'aaabbb',
        'aabaaa', 'aabbaa', 'aabbbb', 'abaaaa', 'abaaab', 'ababaa', 'ababab', 'ababba', 'ababbb',
        'abbaaa', 'abbaba', 'abbabb', 'abbbaa', 'abbbab', 'abbbba', 'abbbbb', 'baaaaa', 'baaaab',
        'baaaba', 'baaabb', 'baabaa', 'baabab', 'baabba', 'baabbb', 'babaaa', 'babaab', 'bababa',
        'bababb', 'babbaa', 'babbab', 'babbba', 'babbbb', 'bbaaaa', 'bbaaab', 'bbaaba', 'bbaabb',
        'bbabaa', 'bbabab', 'bbabba', 'bbabbb', 'bbbaaa', 'bbbaab', 'bbabab', 'bbbabb', 'bbbbaa',
        'bbbbab', 'bbbbba', 'bbbbbb'
    ]
    
    for strings in L:
        print(obj.run(strings))