print('Program menghitung luas, volume, dan keliling balok')
p = int(input('masukan panjang balok: '))
l = int(input('masukan lebar balok: '))
t = int(input('masukan tinggi balok: '))
 
def luas_permukaan(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t) )
    return L
 
def volume(p,l,t):
    V = p * l * t
    return V
 
def keliling(p,l,t):
    k = 4 * (p + l + t)
    return k
 
 
print('Jadi balok dengan ukuran panjang: {}, lebar: {}, tinggi: {} \nMempunyai luas: {} , volume: {} , keliling: {}'.format(p,l,t, luas_permukaan(p,l,t), volume(p,l,t), keliling(p,l,t)))
