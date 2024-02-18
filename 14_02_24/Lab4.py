def make_pizza(size, *toppings, base ):
    print(size,toppings, base)
    for topings in toppings:
        print(size,toppings,base)
    return toppings,size,base

shilpika = make_pizza(6, 'pepperoni', 'green', base='thin crust')

print(shilpika)