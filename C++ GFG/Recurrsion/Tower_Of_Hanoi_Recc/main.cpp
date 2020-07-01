#include <iostream>

using namespace std;

void towerOfHanoi(int n , char A, char B, char C)
{
    if(n == 1)
    {
        cout << "Move rod 1 from " << A << " to " << C << endl;
        return 1 + 2*towerOfHanoi(n-1);
    }

    towerOfHanoi(n-1, A, C, B);
    cout << "Move rod " << n << " from " << A << " to " << C << endl;
    towerOfHanoi(n-1, B, A, C);
}

int main()
{
    int num;
    cout << "Enter the number of tower : ";
    cin >> num;
    towerOfHanoi(num, 'A', 'B', 'C');
    return 0;
}
