from typing import List


class TrieNode:
    def __init__(self, value: any, children: List = None):  # children: List[Optional[Node]] type
        self.children = children if children else []
        self.value = value

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, value):  # return type: Optional[TrieNode]
        for child in self.children:
            if child and child.value == value:
                return child
        return None

    def is_leaf(self):
        return None in self.children


class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            child = curr_node.find_child(c)
            if child:
                curr_node = child
            else:
                new_child = TrieNode(c)
                curr_node.add_child(new_child)
                curr_node = new_child
        curr_node.add_child(None)

    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            child = curr_node.find_child(c)
            if not child:
                return False
            else:
                curr_node = child
        return curr_node.is_leaf()

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            child = curr_node.find_child(c)
            if not child:
                return False
            else:
                curr_node = child
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
