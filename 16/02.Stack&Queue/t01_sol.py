def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length
    
    while len(bridge_on) != 0 :
        answer += 1
        print(answer)
        bridge_on.pop(0)
        if truck_weights:
            if(sum(bridge_on) + truck_weights[0] <= weight):
                bridge_on.append(truck_weights.pop(0))
            else:
                bridge_on.append(0)
    return answer



bridge_length = 2
weight = 10
truck_weights= [ 7 , 4 ,5 ,6]
a  = solution(bridge_length , weight , truck_weights)
print(a)