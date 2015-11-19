#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
	if (x < 0){
		return false;
	}
	if (x == 0){
		return true;
	};
	vector<int> l;
	while (x != 0){
		l.push_back(x%10);
		x /= 10;
	};
	int len = l.size();
	for (int i = 0; i < len; ++i){
		if (l[i] != l[len-i-1]){
			return false;
		}
	}
	return true;
    }
};
int main(int argc, char** argv){
	Solution sol;
	cout<<sol.isPalindrome(atoi(argv[1]))<<endl;
	return 0;
}
