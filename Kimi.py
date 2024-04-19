class Adat:
    def __init__(self, datum, hely, bef, kor, konstrukor, celbaErt, korh, hibaOk):
        self.datum = datum
        self.hely = hely
        self.bef = bef
        self.kor = kor
        self.konstruktor = konstrukor
        self.celbaErt = celbaErt
        self.korh = korh
        self.hibaOk = hibaOk

    def __str__(self):
        return f''