class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True



n = int(input("enter no:of entries: "))
trie = Trie()

for _ in range(n):
    parts = input().split()
    command = parts[0]
    arg = parts[1]

    if command == "insert":
        trie.insert(arg)
    elif command == "search":
        result = trie.search(arg)
        print("true" if result else "false")
    elif command == "startsWith":
        result = trie.startsWith(arg)
        print("true" if result else "false")
