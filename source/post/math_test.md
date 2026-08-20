---
Title:   Math Rendering Test
Summary: A test post for LaTeX math formula rendering.
Authors: Puyu Wang
Date:    2026-04-03
Category: Test
Tags: [math, test, latex]
---

# Math Rendering Test

## Inline Math

Einstein's famous equation: $E = mc^2$

The quadratic formula: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

Euler's identity: $e^{i\pi} + 1 = 0$

## Display Math

Gaussian integral:

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

Maxwell's equations (Gauss's law):

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$

A matrix:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

Taylor series expansion:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n$$

## Mixed Content

Given a probability distribution $p(x)$, the entropy is defined as:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log p(x)$$

For continuous distributions, this becomes $H(X) = -\int p(x) \log p(x)\, dx$.

## Code Highlighting

Python:

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

JavaScript:

```javascript
const greet = (name) => `Hello, ${name}!`;
console.log(greet("World"));
```

SPARQL:

```sparql
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
  FILTER(?subject = <http://example.org/resource>)
}
```
