#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);

	int T;
	cin>>T;
	int i, j, t, hi=0, count=0, rep=0, atleastone=0, first=0;
	int N=0;
	for (t=0;t<T;t++){
		cin>>N;
		int types[N]{}, instances[N]{}, order[N]{};
		for (i=0;i<N;i++){
			cin>>hi;
			order[i] = hi;
			instances[hi-1]++;
		} 
		atleastone=0;
		for (i=0;i<N;i++){
			hi = order[i]-1;
			rep = instances[hi];

			if (rep == 1) continue;
			if (types[hi]) continue;
			
			count = 0;
			for (j=i;j<i+2*rep-1;j++){
				if (j>N-1) break;
				if (order[j]-1 == hi) count++;
				if (count==rep){
					types[hi] = 1;
					atleastone = 1;
					break;
				}
			}

		}
		first = 1;
		if (atleastone){
			for (i=0;i<N;i++){
				if (types[i]){
					if (!first) cout<<" ";
					cout<<i+1;
					first = 0;
				}
			}
			cout<<"\n";
		}
		else cout<<-1<<"\n";

		
	}

}
