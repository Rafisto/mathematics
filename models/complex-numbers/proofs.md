# De Movire formula induction proof

Prove the following
$z^n=r^n(cos(n\varphi )+isin(n\varphi ))$

For $n_0=1, T(1)$ the equation is:
$z=r(cos(\varphi )+isin(\varphi ))$<br>
Which is the definition of a polar form of a complex number, hence true<br>
For $n$ the equation is true from hypothesis<br>
Let's proove that $T(n)\implies T(n+1)$, if $T(n)$ is true then the following equality holds:<br>
$(cos(\varphi )+isin(\varphi ))^n=cos(n\varphi )+isin(n\varphi )$<br>
$(cos(\varphi )+isin(\varphi ))^{n+1}=(cos(n\varphi )+isin(n\varphi ))\cdot (cos\varphi +isin\varphi )=$<br>
$=cos(n\varphi )cos(\varphi) - sin(n\varphi )sin(\varphi) + i(sin(n\varphi )cos(\varphi) - cos(n\varphi )sin(\varphi))$<br>
Knowing that:<br>
$sin(a+b)=sin(a)cos(b)+cos(a)sin(b)$<br>
$cos(a+b)=cos(a)cos(b)-sin(a)sin(b)$<br>
We prove the above equals:<br>
$=cos((n+1)\varphi )+isin((n+1)\varphi )$, which finally implies:<br>
$z^n=r^n(cos(n\varphi )+isin(n\varphi ))_\blacksquare$