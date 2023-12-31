#include "testlib.h"
#include <cmath>
#include <cstdio>

#define AC 42
#define WA 43
char reportfile[50];

int main(int argc, char* argv[]) {
    /*
    * argv[1]: 輸入
    * argv[2]: 標準輸出
    * argv[3]: 測試結果輸出資料夾
    * stdin: 程式輸出
    */
    FILE* fin = fopen(argv[1], "r");
    FILE* fstd = fopen(argv[2], "r");
    sprintf(reportfile, "%s/judgemessage.txt", argv[3]);
    FILE* freport = fopen(reportfile, "w");

    int jn;
    while(~fscanf(fin, "%d", &jn) && jn != 0)
    {
        int ua, ub;
        int ls = 0, rs = 0;
        int jx, jy;
        scanf("%d %d", &ua, &ub);
        for(int i = 0; i < 2 * jn; ++i)
        {
            fscanf(fin, "%d %d", &jx, &jy);
            if(jx * ua + jy * ub < 0)++ls;
            else if(jx * ua + jy * ub > 0)++rs;
        }
        if(ls != jn || rs != jn){
            fprintf(freport, "ls=%d, rs=%d, jn=%d\n",ls,rs,jn);            
            return WA;
        }
    }

    return AC;
}