#include <iostream>

using namespace std;

int maxCuts(int N, int A,int B, int C)
{
    if(N == 0)
        return 0;
    if(N < 0)
        return -1;

    int res = max(maxCuts(N-A,A,B,C),
                  maxCuts(N-B,A,B,C),
                  maxCuts(N-C,A,B,C));

    if(res == -1)
    {
        return -1;
    }
    return(res + 1);
}

int main()
{
    int n, a, b, c;
    cout << "Enter the length of rope : ";
    cin >> n;
    cout << "Enter length of first cut : ";
    cin >> a;
    cout << "Enter length of second cut : ";
    cin >> b;
    cout << "Enter length of third cut : ";
    cin >> c;
    cout << "Maximum number of Cuts is :" << maxCuts(n, a, b, c);
    return 0;
}
