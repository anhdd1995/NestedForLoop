print('\t\t\t----------MULTIPULATION TABLE----------')
for i in range(1, 10):
    print('\t%4d' % (i), end='')
print()
print('------------------------------------------------------------------------')
for j in range(1, 10):
    print('%d|' % (j), end='')
    for k in range(1, 10):
        print('\t%4d' % (j * k), end='')
    print('\n')