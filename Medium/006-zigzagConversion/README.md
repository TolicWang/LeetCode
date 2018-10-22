边界情况：<br>
输入：`s = '',numRow=1`<br>
输出： `''`

输入：`s = 'A',numRow=1`<br>
输出： `A`

输入：`s = 'AB',numRow=1`<br>
输出： `AB`

输入：`s = 'AB',numRow=2`<br>
输出： `AB`

### 1.我的解（128ms)：
如图所示：

![p1](./p1.png)

第一步：求索引，红色数字为左右两个字符之间间隔 `space`，且为第0行或者第`numRaw-1`行时，`space=k`;其余情况时当前字符的索引加上space即为下一个字符的索引；<br>
第二步：按索引遍历一次；<br>

[源码点击](m1.py)
### 2.最优解（84ms)
第一步：建立一个元素个数为numRows的list,即 ` l=[""] * numRows`;
第二步：遍历 `s`中的所有字符，按条件加入到`l`中，如上图中的`a~u`在`l`中的存在形式为：`l=["aiq","bhjpr","cgkos","dflnt","emu"]`<br>

[源码点击](m2.py)<br>