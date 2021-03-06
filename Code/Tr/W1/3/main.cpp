#include <cstdio>
#include<algorithm>
using namespace std;
int fa[100005],pre[100005];
int l[100005],r[100005],now=0;
int findfa(int x)
{
    if(x==fa[x]) return x;
    else
    {
       return fa[x]=findfa(fa[x]);
    }
}
int main()
{
    int n,m,op,x,y;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++) fa[i]=pre[i]=i;
    for(int i=1;i<=m;i++)
    {
        scanf("%d",&op);
        if(op==1)
        {
            scanf("%d%d",&x,&y);
            pre[x]=y;
            fa[x]=findfa(y);
        }
        if(op==2)
        {
            scanf("%d",&x);++now;
            l[now]=findfa(x);
            r[now]=x;
        }
        if(op==3)
        {
            scanf("%d%d",&x,&y);
            int L=l[y],R=r[y];
            bool f=false;
            while(R!=L)
            {
                if(R==x) f=true;
                R=pre[R];
            }
            if(L==x) f=true;
            if(f) printf("YES\n");
            else printf("NO\n");
        }
    }

    return 0;
}
