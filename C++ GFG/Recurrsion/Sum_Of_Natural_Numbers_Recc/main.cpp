#include <iostream>

using namespace std;

int natSum(int N)
{
    if(N == 0)
        return 0;
    else
        return N + natSum(N - 1);
}

int main()
{
    int num;
    cout << "Enter a number ";
    cin >> num;
    cout << "The sum is : " << natSum(num);
    return 0;
}
