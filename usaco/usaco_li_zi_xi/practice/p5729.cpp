// #include<iostream>
// using namespace std;

// int main(){
//     int x , y , z ;
//     cin >> x >> y >> z;
//     bool o[x + 1][y + 1][z + 1];
//     int q ;
//     cin >> q;
//     for(int i = 1;i <= x; ++i ){
//         for(int w = 1;w <= y; ++w ){
//             for(int t = 1;t <= z; ++t ){
//                 o[i][w][t] = 1;
//             }
//         }
//     }

//     int x1, y1, z1, x2, y2, z2;
//     for (int d = 0; d < q; ++d)
//     { // iteration q times
//         cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
//         for(int i = x1;i <= x2; ++i )
//         {
//             for(int w = y1;w <= y2; ++w ){
//                 for(int t = z1;t <= z2; ++t ){
//                     o[i][w][t] = 0;
//                 }
//             }
//         }
//     }

//     int sum = 0;
//     for(int i = 1;i <= x; ++i ){
//         for(int w = 1;w <= y; ++w ){
//             for(int t = 1;t <= z; ++t ){
//                 sum += o[i][w][t];
//             }
//         }
//     }
//     cout << sum;
//     return 0;
// }

#include<iostream>
using namespace std;
char ch;
int main(){
	if(cin>>ch){//判断是否输入 
		if(ch>='a'&&ch<='z')ch+='A'-'a';//转换大小写 
		cout<<int(ch);//输出 
		main();//递归调用 
	} 
	return 0;//如果没有输入就退
}