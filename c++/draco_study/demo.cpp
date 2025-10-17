#include <iostream>  //包含头文件iostream，包含输入输出流
using namespace std; // 使用标准命名空间std，包含cout、cin、endl等

int main()
{                                   // 主函数，程序从此处开始执行
    cout << "Hello World!" << endl; // 输出Hello World!
    cout << 3 + 1 << endl;          // output 4

    // array
    int arr[] = {1, 2, 3};

    // type conversion
    cout << (int)1.1 << endl;

    return 0; // 返回0，表示程序正常结束
}