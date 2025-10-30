#include <iostream>
using namespace std;

int main()
{
    int max;
    cin >> max;
    for (int i = 1; i <= max; i++)
    {
        int num = i;
        int count1 = 0;
        bool isTarget = true;
        // 求出当前数字 i 的每一位数
        while (num > 0)
        {
            int r = num % 10;
            if (r == 4)
            {
                isTarget = false;
                break;
            }
            else if (r == 1)
            {
                count1 = count1 + 1;
                if (count1 >= 2)
                {
                    isTarget = false;
                    break;
                }
            }
            num = num / 10;
        }
        if (isTarget == true)
        {
            cout << i << " ";
        }
    }

    return 0;
}
