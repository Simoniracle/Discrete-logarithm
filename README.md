# Discrete-logarithm
大体思路：

首先使用 pohlig-hellman 算法，将 g^e≡t(mod p)转化成 ai*e≡bi(mod p-1)，
通过大步小步法求出 ai，再使用中国剩余定理，最终求出 e 的最小值。

Pohlig-hellman 算法：

主要思想：

通过费马小定理和欧拉定理可以得知 g^(p-1) ≡1(mod p)。对于
a^e≡b(mod p)，记其原根为 g。则 a≡g^ai,b≡b^bi (原根的次幂可以
在[1,p-1]中一一对应，故必定存在)，即 g^(ai*e) ≡g^bi(mod p)。因此
根据指数和原根的性质，可以转化为求 ai*e≡bi(mod p-1)。通过求 ai,bi,
再使用拓展欧几里得算法可以求出所求的 e。
