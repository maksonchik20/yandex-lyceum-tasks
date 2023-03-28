#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;


int main()
{
    int n;
    cin >> n;
    vector<int> elements = {};
    vector<vector<int>> data = {};
    for (int i; i < n - 1; i++) {
        int a, b;
        cin >> a;
        cin >> b;
        vector<int> f = {a, b};
        data.push_back(f);
        if (*std::find(elements.begin(), elements.end(), a)) {
            elements.
        }
    }
    
    
    
    
    
    return 0;
}
