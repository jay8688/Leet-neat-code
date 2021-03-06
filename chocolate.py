# https://www.1point3acres.com/bbs/thread-499490-1-1.html


首先要知道利口1014/410问的东西和这题很像但是不一样：
- 原题问的是把最大值尽可能变小，总共要K份
可以把他想成一个Bar Graph，每一个subarray sum是一个Bar，总共要至少K个Bar，而且最高的那个Bar不得超过二分法猜的 Target．二分法的过程中我们要尽可能的把那个Target压小，直到Target再小一格的话就达不到 K 个Bar了．使用左闭右开的二分法模板，最后left的数值是“符合条件的最小数字”，在这一题的条件就是至少要K个Bar，而每个Bar都不能超过猜测的Target ，所以left 会得到最小化的最大值．

- 这题问的是把最小值尽可能变大，总共要K份
同理，我们也把题目想成一个Bar Graph，每一个subarray sum 是一个Bar，总共至少K个Bar，而这一次我们要让所有的Bar都至少达标一个猜测的Target，这样Target就是Bar Graph的最小值．二分法的过程中我们要尽可能的把这个猜测的Target变大，直到再变大一格就没办法分成K份了．可是如果要把猜测的数值尽可能变大，就没办法直接套用左闭右开的二分法模板了．其他的二分法模板应该能解决，但我很任性就只想记一种模板，所以为何不把二分法确认的条件换一下？我们也可以去猜一个Target，要求每一个Bar 都要Target，但如果用了这个Target 就不足以分成K份了，找这个Target的最小值．也就是说：使用二分法会找到一个最小值的Target，虽然不能分成K份，但它已经小到再小一格就能分成K份了．使用左闭又开模板Left会得到这个Target，所以Left-1就刚刚好是能分成K份的最大化最小值．

如果对左闭右开的二分法模板不熟，推荐去看油管一个叫花花酱的播主特辑第五章，讲得让人茅塞顿开，一种二分法模板打遍天下．
