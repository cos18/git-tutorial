import matplotlib.pyplot as plt
import numpy as np

def trap_rain_water(heights):
  n = len(heights)
  if n == 0:
    return 0, []

  water_distribution = [0] * n

  left, right = 0, n - 1
  left_max, right_max = 0, 0
  while left < right:
    if heights[left] < heights[right]:
      if heights[left] >= left_max:
        left_max = heights[left]
      else:
        water_distribution[left] = left_max - heights[left]
      left += 1
    else:
      if heights[right] >= right_max:
        right_max = heights[right]
      else:
        water_distribution[right] = right_max - heights[right]
      right -= 1

  total_water = sum(water_distribution)
  return total_water, water_distribution

def visualize_rain_water(heights, total_water, water_dist):
  x = np.arange(len(heights))

  fig, ax = plt.subplots(figsize=(6, 3))

  ax.bar(x, heights, color='gray', label='Bar Height')
  ax.bar(x, water_dist, bottom=heights, color='blue', alpha=0.6, label='Water')

  ax.set_xticks(x)
  ax.set_xlabel('Index')
  ax.set_ylabel('Height')
  ax.legend()
  plt.show()