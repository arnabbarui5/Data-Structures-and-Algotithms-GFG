#include <iostream>

using namespace std;

int sumOfDigits(int N)
{
    if(N < 10)
        return N;
    else
        return sumOfDigits(N/10) + N%10;
}

int main()
{
    int num;
    cout << "Enter a number Please : ";
    cin >> num;
    cout << "The Sum of Digits is : " << sumOfDigits(num);
    return 0;
}
