
import numpy
import matplotlib.pyplot as mpl

""" Pressão no pedal low, PL{(0, 1), (50, 0)}"""


def press_pedal_low(ppl):
    if ppl >= 50:
        return 0.0
    elif ppl < 50:
        return (50 - ppl) / 50


""" Pressão no pedal medium, PM{(30, 0), (50, 1), (70, 0)}"""


def press_pedal_med(ppm):
    if 30 >= ppm or ppm >= 70:
        return 0.0
    else:
        if 30 < ppm <= 50:
            return (ppm - 30) / 20
        if 50 <= ppm < 70:
            return (70 - ppm) / 20


""" Pressão no pedal high, PH{(50, 0) (100, 1)}"""


def press_pedal_high(pph):
    if pph <= 50:
        return 0.0
    elif pph > 50:
        return (pph - 50) / 50


""" Velocidade da roda low, VRS{(0, 1), (60, 0)}"""


def vel_roda_slow(vrs):
    if vrs >= 60:
        return 0.0
    elif vrs < 60:
        return (60 - vrs) / 60


""" Velocidade da roda medium, VRM{(30, 0), (50, 1), (80, 0)}"""


def vel_roda_med(vrm):
    if 20 >= vrm or vrm >= 80:
        return 0.0
    else:
        if 20 < vrm <= 50:
            return (vrm - 20) / 30
        if 50 <= vrm < 80:
            return (80 - vrm) / 30


""" Velocidade da roda fast, VRF{(40, 0) (100, 1)}"""


def vel_roda_fast(vrf):
    if vrf <= 40:
        return 0.0
    elif vrf > 40:
        return abs((vrf - 40) / 60)


""" Velocidade do carro slow, VCS{(0, 1), (60, 0)}"""


def vel_carro_slow(vrs):
    if vrs >= 60:
        return 0.0
    elif vrs < 60:
        return (60 - vrs) / 60


""" Velocidade do carro medium, VCM{(30, 0), (50, 1), (80, 0)}"""


def vel_carro_med(vcm):
    if 20 >= vcm or vcm >= 80:
        return 0.0
    else:
        if 20 < vcm <= 50:
            return (vcm - 20) / 30
        if 50 <= vcm < 80:
            return (80 - vcm) / 30


""" Velocidade do carro fast, VCF{(40, 0) (100, 1)}"""


def vel_carro_fast(vcf):
    if vcf <= 40:
        return 0.0
    elif vcf > 40:
        return abs((vcf - 40) / 60)


def liberar(p):
    return (100 - p) / 100


def apertar(p):
    return p / 100


"""Rule 1: 
            Se a Pressão no pedal for média 
            aplicar o freio"""


def rule_1(pp):
    return press_pedal_med(pp)


"""Rule 2:  
            Se a Pressão no pedal for alta
            e a velocidade do carro for alta
            e a velocidade das rodas for alta
            aplicar o freio"""


def rule_2(pp, vc, vr):
    return min(press_pedal_high(pp), vel_carro_fast(vc), vel_roda_fast(vr))


"""Rule 3:  
            Se a Pressão no pedal for alta
            e a velocidade do carro for alta
            e a velocidade das rodas for baixa
            libera o freio"""


def rule_3(pp, vc, vr):
    return min(press_pedal_high(pp), vel_carro_fast(vc), vel_roda_slow(vr))


"""Rule 4: 
            Se a Pressão no pedal for baixa 
            aplicar o freio"""


def rule_4(pp):
    return press_pedal_low(pp)


x = numpy.arange(101).reshape(101, 1)

y_ppl = numpy.zeros(101).reshape(101, 1)
y_ppm = numpy.zeros(101).reshape(101, 1)
y_pph = numpy.zeros(101).reshape(101, 1)
y_vrs = numpy.zeros(101).reshape(101, 1)
y_vrm = numpy.zeros(101).reshape(101, 1)
y_vrf = numpy.zeros(101).reshape(101, 1)
y_vcs = numpy.zeros(101).reshape(101, 1)
y_vcm = numpy.zeros(101).reshape(101, 1)
y_vcf = numpy.zeros(101).reshape(101, 1)
y_a = numpy.zeros(101).reshape(101, 1)
y_l = numpy.zeros(101).reshape(101, 1)
y_r_a = numpy.zeros(101).reshape(101, 1)
y_r_l = numpy.zeros(101).reshape(101, 1)
y_c = numpy.zeros(101).reshape(101, 1)
var = 0
while var < 101:
    y_ppl[var] = press_pedal_low(x[var])
    y_ppm[var] = press_pedal_med(x[var])
    y_pph[var] = press_pedal_high(x[var])
    y_vrs[var] = vel_roda_slow(x[var])
    y_vrm[var] = vel_roda_med(x[var])
    y_vrf[var] = vel_roda_fast(x[var])
    y_vcs[var] = vel_carro_slow(x[var])
    y_vcm[var] = vel_carro_med(x[var])
    y_vcf[var] = vel_carro_fast(x[var])
    y_a[var] = apertar(x[var])
    y_l[var] = liberar(x[var])
    y_r_a[var] = apertar(x[var])
    y_r_l[var] = liberar(x[var])
    var = var + 1

print("Entre com os valores de pressão no pedal, velocidade do carro e velocidade das rodas\n")
inp_pp = float(input("Pressão no pedal: "))
inp_vc = float(input("Velocidade do carro: "))
inp_vr = float(input("Velocidade das rodas: "))

r1 = rule_1(inp_pp)
r2 = rule_2(inp_pp, inp_vc, inp_vr)
r3 = rule_3(inp_pp, inp_vc, inp_vr)
r4 = rule_4(inp_pp)

r_a = r1 + r2
r_l = r3 + r4


var = 0
while var < 101:
    if y_r_a[var][0] > r_a:
        y_r_a[var][0] = r_a
    if y_r_l[var][0] > r_l:
        y_r_l[var][0] = r_l
    var = var + 1

pax = 0
pa = 0
var = 0
while var < 101:
    if y_r_a[var][0] >= y_r_l[var][0]:
        pax = pax + (y_r_a[var][0] * var)
        pa = pa + (y_r_a[var][0])
    else:
        pax = pax + (y_r_l[var][0] * var)
        pa = pa + (y_r_l[var][0])
    var = var + 1

var = 0
while var < 101:
    y_c[var][0] = pax / pa
    var = var + 1

print("A pressão aplicada é " + str(pax / pa))

mpl.figure(1)
mpl.subplot(3, 1, 1)
mpl.plot(x, y_ppl, '-', label='L')
mpl.plot(x, y_ppm, '-', label='M')
mpl.plot(x, y_pph, '-', label='H')
mpl.ylabel("input: "+str(inp_pp)+'\nPressão\nno pedal')
mpl.legend()

mpl.subplot(3, 1, 2)
mpl.plot(x, y_vrs, '-', label='S')
mpl.plot(x, y_vrm, '-', label='M')
mpl.plot(x, y_vrf, '-', label='F')
mpl.ylabel("input: "+str(inp_vr)+'\nVelocidade\ndas rodas')
mpl.legend()

mpl.subplot(3, 1, 3)
mpl.plot(x, y_vcs, '-', label='S')
mpl.plot(x, y_vcm, '-', label='M')
mpl.plot(x, y_vcf, '-', label='F')
mpl.ylabel("input: "+str(inp_vc)+"\nVelocidade\ndo carro")
mpl.legend()


mpl.figure(2)
mpl.subplot(2, 1, 1)
mpl.plot(x, y_a, '-', label='A')
mpl.plot(x, y_l, '-', label='L')
mpl.title('Liberar freio X Apertar freio')
mpl.legend()

mpl.subplot(2, 1, 2)
mpl.plot(x, y_r_a, '-', label='A')
mpl.plot(x, y_r_l, '-', label='L')
mpl.plot(y_c, y_r_a, '-', label='C')
mpl.xlabel('Grau em que o freio é aplicado ( ' + str(pax / pa) + " )")
mpl.legend()

mpl.show()
