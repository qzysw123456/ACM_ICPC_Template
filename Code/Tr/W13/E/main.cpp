#include <cstdio>
#include<queue>
#include<cstring>
#include<algorithm>
#include<map>
#include<cstring>
using namespace std;
#define MAXN 440
#define SET(a,b) memset(a,b,sizeof(a))
deque<int> Q;
//g[i][j]��Ź�ϵͼ��i,j�Ƿ��б�,match[i]���i��ƥ��ĵ�
//��ͼ��ʼ��ʼ��g
//����ƥ�䷽��Ϊmatch
//���Ӷ�O(n^3)
//���Ǵ�1��n��
bool g[MAXN][MAXN],inque[MAXN],inblossom[MAXN],inpath[MAXN];
int match[MAXN],pre[MAXN],base[MAXN];

//�ҹ�������
int findancestor(int u,int v)
{
    memset(inpath,false,sizeof(inpath));
    while(1)
    {
        u=base[u];
        inpath[u]=true;
        if(match[u]==-1)break;
        u=pre[match[u]];
    }
    while(1)
    {
        v=base[v];
        if(inpath[v])return v;
        v=pre[match[v]];
    }
}

//ѹ����
void reset(int u,int anc)
{
    while(u!=anc)
    {
        int v=match[u];
        inblossom[base[u]]=1;
        inblossom[base[v]]=1;
        v=pre[v];
        if(base[v]!=anc)pre[v]=match[u];
        u=v;
    }
}

void contract(int u,int v,int n)
{
    int anc=findancestor(u,v);
    SET(inblossom,0);
    reset(u,anc);reset(v,anc);
    if(base[u]!=anc)pre[u]=v;
    if(base[v]!=anc)pre[v]=u;
    for(int i=1;i<=n;i++)
        if(inblossom[base[i]])
        {
            base[i]=anc;
            if(!inque[i])
            {
                Q.push_back(i);
                inque[i]=1;
            }
        }
}

bool bfs(int S,int n)
{
    for(int i=0;i<=n;i++)pre[i]=-1,inque[i]=0,base[i]=i;
    Q.clear();Q.push_back(S);inque[S]=1;
    while(!Q.empty())
    {
        int u=Q.front();Q.pop_front();
        for(int v=1;v<=n;v++)
        {
            if(g[u][v]&&base[v]!=base[u]&&match[u]!=v)
            {
                if(v==S||(match[v]!=-1&&pre[match[v]]!=-1))contract(u,v,n);
                else if(pre[v]==-1)
                {
                    pre[v]=u;
                    if(match[v]!=-1)Q.push_back(match[v]),inque[match[v]]=1;
                    else
                    {
                        u=v;
                        while(u!=-1)
                        {
                            v=pre[u];
                            int w=match[v];
                            match[u]=v;
                            match[v]=u;
                            u=w;
                        }
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int solve(int n)
{
    SET(match,-1);
    int ans=0;
    for(int i=1;i<=n;i++)
        if(match[i]==-1&&bfs(i,n))
            ans++;
    return ans;
}
int A[404],B[105];
int n,m;
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++) scanf("%d",&A[i]);
        for(int i=0;i<m;i++) scanf("%d",&B[i]);
        sort(A,A+n);sort(B,B+m);
        map<int,int> mp;
        memset(g,0,sizeof(g));
        for(int i=0;i<m;i++) mp[B[i]]=1;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(mp[A[i]+A[j]])
                {
                    g[i+1][j+1]=g[j+1][i+1]=1;
                }
            }
        }
        printf("%d\n",solve(n));
    }
    return 0;
}
