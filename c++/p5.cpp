#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
	int len = s.length();
	vector<int> fs;
	char ch = ' ';
	int i = 0, j, k;
	while (i < len){
		j = i;
		while (j < len && s[j] == s[i]){
			j++;
		};
		fs.push_back((s[i]-'a')*1000+j-i);
		i = j;
	}
	int sz = fs.size();
	vector<int> f(sz, 1);
	vector<int> g(sz, 0);
	int l, r, ans = 0;
	for (i = 0; i < sz; ++i){
		g[i] = fs[i]%1000;
		if (g[i] > ans){
			ans = g[i];
			l = i;
			r = i;
		};
		cout<<i<<' '<<fs[i]<<' '<<f[i]<<' '<<g[i]<<endl;
	};
	for (i = 1; i < sz; ++i){
		if (i-f[i-1] > 0){
			k = i-f[i-1]-1;
			if (fs[k] == fs[i]){
				f[i] = f[i-1]+2;
				g[i] = g[i-1]+2*(g[i]);
				if (g[i] > ans){
					ans = g[i];
					l = k;
					r = i;
				};
			};
		};
	};
	string anss = "";
	for (i = l; i <= r; ++i){
		anss += ('a'+(fs[i]/1000))*(fs[i]%1000);
	};
	return anss;  
    };
};
int main(int argc, char** argv){
	Solution s;
	cout<<s.longestPalindrome(argv[1])<<endl;
	return 0;
}
