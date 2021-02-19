#disjoint_set : 서로소 집합 공통 원소가 없는 두 집합

def find_parent(parent , x):
    if parent[x] != x :
        # root node 가 아니라면 자기 부모 노드를 호출
        return find_parent(parent , parent[x])
    return x

def union_parent(parent ,a ,b):
    a = find_parent(parent , a)
    b = find_parent(parent , b)
    if a< b:
        parent[b] = a
    else :
        parent[a] = b

for i in range(1 ,v+1):
    parent[i]  = i


for edge in edges:
    cost , a , b = edge
    if find_parent(parent , a) != find_parent(parent ,b):
        union_parent(parent , a ,b)
        result += cost