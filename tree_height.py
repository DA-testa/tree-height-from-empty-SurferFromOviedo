import sys
import threading
import numpy


def compute_height(n, parents):
    tree = {}
    for i in range(n):
        tree[i] = []

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    node_queue = [(root, 0)]

    max_depth = 0
    curr_depth = 0

    while node_queue:
        node, depth = node_queue.pop(0)
        curr_depth = depth
        if curr_depth > max_depth:
            max_depth = curr_depth
        for child in tree[node]:
            node_queue.append((child, curr_depth+1))

    return max_depth+1


def main():
    source = input()
    if source.upper() == "F":
        filename = input()
        while 'a' in filename:
            filename = input()
        try:
            with open(filename, 'r') as file:
                n = int(file.readline().strip())
                parents = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            sys.exit()
    else:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    pass

main()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
