import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Solution {
    private static char[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int tc=0; tc<10; tc++) {
            int n = Integer.parseInt(br.readLine());

            arr = new char[100][100];

            for(int i=0; i<100; i++) {
                arr[i] = br.readLine().toCharArray();
            }

            for(int i=100; i>=1; i--) {
                if(isPalindrome(i)) {
                    System.out.println("#" + n + " " + i);
                    break;
                }
            }
        }

        br.close();
    }

    private static boolean isPalindrome(int len) {
        for(int i=0; i<100; i++) {
            for(int j=0; j<100-len+1; j++)  {
                if(arr[i][j] == arr[i][j+len-1]) {
                    boolean check = true;

                    for (int k=1; k<len/2; k++) {
                        if (arr[i][j+k] != arr[i][j+len-k-1]) {
                            check = false;
                            break;
                        }
                    }

                    if(check) {
                        return true;
                    }
                }

                if(arr[j][i] == arr[j+len-1][i]) {
                    boolean check = true;

                    for(int k=1; k<len/2; k++) {
                        if(arr[j+k][i] != arr[j+len-k-1][i]) {
                            check = false;
                            break;
                        }
                    }

                    if(check) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}