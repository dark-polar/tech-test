import heapq

beginWord = "hot"
endWord = "log"
wordList = ["hot","dot","dog","lot","log"]

class Node:
    def __init__(self, word):
        self.word = word
        self.children = []
        self.visited = False
        self.last = None

    def __str__(self):
        s = ""
        s += self.word + "\n"
        s += ",".join([c.word for c in self.children]) + "\n"
        s += str(self.visited) + "\n"
        return s

def buildGraph(begin, end, wordList):

    all_words = wordList + [begin, end]
    all_words = list(dict.fromkeys(all_words))
    d = { w : Node(w) for w in all_words }

    for i, w in enumerate(all_words):
        for w2 in (all_words[i+1:]):
            if canHop(w, w2):
                d[w].children.append(d[w2])
                d[w2].children.append(d[w])

    return d

def canHop(w, w2):
    return len(list(filter(lambda x: x == False, [c == w2[i] for i, c in enumerate(w)]  ))) == 1

graph = buildGraph(beginWord, endWord, wordList)

s = graph[beginWord]
e = graph[endWord]

def findLadders(s, e, graph):
    scores = []
    heapq.heapify(scores)

    s.visited = True
    paths = [s]
    heapq.heappush(scores, (0, s.word))

    flag = False

    while len(scores) > 0:
        d, w = heapq.heappop(scores)
        n = graph[w]
        for c in n.children:
            if c.visited:
                continue
            c.last = n
            if c == e:
                flag = True
                break
            c.visited = True
            heapq.heappush(scores, (d+1, c.word))
        if flag:
            break
    result = []
    last = e
    while last is not None:
        result.append(last.word)
        last = last.last
    return result

print(findLadders(s,e,graph))