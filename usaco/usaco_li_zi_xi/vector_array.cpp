#include <iostream>
#include <vector>
using namespace std;

void outputVec(const vector<int> &vec)
{
    cout << "Vector elements: ";
    for (int item : vec)
    {
        cout << item << " ";
    }
    cout << endl;
}

int main()
{
    // initialize a vector of integers
    // No.1
    vector<int> vec;
    for (int item : vec)
    {
        cout << "vec item:" << item << endl; // (no output)
    }
    // No.2
    vector<int> vec2(5); // size 5
    for (int item : vec2)
    {
        cout << "vec2 item:" << item << endl; // 0 0 0 0 0
    }
    // No.3
    vector<int> vec3(5, 1); // size 5, all elements initialized to 1
    for (int item : vec3)
    {
        cout << "vec3 item:" << item << endl; // 1 1 1 1 1
    }
    // No.4
    vector<int> vec4 = {1, 2, 3, 4, 5}; // initializer list
    for (int item : vec4)
    {
        cout << "vec4 item:" << item << endl; // 1 2 3 4 5
    }

    // push data to end of vector
    vec.push_back(10);
    int vec_back = vec.back();
    cout << "Vec Last element: " << vec_back << endl; // 10
    vec.pop_back();

    // get size of vector
    cout << "Size of vector: " << vec.size() << endl;

    // access all elements
    for (int i = 0; i < vec.size(); i++)
    {
        cout << "Element " << i << ": " << vec[i] << endl;
        vec.erase(vec.begin() + i); // remove element at index i
    }

    // access all elements using range-based for loop
    for (int val : vec) // for (auto val : vec)
    {
        cout << "Value: " << val << endl;
    }

    // iterate using iterator
    vec = {1, 2, 3, 4};
    for (auto it = vec.begin(); it != vec.end(); ++it)
    {
        cout << "Iterator Value: " << *it << endl;
    }
    // insert element at specific position
    vec.insert(vec.begin() + 2, 5);         // insert 5 at the beginning
    outputVec(vec);                         // 1 2 5 3 4
    vec.insert(vec.begin() + 2, {6, 7, 8}); // insert multiple elements
    outputVec(vec);                         // 1 2 6 7 8 5 3 4
    vec.insert(vec.end(), 2, 100);          // insert two 100s before the last element
    outputVec(vec);                         // 1 2 6 7 8 5 3 4 100 100

    return 0;
}
