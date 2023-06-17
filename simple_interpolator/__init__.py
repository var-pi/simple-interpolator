from interpolator import Interpolator

# TODO delete me!

i = Interpolator([(2,5,-4),(6,3,-4),(3,-6,4),(4,-3,5),(5,-4,8)])

print("Provided coordinates:\n\n\t", i.data, "\n")

print("An interpolant:\n\n",end='\t')
i.print_f(1)

i.show(30)

# TODO delete me!