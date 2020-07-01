#include <iostream>

using namespace std;

int fact(int N)
{
    if(N == 0 || N == 1)
        return 1;
    else
        return N*fact(N-1);
}

int main()
{
    int num;
    cout << "Enter a number : ";
    cin >> num;

    cout << "The factorial of " << num << " is " << fact(num);
    return 0;
}
