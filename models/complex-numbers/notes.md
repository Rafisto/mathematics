# Basic arithmetic of Complex numbers
Addition, Subtraction, Multiplication, Division

There are 3 form in which a complex number may be written:

- Base form
- Polar form
- Exponential form

Each of these forms is slightly different, we often change the form to ease up the calculations.

## Base form
Complex number in its base form is expressed by the following:<br>
$z=a+bi$<br>
We require a real part $a$ and an imaginary part $b$ to define $z$<br>
The basic arithmetic operations are defined below:<br>
$z_1+z_2=a+bi+c+di=(a+b)+(c+d)i$<br>
$z_1+z_2=a+bi-(c+di)=(a-c)+(b-d)i$<br>
$z_1\cdot z_2 = (a+bi)(c+di)=ac+adi+bci+bdi^2=(ac-bd)+(ad+bc)i$<br>
$\frac{z_1}{z_2}=\frac{a+bi}{c+di}\cdot \frac{c-di}{c-di}=\frac{ac-adi+bci-bdi^2}{c^2-d^2i^2}=\frac{ac+bd+i(bc-ad)}{c^2+d^2}=\frac{ac+bd}{c^2+d^2}+i\frac{bc-ad}{c^2+d^2}$<br>
The last two are rather time consuming to calculate by hand.

## Polar form
Complex number in its polar form is expressed by 
$z=r(cos\varphi+isin\varphi)$. It is now easier to multiply and divide. Then:<br>
We require a radius $r$ and an angle $\varphi$ to define $z$<br>
$z_1\cdot z_2=r_1r_2(cos(\varphi_1+\varphi_2)+isin(\varphi_1+\varphi_2))$<br>
$z_1\cdot z_2=\frac{r_1}{r_2}(cos(\varphi_1-\varphi_2)+isin(\varphi_1-\varphi_2))$<br>
Reasonably easier.

## Exponential form
Knowing euler formula $e^{i\varphi}=cos\varphi+isin\varphi$ we may also write $z=re^{i\varphi}$, then:<br>
We require a radius $r$ and an angle $\varphi$ to define $z$<br>
$z_1\cdot z_2=r_1r_2e^{i(\varphi_1+\varphi_2)}$<br>
$\frac{z_1}{z_2}=\frac{r_1}{r_2}e^{i(\varphi_1-\varphi_2)}$<br>
Simple and straightforward. Similar to the polar form.

## De Moivre formulas

$z^n=r^n(cos(n\varphi )+isin(n\varphi ))$<br>
$\sqrt[n]{z}=\sqrt[n]{r}(cos\frac{\varphi + 2k\pi}{n}+isin\frac{\varphi + 2k\pi}{n}), 0\le k\le n-1$<br>

These formulas can be used to find every solution to the following equation:<br>
$z^n-k=0,where\space z,k\in \mathbb{C} \space ,n\in \mathbb{Z}$<br>

### Solve for z in z^n=k equation

There is a simple algorithm to do so:
- Step 1 - Calculate $r=|z|$
- Step 2 - Calculate $\varphi=atan2(y,x)$, where $z=x+yi$
- Step 3 - For each $k\le n$ calculate the second de Moivre formula

Run deMoivre.py to get example equations:<br>
- z^3=-8 has 3 solutions: 1.0+1.73i; -2.0; 1.0-1.73i
- z^6=-64 has 6 solutions: 1.73+1.0i; 2.0i; -1.73+1.0i; -1.73-1.0i; -2.0i; 1.73-1.0i

