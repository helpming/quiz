from collections import deque

test_case = int(input())

for i in range(test_case):
    n, m = list(map(int, input().split()))
    documents = deque(map(int, input().split()))

    results = []

    for i, document in enumerate(documents):
        documents[i] = {i: document}
    
    while documents:
        while list(documents[0].values())[0] < max(max(document.values()) for document in documents):
            documents.rotate(-1)
            
        results.append(documents.popleft())
        
    for i, result in enumerate(results):
        if list(result.keys())[0] == m:
            print(i + 1)