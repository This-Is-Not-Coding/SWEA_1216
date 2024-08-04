#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int expandAroundCenter(const string& s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

int main() {
    for (int t = 0; t < 10; ++t) {
        int n;
        cin >> n;

        vector<string> board(100);
        vector<string> transposed(100, string(100, ' '));

        for (int i = 0; i < 100; ++i) {
            cin >> board[i];
            for (int j = 0; j < 100; ++j) {
                transposed[j][i] = board[i][j];
            }
        }

        int result = 1;
        for (int i = 0; i < 100; ++i) {
            for (int j = 0; j < 100; ++j) {
                // 가로 방향 검사
                int len1 = expandAroundCenter(board[i], j, j);     // 홀수 길이
                int len2 = expandAroundCenter(board[i], j, j + 1); // 짝수 길이
                result = max({ result, len1, len2 });

                // 세로 방향 검사
                len1 = expandAroundCenter(transposed[j], i, i);     // 홀수 길이
                len2 = expandAroundCenter(transposed[j], i, i + 1); // 짝수 길이
                result = max({ result, len1, len2 });
            }
        }

        cout << "#" << n << " " << result << "\n";
    }

    return 0;
}