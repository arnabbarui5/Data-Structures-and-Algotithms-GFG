#include <iostream>

using namespace std;

int fibo(int N)
{
    if(N <= 1)     // For handle Base Cases N = 0 & N = 1
        return N;
    else
        return fibo(N-1) + fibo(N-2);
}

int main()
{
    int num;
    cout << "Enter a number : ";
    cin >> num;
    cout << "The Fibonacci Number is : " << fibo(num);
    return 0;
}
