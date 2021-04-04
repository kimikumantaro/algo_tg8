class TrieNode:

    def __init__(self):
        self.child = {}                             # initialize child node as empty
        self.endOfWord = False                      # endOfWord becomes True if node represent end of word


class Trie:

    def __init__(self):
        self.root = TrieNode()                      # initialize root node as child node

    def insert(self, word):

        for i in range(len(word)):                  # algorithm runs until end of word
            node = self.root                        # current node becomes root node
            for letter in word:                     # for loop runs until all letters are covered
                if letter not in node.child:        
                    node.child[letter] = TrieNode() # value of node of current letter becomes empty

                node = node.child[letter]           # current node becomes node of current letter
                node.endOfWord = True               # endOfWord becomes True
            word = word[1:]                         # current word becomes substring of current word starting from index 1

    def search(self, word):
        node = self.root                            # current node becomes root node

        for letter in word:                         # for loop runs until all letters are covered
            if letter not in node.child:
                return False
            else:
                node = node.child[letter]           # current node becomes node of current letter

        return node.endOfWord                       # return True


trie = Trie()
pattern = 'algorithmisfun'
trie.insert(pattern)
text = 'fun'
found = trie.search(text)

if found:
    print(text, 'is in the trie')
else:
    print(text, 'is not in the trie')
