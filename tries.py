class TrieNode:

    def __init__(self):
        self.child = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        for i in range(len(word)):
            node = self.root
            for letter in word:
                if letter not in node.child:
                    node.child[letter] = TrieNode()

                node = node.child[letter]
                node.endOfWord = True
            word = word[1:]

    def search(self, word):
        node = self.root

        for letter in word:
            if letter not in node.child:
                return False
            else:
                node = node.child[letter]

        return node.endOfWord


trie = Trie()
pattern = 'algorithmisfun'
trie.insert(pattern)
text = 'fun'
found = trie.search(text)

if found:
    print(text, 'is in the trie')
else:
    print(text, 'is not in the trie')
