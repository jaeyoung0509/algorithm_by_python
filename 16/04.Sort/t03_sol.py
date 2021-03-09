def solution(citations):
    sorted_citations = sorted(citations, reverse= True)
    for i in range(len(sorted_citations)):
        if sorted_citations[i]  <= i:
            return i
    return len(sorted_citations)
citations =  [10, 100]    
a = solution(citations)
print(a)