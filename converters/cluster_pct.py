import os
import re


shots = []
for f in os.listdir('frames'):
    matched = re.match('pic_(?P<time>\d+)s\.png', f)
    if matched:
        t = matched.group('time')
        shots.append(t)

print('Total seconds: {}'.format(len(shots)))

for c in os.listdir('face_clusters'):
    cluster_path = os.path.join('face_clusters', c)
    cluster_face_files = os.listdir(cluster_path)
    cluster_count = len(cluster_face_files)
    cluster_pct = cluster_count / len(shots)
    print('{}: {:.2f}%'.format(c, cluster_pct * 100))
