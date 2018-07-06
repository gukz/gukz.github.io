## pickone
[714.Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)
给定一组某一stock在每一天的价格，买卖次数不限，每次买入必须在卖出之后，且每次卖出时都需要fee的手续费，求解最大的收益。
#### 分析
本题采用两种解法
+ 动态规划
+ 贪心算法
##### 动态规划
对于第i天的最大收益，应分成两种情况，一是该天结束后手里没有stock，可能是保持前一天的状态也可能是今天卖出了，此时令收益为cash；二是该天结束后手中有一个stock，可能是保持前一天的状态，也可能是今天买入了，用hold表示。由于第i天的情况只和i-1天有关，所以用两个变量cash和hold就可以，不需要用数组。C++代码如下：
```java
    int maxProfit(vector<int>& prices, int fee) {
        int cash=0;//the maxPro you have if you don't have a stock that day
        int hold=-prices[0];//the maxPro you have if you have a stock that day, if you have a stock the first day,hold=-prices[0]
        for(int i=1;i<prices.size();i++){
            cash=max(cash,hold+prices[i]-fee);//cash in day i is the maxvalue of cash in day i-1 or you sell your stock
            hold=max(hold,cash-prices[i]);
        }
        return cash;      
    }
```
这里需要注意cash和hold的初始值，最终输出cash，因为最后一天的情况一定是手里没有stock的。
##### 贪心算法
贪心选择的关键是找到一个最大后是不是能够卖掉stock，重新开始寻找买入机会。比如序列1 3 2 8，如果发现2小于3就完成交易买1卖3，此时由于fee=2，（3-1-fee）+(8-2-fee)<(8-1-fee)，所以说明卖早了，令max是当前最大price，当（max-price[i]>=fee）时可以在max处卖出，且不会存在卖早的情况，再从i开始重新寻找买入机会。c++代码如下：
```java
    int maxProfit(vector<int>& prices, int fee) {
        int profit=0;
        int curProfit=0;
        int minP=prices[0];
        int maxP=prices[0];
        for(int i=1;i<prices.size();i++){
            minP=min(minP,prices[i]);
            maxP=max(maxP,prices[i]);
            curProfit=max(curProfit,prices[i]-minP-fee);
            if((maxP-prices[i])>=fee){//can just sell the stock at maxP day.
                profit+=curProfit;
                curProfit=0;
                minP=prices[i];
                maxP=prices[i];
            }
        }
        return profit+curProfit;//the last trade have to be made if there is some profit
    }
```
curProfit记录了当前一次交易能得到的最大收益，只有当maxP-prices[i]>=fee时，才将curProfit累加到总的收益中。最后一次交易不需要考虑是否早卖了，所以直接累加最后一次的curProfit。
#### 总结
1. 动态规划的解法是优于贪心的，因为代码实现更加简洁。
2. 在开始coding前一定要确定好思路。

## Topic
### Array 133
#### [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/description/)
##### 我的解法
一开始王的思路就是使用递归的方式来实现, 每次向右侧或者下侧移动一步直到到达终点，可以很容易的写出代码，但是显示超时。
于是我想到在每一个格点上记录到达这个地方一共有多少种方法。
```java
    int res = 0;
    int [][]grid;
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        grid = obstacleGrid;
        moveNext(0, 0);
        return res;
    }
    private void moveNext(int curx, int cury){
        int w = grid.length;
        int h = grid[0].length;
        if(grid[curx][cury]==1) return;
        if (curx==w-1 && cury==h-1 && grid[curx][cury]==0){
            res += 1;
            return;
        }
        if (curx+1<w&&grid[curx+1][cury]==0){
            moveNext(curx+1,cury);
        }
        if(cury+1<h&&grid[curx][cury+1]==0){
            moveNext(curx, cury+1);
        }
    }
```

##### 答案
##### 总结
