"""
    设计一个方法，找出任意指定单词在一本书中的出现频率。

    你的实现应该支持如下操作：

    WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
    get(word)查询指定单词在书中出现的频率
    示例：

        WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
        wordsFrequency.get("you"); //返回0，"you"没有出现过
        wordsFrequency.get("have"); //返回2，"have"出现2次
        wordsFrequency.get("an"); //返回1
        wordsFrequency.get("apple"); //返回1
        wordsFrequency.get("pen"); //返回1
    提示：

        book[i]中只包含小写字母
        1 <= book.length <= 100000
        1 <= book[i].length <= 10
        get函数的调用次数不会超过100000

"""
from typing import List

class TreeNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.child:
                node.child[c] = TreeNode()
            node = node.child[c]

        node.is_word = True
        node.count += 1

        return 

    def search(self, word):
        node = self.root
        
        for c in word:
            if c not in node.child:
                return 0
            node = node.child[c]
        
        if node.is_word:
            return node.count
        else:
            return 0

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.t = Trie()
        for word in book:
            self.t.insert(word)

    def get(self, word: str) -> int:
        return self.t.search(word)

# from collections import Counter
# class WordsFrequency:

#     def __init__(self, book: List[str]):
        
#         self.booklist = Counter(book)


#     def get(self, word: str) -> int:
#         return self.booklist[word]


# Your WordsFrequency object will be instantiated and called as such:
obj = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
param_1 = obj.get("i")
print(param_1)