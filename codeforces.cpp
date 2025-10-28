/*
 * =====================================================
 * Codeforces Problem Solution Template
 * =====================================================
 * Platform: Codeforces
 * Author: [Your Name]
 * Problem: [Problem Code - Problem Name]
 * Link: [Problem URL]
 * =====================================================
 */

#include <bits/stdc++.h>
using namespace std;

// Type definitions for convenience
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

// Macros for fast coding
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define per(i, a, b) for(int i = (a); i >= (b); i--)

// Fast I/O
void fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

/*
 * =====================================================
 * EXAMPLE SOLUTION: Two Sum Problem
 * Problem: Find two numbers in array that sum to target
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * =====================================================
 */
void solve_example() {
    int n, target;
    cin >> n >> target;
    
    vi arr(n);
    rep(i, 0, n) cin >> arr[i];
    
    // Using hash map for O(n) solution
    unordered_map<int, int> seen;
    
    rep(i, 0, n) {
        int complement = target - arr[i];
        if(seen.find(complement) != seen.end()) {
            cout << seen[complement] + 1 << " " << i + 1 << "\n";
            return;
        }
        seen[arr[i]] = i;
    }
    
    cout << "IMPOSSIBLE\n";
}

/*
 * =====================================================
 * Main Function - Problem Solving Template
 * =====================================================
 */
void solve() {
    // Write your solution here
    
    // Example: Read input
    int n;
    cin >> n;
    
    // Process and solve
    // ...
    
    // Output result
    cout << "Answer" << "\n";
}

int main() {
    fast_io();
    
    // For multiple test cases
    int t = 1;
    cin >> t;
    
    while(t--) {
        solve();
    }
    
    return 0;
}
