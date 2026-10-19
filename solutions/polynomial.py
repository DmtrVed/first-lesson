class Polynomial:
    def __init__(self, coeffs):
        coeffs = list(coeffs)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        if not coeffs:
            coeffs = [0]
        self._coeffs = coeffs

    @property
    def coeffs(self):
        return self._coeffs[:]

    def degree(self):
        return len(self._coeffs) - 1

    def __call__(self, x):
        result = 0
        for c in reversed(self._coeffs):
            result = result * x + c
        return result

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        n = max(len(self._coeffs), len(other._coeffs))
        result = [0] * n
        for i in range(n):
            a = self._coeffs[i] if i < len(self._coeffs) else 0
            b = other._coeffs[i] if i < len(other._coeffs) else 0
            result[i] = a + b
        return Polynomial(result)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        n = len(self._coeffs) + len(other._coeffs) - 1
        result = [0] * n
        for i, a in enumerate(self._coeffs):
            for j, b in enumerate(other._coeffs):
                result[i + j] += a * b
        return Polynomial(result)

    def derivative(self):
        if len(self._coeffs) == 1:
            return Polynomial([0])
        return Polynomial([i * self._coeffs[i] for i in range(1, len(self._coeffs))])

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return self._coeffs == other._coeffs

    def __repr__(self):
        return f"Polynomial({self._coeffs})"