from priority_queue_112 import PQ
import sys

pq = PQ()
num = sys.argv[1]
for i in range(int(num) + 1):
    for lines in sys.stdin:
        pq.insert(int(lines.strip()))
    while pq.size() > int(num):
        pq.delMax()
for i in range(int(num)):
    print(pq.delMax())
