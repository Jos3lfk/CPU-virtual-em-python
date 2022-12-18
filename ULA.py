import Registradores as Rg


class InstrucoesLa:
    def __init__(self, a, b, c, d):
        Rg.r1 = a
        Rg.r2 = c
        Rg.r3 = d
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def mov_c_d(self):
        self.c = self.d

    def mov_d_c(self):
        self.d = self.c

    def mov_a_d(self):
        self.a = self.d

    def mov_d_a(self):
        self.d = self.a

    def mov_c_a(self):
        self.c = self.a

    def mov_a_c(self):
        self.a = self.c

    def add(self):
        self.a = self.a + self.b
        return self.a

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def inc(self):
        return self.a + 1

    def dec(self):
        return self.a - 1

    def beq(self):
        if self.c == self.d:
            return True
        else:
            return False

    def bne(self):
        if self.c != self.d:
            return True
        else:
            return False

    def blt(self):
        if self.c < self.d:
            return True
        else:
            return False

    def ble(self):
        if self.c <= self.d:
            return True
        else:
            return False

    def bge(self):
        if self.c > self.d:
            return True
        else:
            return False

    def bgt(self):
        if self.c >= self.d:
            return True
        else:
            return False
