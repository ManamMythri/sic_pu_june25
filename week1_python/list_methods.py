ns=[10,30,3,3,9,5]
print(sorted(ns))
print(ns.remove(3))
print(ns)
element=12
ns=[1,2]

try:
    print(ns[2])
    ns.remove(element)
    print('hi')
except ValueError as e:
    print(f'{element} not found')

except Exception as e:
    print("An error occured at runtime may be while removing the element")
except:
    print(print(f'{element} was not found'))
    