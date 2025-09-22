# Taylor Series

Goal: generate a taylor series of the general form

$$
\sum_{n=0}^{\infty} \frac{f^n(a)}{n!} (x-a)^2
$$

Without storing the explicit derivatives of functions, use the estimator

$$
\hat{f}^{(n)}(x) = \frac{\hat{f}^{(n-1)} (x+\epsilon) - \hat{f}^{(n-1)} (x-\epsilon)}{2\epsilon}
$$

- where $\epsilon$ is the machine epsilon (i.e. smallest number in floating point calculations).
- and $f^{(n)}(x) \approx \hat{f}^{(n)}(x)$

The approximator $\hat{f}(x)$ should be used recursively to approximate higher order derivatives.
