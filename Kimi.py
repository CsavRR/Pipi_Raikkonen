class Adat:
    def __init__(self, datum, nagydij, hely, bef, kor, konstrukor, celbaErt, korh, hibaOk):
        self.datum = datum
        self.nagydij = nagydij
        self.hely = hely
        self.bef = bef
        self.kor = kor
        self.konstruktor = konstrukor
        self.celbaErt = celbaErt
        self.korh = korh
        self.hibaOk = hibaOk


    
f = open('kimi.csv', 'rt', encoding='UTF-8')
f.readline()

lista = []

for sor in f:
    sor = sor.strip().split(';')
    lista.append(Adat(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6], sor[7], sor[8]))

print(f'3. feladat: {len(lista)}')

print('4. feladat: Magyar Nagydíj helyezései')
for celba in lista:
    if celba.nagydij == 'Magyar Nagydíj':
        if celba.celbaErt == 'I':
            print(f'{celba.datum}: {celba.hely} helyezés')