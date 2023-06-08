class TrieNode:
    def __init__(self, char):
        self.char = char
        self.next_char = {}


class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def add(self, word, node):
        if not word:
            return
        if word[0] not in node.next_char.keys():
            node.next_char[word[0]] = TrieNode(word[0])
        self.add(word[1:], node.next_char[word[0]])
        

class Solution:
    def minimumLengthEncoding(self, words):
        tr = Trie()
        for word in words:
            tr.add(word[::-1], tr.root)
        
        self.ans = 0
        def leafsum(node, d=0):
            if not node.next_char:
                self.ans += d+1
            for x in node.next_char.values():
                leafsum(x, d+1)
        
        leafsum(tr.root)
        return self.ans