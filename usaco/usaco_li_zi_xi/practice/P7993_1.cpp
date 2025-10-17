#include <iostream>
using namespace std;

int main()
{
    int N;
    string p;
    cin >> N >> p;
    int sum = 0;

    // 从头开始遍历每个字符
    for (int i = 0; i < N - 2; ++i)
    {
        int sum1 = 0; // sum of H
        int sum2 = 0; // sum of G
        for (char c : p.substr(i, 3))
        {
            c == 'H' ? sum1++ : sum2++;
        }
        sum += (sum1 == 1 || sum2 == 1) ? 1 : 0;

        for (int j = i + 3; j < N; ++j)
        {
            p[j] == 'H' ? sum1++ : sum2++;
            sum += (sum1 == 1 || sum2 == 1) ? 1 : 0;
            // 如果已经满足最少 2*H 且 2*G，那么后续的字符组成的照片一定「不是」孤独的照片
            if (sum1 >= 2 && sum2 >= 2)
            {
                break;
            }
        }
    }
    cout << sum;
    return 0;
}