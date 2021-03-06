from collections import deque
def solution(bridge_length, weight, truck_weights):
    time  = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        # truck이 남아 있을 경우
        if truck_weights:
            # 다리에 잇는 트럭과 트럭[0] 의 합이 10을 넘지 않을 때
            if sum(bridge) + truck_weights[0] <= weight:
                print('not up to 10 bridge' , bridge  , 'truck_weight' , truck_weights[0] )
                bridge.append(truck_weights.pop(0))
                print(bridge)
            else:
                print('up to 10 , bridge' , bridge  , 'truck_weight' , truck_weights[0] )
                bridge.append(0)
                print(bridge)
    return time

bridge_length = 2
weight = 10
truck_weights= [ 7 , 4 ,5 ,6]
a  = solution(bridge_length , weight , truck_weights)
print(a)