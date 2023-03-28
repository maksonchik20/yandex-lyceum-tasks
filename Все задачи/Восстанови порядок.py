# # def main():
# #     n = int(input())
# #     elements = []
# #     data = []
# #     for _ in range(n - 1):
# #         a, b = map(int, input().split())
# #         data.append((a, b))
# #         if a in elements:
# #             elements.remove(a)
# #         elif a not in elements:
# #             elements.append(a)
# #         if b in elements:
# #             elements.remove(b)
# #         elif b not in elements:
# #             elements.append(b)
# #     for el in data:
# #         if el[0] == elements[1]:
# #             now = elements[1]
# #             break
# #         elif el[0] == elements[0]:
# #             now = elements[0]
# #             break
# #     result = [now]
# #     for _ in range(n):
# #         for el in data:
# #             if el[0] == now:
# #                 result.append(el[1])
# #                 now = el[1]
# #                 data.remove(el)
# #                 break
# #             elif el[1] == now:
# #                 result.append(el[0])
# #                 now = el[0]
# #                 data.remove(el)
# #                 break
# #     print(*result)
# # main()

# n = int(input())
# a = {}
# for _ in range(n-1):
#     a.update([tuple(map(int, input().split()))])
# p = n*(n+1)//2
# for i in a.values():
#     p -= i
# ans = [p]
# for i in range(n-1):
#     p = a[p]
#     ans.append(p)
#     print(p)
# print(*ans)

#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <list>
#include <map>

# using namespace std;


# int main()
# {
#     int n;
#     cin >> n;
#     std::map<int, int> m;
#     // m[0] = 5;
#     // m[1] = 2;
#     // for (const auto &myPair : m) {
#     //     cout << myPair.second;
#     // }
    
#     // cout << m[0][1];
#     for (int i = 0; i < n - 1; i ++) {
#         int a, b;
#         cin >> a;
#         cin >> b;
#         m[a] = b;
#     }
#     int s = n*(n+1)/2;
#     for (const auto &item : m) {
#         s -= item.second;
#     }
#     vector<int> ans = {};
#     ans.push_back(s);
#     // cout << s;
#     // for (const auto &myPair : m) {
#     //     cout << myPair.first << ' ' << myPair.second << '\n';
#     // }
#     // cout << m[s];
#     for (int i = 0; i < n - 1; i++) {
#         int s = m[s];
        
#         // ans.push_back(s);
#         cout << s + ' ';
#     }
#     // for (int i = 0; i < ans.size(); i++){
#     //     cout << ans[i] + ' ';
#     // }
#     return 0;
# }
