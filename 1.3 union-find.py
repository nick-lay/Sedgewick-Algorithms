#!/usr/bin/env python3
"""
"""
from collections import defaultdict

pair = ((3, 4),
        (4, 9),
        (8, 0),
        (2, 3),
        (5, 6),
        (2, 9),
        (5, 9),
        (7, 3),
        (4, 8),
        (5, 6),
        (0, 2),
        (6, 1))

id = dict()
for p, q in pair:
    id[p] = p
    id[q] = q

for p, q in pair:
    t = id[p]
    if t == id[q]:
        continue
    for k in id:
        if id[k] == t:
            id[k] = id[q]
    print(p, q, id)
