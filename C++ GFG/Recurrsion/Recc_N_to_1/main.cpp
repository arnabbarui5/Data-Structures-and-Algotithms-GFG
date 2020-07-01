#include <iostream>

using namespace std;

void reccNto1(int N)
{
    if(N == 0)
        return;

    cout<< N <<endl;
    reccNto1(N-1);
}

int main()
{
    int num;
    cout <<"Enter a number : ";
    cin >> num;
    reccNto1(num);
    return 0;
}
