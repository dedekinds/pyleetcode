int genknuth(int m,int n)
{
    int i;
    for(i=0;i<n;i++)
        if(rand()%(n -i) < m) {
            printf("%d\n",i);
            m--;
        }
    return 0;
}
