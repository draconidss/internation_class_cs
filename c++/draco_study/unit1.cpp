#include <iostream>     //包含头文件iostream，包含输入输出流
using namespace std;    //使用标准命名空间std，包含cout、cin、endl等

int main(){             //主函数，程序从此处开始执行
    // cout << 3 + 1 << endl; // output 4
    // cout << 5 / 2 << endl; // 
    // cout << 2 / 5 << endl; // 0
    // cout << 2 % 5 << endl; // 2
    // cout << 5 % 2 << endl; // 1 odd
    // cout << 6 % 2 << endl; // 0 even
    // cout << 0 % 2 << endl; // 0 even

    // int a, b, c;
    // cin >> a >> b >> c;
    // cout << a << " " << b << " " << c;

    int d = 5, e = 10;
    swap(d, e);
    cout << d << " " << e << endl;

    // 0*5+2 = 2
    return 0; // 返回0，表示程序正常结束
}