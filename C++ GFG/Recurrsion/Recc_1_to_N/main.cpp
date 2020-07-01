#include <iostream>

using namespace std;

void recc1toN(int N)
{
    if (N == 0)
        return;

    recc1toN(N-1);
    cout << N << " " << endl;
}

int main()
{
    int num = 10;
    recc1toN(num);
    return 0;
}
