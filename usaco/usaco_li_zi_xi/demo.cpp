#include <iostream>     //包含头文件iostream，包含输入输出流
using namespace std;    //使用标准命名空间std，包含cout、cin、endl等

const int a = 10;

int rand_func()
{
    int i,j;

    // 设置种子
    srand( time( NULL ) );

    /* 生成 10 个随机数 */
    for( i = 0; i < 10; i++ ){
        // 生成实际的随机数
        j= rand();
        cout <<"随机数： " << j << endl;
    }
    return 0;
}

int main(){             //主函数，程序从此处开始执行
    cout << "Hello World!" << endl;// 输出Hello World!
    cout << 3 + 1 << endl; // output 4
    cout << a;
    cout << rand_func() << endl;
    return 0; // 返回0，表示程序正常结束

}