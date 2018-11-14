# Phil Tenteromano
# 10/15/2018

# fibseries.py

# first 16 fib numbers, iterative algorithm
def fibSeries():
  f0, f1 = 1, 1

  # shift them, f_1 becomes new f_n
  for i in range(16):
    print("f_" + str(i) + ": ", f1)
    f0, f1 = f1, f0 + f1

fibSeries()

# output:
# f_0:  1
# f_1:  1
# f_2:  2
# f_3:  3
# f_4:  5
# f_5:  8
# f_6:  13
# f_7:  21
# f_8:  34
# f_9:  55
# f_10:  89
# f_11:  144
# f_12:  233
# f_13:  377
# f_14:  610
# f_15:  987
# f_16:  1597
