class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_last = False

class Trie:
    def __init__(self):
        self.trie = TrieNode('#')
        self.counter = 0

    def insert(self, word):
        root = self.trie

        if not word:
            return

        for char in word:
            if not char in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.is_last = True
        self.counter += 1

    def search(self, word):
        root = self.trie

        for char in word:
            if char in root.children:
                root.children[char] = TrieNode(char)
            else:
                return False
        return root.is_last

    def find_common_prefix(self):
        root = self.trie
        common_prefix = ""
        child = root.children
        while child:

            if len(child.keys()) > 1:
                break

            for k in child:
                common_prefix += k
                print(child[k])
                if child[k].is_last:
                    child = None
                    break
                child = child[k].children


        return common_prefix

if __name__ == "__main__":
    trie = Trie()
    strs = ["ab", "a"]
    for i in strs:
        trie.insert(i)
    # print(trie)
    print(trie.find_common_prefix())


