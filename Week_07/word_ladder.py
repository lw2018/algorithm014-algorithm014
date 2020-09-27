#127. 单词接龙

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:return 0

        front = {beginWord} #
        back = {endWord}    #
        wordList = set(wordList)
        word_len = (len(endWord))
        dist = 1
        letter = [chr(i) for i in range(97, 123)]
        visited = set()

        while front and back:   #
            next_front = set()  #下一层nodes
            dist+=1
            for word in front:  #生成新的node 加到下一层nodes
                for i in range(word_len):
                    for c in letter:
                        if c != word[i]:
                            new_word = word[:i] +c+word[i+1:]
                            if new_word in back:
                                return dist
                            #if new_word in wordList:
                            if new_word not in visited and new_word in wordList:
                                next_front.add(new_word)
                                #wordList.remove(new_word)
                                visited.add(new_word)

            #下面将下一层nodes赋值给front
            front = next_front  
            if len(front) > len(back):
                front, back = back, front
        return 0