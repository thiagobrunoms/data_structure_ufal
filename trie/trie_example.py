class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {} #key: char, #value: reference to another TrieNode

    def __str__(self):
        return "char = " + self.char + ", is_ending = " + str(self.is_end) + ", children = " + self.children.__str__()

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert_word(self, word: str):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
           
            current = current.children[letter]

        current.is_end = True

    def autocomplete(self, prefix: str):
        suggestions = []
        
        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return suggestions

        if current.is_end:
            suggestions.append(prefix)

        self.lookup_suggestions(current, prefix, suggestions)
        return suggestions

    def lookup_suggestions(self, current: TrieNode, prefix: str, suggestions: list) -> list:
        node = current
        for char in node.children:
            suggestion_word = prefix + char

            if node.children[char].is_end:
                suggestions.append(suggestion_word)
            
            self.lookup_suggestions(node.children[char], suggestion_word, suggestions)

        return suggestions
    
    def show(self, next_node: TrieNode):
        print(next_node)
        for letter in next_node.children:
            self.show(next_node.children[letter])

    def __str__(self):
        return self.root

suggestions = Trie()
suggestions.insert_word("word")
suggestions.insert_word("work") 
suggestions.insert_word("worp") 
suggestions.insert_word("working")
suggestions.insert_word("wording")

suggestions_list = suggestions.autocomplete("wor")
print(suggestions_list)
