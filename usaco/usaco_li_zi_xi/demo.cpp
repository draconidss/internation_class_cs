#include <iostream>  //包含头文件iostream，包含输入输出流
using namespace std; // 使用标准命名空间std，包含cout、cin、endl等

const int a = 10;

int rand_func()
{
    int i, j;

    // 设置种子
    srand(time(NULL));

    /* 生成 10 个随机数 */
    for (i = 0; i < 10; i++)
    {
        // 生成实际的随机数
        j = rand();
        cout << "随机数： " << j << endl;
    }
    return 0;
}

int main()
{                                   // 主函数，程序从此处开始执行
    cout << "Hello World!" << endl; // 输出Hello World!
    cout << 3 + 1 << endl;          // output 4
    cout << a;
    cout << rand_func() << endl;

    string str = "Hello World Hello";
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    cout << str << endl;

    reverse(str.begin(), str.end());
    cout << str << endl;

    string abc(str.rbegin(), str.rend());
    cout << str << endl;
    cout << abc << endl;

    int pos = str.find_last_of("aeiou");             // 查找最后一个元音字母
    cout << "最后一个元音字母位置: " << pos << endl; // 14 ('e')

    return 0; // 返回0，表示程序正常结束
}