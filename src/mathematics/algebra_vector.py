import numpy as np

#==============================================================================
# VECTOR
# - Magnitude
# - Cosine Angle
#==============================================================================
v = np.array([3, 4])
w = np.array([5, 6])

v_magnitude = np.linalg.norm(v)
w_magnitude = np.linalg.norm(w)
cosine_angle = np.dot(v, w) / (v_magnitude * w_magnitude)

print(f"""
Given 2 vectors in Euclidian space, where
- v: [{v[0]}, {v[1]}] has magnitude of {v_magnitude}
- w: [{w[0]}, {w[1]}] has magnitude of {w_magnitude}
cosine angle between v and w is {cosine_angle:.2f}
""")
