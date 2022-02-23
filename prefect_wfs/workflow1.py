from prefect_wfs.algorithms.common.string import *

a = ["bananes", "pommes", "ananas", "poires", "mangues", "kiwis"]

x = replace(a, "bananes", "coconuts")
print(x)
x = split(x)
print(x)
x = concat(x)
print(x)