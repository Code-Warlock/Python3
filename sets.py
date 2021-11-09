""" Sets in Python """
x = {1,3,5}
y = {2,7,5}
x.union(y)
x.intersection(y)
y.difference(x)
x.add(9)
x.remove(1)
name = {"Desmond","Michael","David",34}
names = ["Vegetables","Michael","Julia", "Pytar"]
reset = set(names)
reset.add("Vegetables")
reset.symmetric_difference_update(name)
