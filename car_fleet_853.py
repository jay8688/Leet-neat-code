# https://blog.csdn.net/fuxuemingzhu/article/details/81867361

一遍就AC的题还是很有成就感的。

我的想法是这样的，把车按照位置大小进行排序，计算出每个车在无阻拦的情况下到达终点的时间，如果后面的车到达终点所用的时间比前面车小，那么说明后车应该比前面的车先到。但是由于后车不能超过前车，所以这种情况下就会合并成一个车队，也就是说后车“消失了”。

然后像这种需要判断是否存在的题目一般都是用栈进行解决，对时间遍历，把哪些应该消失的车不进栈就行了
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/81867361
版权声明：本文为博主原创文章，转载请附上博文链接！


c++
https://www.cnblogs.com/grandyang/p/10540136.html
