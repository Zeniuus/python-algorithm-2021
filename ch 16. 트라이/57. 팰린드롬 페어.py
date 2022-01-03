from typing import List
from util import print_result


# 56. 트라이 구현.py에서 copy-and-paste 해옴
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
        self.root = TrieNode('')

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


def is_palindrome(word: str):
    return word == word[::-1]


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])

        result = []
        for word_idx, word in enumerate(words):
            curr_node = trie.root
            prefix = ''
            postfix = word
            if curr_node.is_leaf() and is_palindrome(postfix) and word != prefix[::-1]:
                result.append([word_idx, words.index(prefix[::-1])])
            for c in word:
                prefix += c
                postfix = postfix[1:]
                curr_node = curr_node.find_child(c)
                if not curr_node:
                    break
                if curr_node.is_leaf() and is_palindrome(postfix) and word != prefix[::-1]:
                    result.append([word_idx, words.index(prefix[::-1])])

            if curr_node:
                candidates = []

                def bfs(node: TrieNode, curr_word: str):
                    for child in node.children:
                        if child:
                            bfs(child, curr_word + child.value)
                    if node.is_leaf():
                        candidates.append(curr_word[::-1])

                bfs(curr_node, word)
                for candidate in candidates:
                    if len(prefix) < len(candidate) and is_palindrome(prefix + candidate):
                        result.append([word_idx, words.index(candidate)])

        return result


print_result(Solution(),
             inputs=[["abcd","dcba","lls","s","sssll"]],
             expected=[[0,1],[1,0],[3,2],[2,4]])
print_result(Solution(),
             inputs=[["a",""]],
             expected=[[0,1],[1,0]])
