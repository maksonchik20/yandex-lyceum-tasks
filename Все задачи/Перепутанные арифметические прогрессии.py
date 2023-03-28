def main():
    n = int(input())
    nums = input().split()

    for ind in range(1, n * 2):
        r = int(nums[ind]) - int(nums[0])
        flag = False
        for j in range(n):
            if str(int(nums[0]) + (r * j)) in nums:
                flag = True
            else:
                flag = False
                break
        if flag:
            break

    result = []
    for el in range(n):
        print(r)
        result.append(str(int(nums[0]) + (r * el)))
    print(" ".join(result))

    
main()


# #include <iostream>
# #include <iterator>
# #include <vector>
# #include <algorithm>
# #include <list>

# using namespace std;


# int main()
# {
#     int n;
#     cin >> n;
#     vector<int> elements = {};
#     vector<vector<int>> data = {};
#     for (int i; i < n - 1; i++) {
#         int a, b;
#         cin >> a;
#         cin >> b;
#         vector<int> f = {a, b};
#         data.push_back(f);
#         if (*std::find(elements.begin(), elements.end(), a)) {
#             elements.
#         }
#     }
    
    
    
    
    
#     return 0;
# }
