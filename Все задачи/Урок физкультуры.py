def main():
    input()
    s = input()
    cnt = 0
    now, _set = -1, set()
    flag = True
    while now:
        # if s in _set:
        #     flag = False
        #     print(-1)
        #     break
        # _set.add(s)
        now = s.count('><')
        s = s.replace('><', '<>')
        cnt += now
    print(cnt)
    # if flag:
    #     print(-1 if now else cnt)

main()

# >><< -> ><>< -> <><>

# #include <iostream>
# #include <string>
# #include <algorithm>
# using namespace std;

# void replace_first(
#     std::string& s,
#     std::string const& toReplace,
#     std::string const& replaceWith
# ) {
#     std::size_t pos = s.find(toReplace);
#     if (pos == std::string::npos) return;
#     s.replace(pos, toReplace.length(), replaceWith);
# }

# int main()
# {
#     // string s = ">><<><";
#     // std::string x = "><", y = "<>";
#     //     while (true) {
#     //         string check = s;
#     //         replace_first(s, x, y);
#     //         if (check == s) {
#     //             break;
#     //         }
#     //     }
#     // cout << s;
#     int a;
#     cin >> a;
#     string s;
#     cin >> s;
#     int cnt = 0;
#     int now = -1;
#     while (now) {
#         int now= 0;
#         std::string x = "><", y = "<>";
#         while (true) {
#             string check = s;
#             replace_first(s, x, y);
#             if (check == s) {
#                 break;
#             }
#         }
#         cout << s << ' ' << cnt << '\n';
#         cnt += now;
#     }
#     cout << cnt;

#     return 0;
# }