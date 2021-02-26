class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = False
        self.children = {}
    
class Trie:
    
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, word):
        cur_node = self.head
        
        for char in word:
            if cur_node.data:
                return False    

            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            
            cur_node = cur_node.children[char]
        
        cur_node.data = True
        if len(cur_node.children) > 0:
            return False
        else:
            return True
        
# s = Trie()
# print(s.insert("bring"))
# print(s.insert("brings"))
# print(s.insert("bri"))
# print(s.insert("bro"))
# print(s.insert("brin"))

def solution(phone_book):
    answer = True
    
    return answer