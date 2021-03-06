
def f(x):

    return round(-20.04 * x ** 3 + x ** 2 + 2*x -1, 4)
    # return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)

a = -10
b = 3
tol = 0.1
k_max = 6

import sys
sys.stdout = open("./iterations/nurlan_gssm.txt", "w+")

def gssm(a=a, b=b, tol=tol, k_max=k_max):
	r = (5 ** (1/2)) / 2
	x1 = a + (1 - r) * (b - a)
	f1 = f(x1)
	x2 = a + r * (b - a)
	f2 = f(x2)
	k = 0
	print(f"Iteration {k}\n"\
		  f"\tf(x) = -0.04 * X ^ 3 + X ^ 2 + X - 1\n"
		  f"\tr = (5 ^ (1/2)) / 2 = {r}\n"\
		  f"\tx1 = a + (1-r) * (b-a) = {x1}\n"\
		  f"\tf1 = f(x1) = {f1}\n"\
		  f"\tx2 = a + r * (b-a) = {x2}\n"\
		  f"\tf2 = f(x2) = {f2}\n"\
		  f"\tk = {k}\n\n")

	while k < k_max:
		k += 1
		print(f"Iteration {k}\n"\
			  f"1) k = {k}\n"\
			  f"2) f1 > f2 -> {f1} > {f2}\t{f1 > f2}")

		if f1 > f2:
			a = x1
			x1 = x2
			f1 = f2
			x2 = a + r * (b - a)
			f2 = f(x2)
			print(f"3) a = x1 = {a}\n"\
				  f"   x1 = x2 = {x1}\n"\
				  f"   f1 = f2 = {f1}\n"\
				  f"   x2 = a + r * (b-a) = {x2}\n"\
				  f"   f2 = f(x2) = {f2}\n\n")
		else:
			b = x2
			x2 = x1
			f2 = f1
			x1 = a + (1 - r) * (b - a)
			f1 = f(x1)
			print(f"3) b = x2 = {b}\n"\
				  f"   x2 = x1 = {x2}\n"\
				  f"   f2 = f1 = {f2}\n"\
				  f"   x1 = a + (1-r) * (b-a) = {x1}\n"\
				  f"   f1 = f(x1) = {f1}\n\n")
	print(f"x1 = {x1}\n"\
		  f"f1 = {f1}\n"\
		  f"k = {k}\n"\
		  f"abs(b-a) = {abs(b-a)}")

if __name__ == '__main__':
	gssm()
