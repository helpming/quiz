from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_in_line = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = 0
    current_weight = 0

    while truck_in_line:
        time += 1

        current_weight -= bridge.popleft()
        
        if current_weight + truck_in_line[0] <= weight:
            truck = truck_in_line.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    time += bridge_length

    return time