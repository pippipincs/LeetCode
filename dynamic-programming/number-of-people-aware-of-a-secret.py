class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp=[0]*n
        dp[0]=1
        share=0
        for i in range(1,n):
            if i-delay>=0:
                share=(share+dp[i-delay])%(10**9+7)
            if i-forget>=0:
                share=(share-dp[i-forget])%(10**9+7)
            dp[i]=share
        res=0
        for j in range(n-1-forget+1,n):
            res=(res+dp[j])%(10**9+7)
        return res
        