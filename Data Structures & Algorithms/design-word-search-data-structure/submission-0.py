class WordDictionary:

    def __init__(self):
        self.stack = []

    def addWord(self, word: str) -> None:
        if word in self.stack:
            return
        self.stack.append(word)

    def search(self, word: str) -> bool:
        if word in self.stack:
            return True
        #now handle the . case
        for stored in self.stack:
            if len(stored) != len(word):
                continue

            match = True

            for i in range(len(word)):
                if word[i] == ".":
                    continue

                if word[i] != stored[i]:
                    match = False
                    break

            if match:
                return True

        return False
