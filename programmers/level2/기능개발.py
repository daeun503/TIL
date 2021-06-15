# 1회차
import math
def solution(progresses, speeds):
    answer = []

    # 며칠 후에 100%가 될 수 있는지
    dates_fix = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    # pop 용도로 리스트 복사
    dates = list(dates_fix)

    release = dates[0]          # 첫 번째 기능 배포까지 걸리는 시간 
    release_num = 1             # 첫 번째 기능 배포이므로  +1  
    dates.pop(0)                # 첫 번째 기능 리스트에서 삭제

    for date in dates_fix[1:]:
        if release >= date:     # n-1번째 기능 배포 시간 >= n 번째 기능 배포 시간 (같이 배포 가능) 
            release_num += 1    # 함께 배포 +1 
            dates.pop(0)        # 함께 배포하므로 리스트에서 삭제 
        else:                   # n-1번째 기능 배포 시간 < n 번째 기능 배포 시간 (뒤에꺼 늦게 배포)
            answer.append(release_num)  # n-1번째 개까지 우선 배포하는 걸로 리스트에서 추가
            release_num = 1             # 새로 n번째 배포 1부터 시작
            release = date              # n번째 배포까지 걸리는 시간으로 업데이트
            dates.pop(0)                # n번째 배포 리스트에서 삭제
    answer.append(release_num)

    return answer