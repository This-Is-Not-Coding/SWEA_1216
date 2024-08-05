for _ in range(1, 11):
    tc = int(input())
    result = 0
    arr = [list(input()) for _ in range(100)] # 행 검사
    arrT = [list(i) for i in zip(*arr)] # 열 검사

    result = 0
    cnt1, cnt2 = 0, 0

    for k in range(100, 0, -1): # 검사 길이
        for i in range(100): # 검사 시작 위치 (행)
            for j in range(100): # 검사 시작 위치 (열)
                if j+k > 100 : break # 범위 벗어나면 다음 행 검사
                word1 = arr[i][j:j+k] # 검사하는 단어 (기존행렬)
                word2 = arrT[i][j:j+k] # 검사하는 단어 (전치행렬)

                # 회문여부 확인 후, 단어 길이 측정
                if word1 == word1[::-1]:
                    cnt1 = len(word1)
                elif word2 == word2[::-1]:
                    cnt2 = len(word2)
                result = max(cnt1, cnt2) # 결과값 업데이트

            if result != 0 : break # 결과값이 있으면 종료
        if result != 0 : break

    print(f'#{tc} {result}')