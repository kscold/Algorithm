#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;

typedef long long ll;
typedef pair<ll, ll> p;

mt19937 rd;

ll n, per;
ll want;
vector<p> v;

int cnt(p x, p y){
	int ret = 0;
	for(auto i : v){
		ret += (y.y - x.y)*(i.x - x.x) == (i.y - x.y)*(y.x - x.x);
	}
	return ret;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> per; v.resize(n);
	if(n == 1){
		cout << "possible"; return 0;
	}
	if(n*per%100 == 0) want = n*per/100;
	else want = n*per/100+1;
	for(int i=0; i<n; i++) cin >> v[i].x >> v[i].y;

	rd = mt19937((unsigned)chrono::steady_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> ran(0, n-1);

	for(int loop=0; loop<150; loop++){
		int a = ran(rd);
		int b = ran(rd);
		while(a == b) b = ran(rd);
		if(cnt(v[a], v[b]) >= want){
			cout << "possible"; return 0;
		}
	}
	cout << "impossible";
}