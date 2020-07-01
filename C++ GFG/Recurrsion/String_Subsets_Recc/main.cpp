#include <iostream>

using namespace std;

void strSub(string str, string curr="", int index=0)
{
    int n = str.length();

    // base case
    if (index == n){
        cout << curr << " ";
        return;
    }


    strSub(str, curr, index+1);
    strSub(str, curr+str[index], index+1);
}

int main()
{
    string word;
    cout << "Enter a String : ";
    cin >> word;
    cout << " The Substring of the word ", word , " are ";
    strSub(word);
    return 0;
}
