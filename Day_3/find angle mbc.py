import math
ab = int(input())
bc = int(input())

hyp = math.hypot(ab, bc)
adj = bc

ang = int(round(math.degrees(math.acos(adj/hyp))))

ang = str(ang)

print(ang + '°')  #for degree symbol (alt+0176)
