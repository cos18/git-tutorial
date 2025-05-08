samples = [
  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], # Figure 1과 비슷한 예시
  [4, 2, 0, 3, 2, 5],                   # 다양한 높낮이
  [2, 0, 2],                            # 양쪽이 막혀서 가운데에 물이 고이는 간단 예시
  [3, 1, 2, 5, 0, 3, 4],                # 더 복잡한 패턴
  [0, 0, 0, 0],                         # 전부 0인 경우 (물 고임 X)
  [5, 5, 5, 5]                          # 모두 같은 높이인 경우 (물 고임 X)
]

for i, heights in enumerate(samples, start=1):
  print(f"=== Sample #{i} ===")
  print("Heights:", heights)

  total, dist = trap_rain_water(heights)
  print(f"-> Total trapped water: {total}")

  visualize_rain_water(heights, total, dist)