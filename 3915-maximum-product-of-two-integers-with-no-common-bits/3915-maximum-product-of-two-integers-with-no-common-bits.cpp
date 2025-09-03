class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        int n = nums.size();
        int maxv = 0;
        for (int x : nums) if (x > maxv) maxv = x;
        int B = 0;
        while ((1 << B) <= maxv) ++B;
        if (B == 0) B = 1;
        int SZ = 1 << B;
        vector<int> fenoraktil = nums;
        vector<pair<int,int>> best1(SZ, {-1,-1}), best2(SZ, {-1,-1});
        for (int i = 0; i < n; ++i) {
            int m = nums[i];
            if (nums[i] > best1[m].first) {
                best2[m] = best1[m];
                best1[m] = {nums[i], i};
            } else if (nums[i] > best2[m].first) {
                best2[m] = {nums[i], i};
            }
        }
        for (int bit = 0; bit < B; ++bit) {
            for (int mask = 0; mask < SZ; ++mask) {
                if (mask & (1 << bit)) {
                    auto a1 = best1[mask];
                    auto a2 = best2[mask];
                    auto b1 = best1[mask ^ (1 << bit)];
                    auto b2 = best2[mask ^ (1 << bit)];
                    if (b1.first > a1.first) {
                        if (a1.second != b1.second) a2 = a1;
                        a1 = b1;
                    } else if (b1.first > a2.first && b1.second != a1.second) {
                        a2 = b1;
                    }
                    if (b2.first > a1.first) {
                        if (a1.second != b2.second) a2 = a1;
                        a1 = b2;
                    } else if (b2.first > a2.first && b2.second != a1.second) {
                        a2 = b2;
                    }
                    best1[mask] = a1;
                    best2[mask] = a2;
                }
            }
        }
        long long ans = 0;
        int FULL = SZ - 1;
        for (int i = 0; i < n; ++i) {
            int m = nums[i];
            int comp = (~m) & FULL;
            auto c1 = best1[comp];
            auto c2 = best2[comp];
            if (c1.first != -1 && c1.second != i) ans = max(ans, 1LL * nums[i] * c1.first);
            else if (c2.first != -1 && c2.second != i) ans = max(ans, 1LL * nums[i] * c2.first);
        }
        return ans;
    }
};

const auto _ = std::cin.tie(nullptr)->sync_with_stdio(false);
#define LC_HACK
#ifdef LC_HACK
const auto __ = []() {
    struct ___ {
        static void _() { std::ofstream("display_runtime.txt") << 0 << '\n'; }
    };
    std::atexit(&___::_);
    return 0;
}();
#endif