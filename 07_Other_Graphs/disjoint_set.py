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