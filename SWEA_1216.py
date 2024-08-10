'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

# T = int(input())
T = 10


for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''

    # test_case_number = readList[(test_case - 1) * 101]
    test_case_number = int(input())
    str_h_matrix = [input() for _ in range(100)]

    # str_h_matrix = readList[(test_case - 1) * 101 + 1: (test_case - 1) * 101 + 101]
    str_v_matrix = [''.join([line[i] for line in str_h_matrix]) for i in range(len(str_h_matrix[0]))]

    max_length = 1
    for i in range(len(str_h_matrix)):
        left_index = 0

        while left_index < len(str_h_matrix[0]) - max_length:
            left_h_char = str_h_matrix[i][left_index]
            left_v_char = str_v_matrix[i][left_index]

            right_index = len(str_h_matrix[0]) - 1

            while right_index - left_index + 1 > max_length:
                right_h_char = str_h_matrix[i][right_index]
                right_v_char = str_v_matrix[i][right_index]

                if left_h_char == right_h_char:
                    reverse_h_str = ''.join([str_h_matrix[i][j] for j in range(right_index, left_index - 1, -1)])
                    if str_h_matrix[i][left_index:right_index+1] == reverse_h_str:
                        max_length = right_index - left_index + 1
                        break

                if left_v_char == right_v_char:
                    reverse_v_str = ''.join([str_v_matrix[i][j] for j in range(right_index, left_index - 1, -1)])
                    if str_v_matrix[i][left_index:right_index+1] == reverse_v_str:
                        max_length = right_index - left_index + 1
                        break

                right_index -= 1

            left_index += 1

    print(f"#{test_case_number} {max_length}")
    # ///////////////////////////////////////////////////////////////////////////////////