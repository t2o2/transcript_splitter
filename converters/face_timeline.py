import os
import re
from pprint import pprint as pp


timeline = {}

for c in os.listdir('face_clusters'):
    timeline[c] = []
    for f in os.listdir(os.path.join('face_clusters', c)):
        matched = re.match('face_(?P<time>\d+)s_(?P<idx>\d+)\.jpg', f)
        if matched:
            t = matched.group('time')
            timeline[c].append(int(t))
    timeline[c] = sorted(timeline[c])

pp(timeline)
