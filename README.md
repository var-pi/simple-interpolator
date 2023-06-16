# What is it?

This package provides functionality for [bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation).
The current capabilities are the following:

- Computation of an [interpolant](https://en.wikipedia.org/wiki/Interpolation) function based on the [least sqares](https://en.wikipedia.org/wiki/Least_squares) method.

  - The interpolant is a [bilinear polynomial](https://en.wikipedia.org/wiki/Multilinear_polynomial).

  - The [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial) of the polynomial is chosen automatically so that it would provide a perfect fit for given set of [coordinates](https://en.wikipedia.org/wiki/Coordinate_system).

- Visualisation of the [bivariate](<https://en.wikipedia.org/wiki/Function_(mathematics)#Multivariate_function>) function.

- Mathematical representation of the interpolant polynomial.

# How to install it?

```shell
pip install simple-interpolator
```

> Find out more [here](https://pypi.org/project/simple-interpolator/).

# How to use it?

The library `simple_interpolator` provides a file `interpolator` encapsulating a class `Interpolator`.

```python
from simple_interpolator.interpolator import Interpolator
```

# `Interpolator` class

|             |                                                |
| :---------: | :--------------------------------------------- |
|  `show()`   | three-dimentional graph of the interpolant     |
|   `data`    | a list of the initial coordinates              |
|     `f`     | an interpolant function                        |
| `print_f()` | mathematical representation of the interpolant |

