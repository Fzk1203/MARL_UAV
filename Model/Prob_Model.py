import math
import numpy as np
pi = math.pi
c = np.float64(299792458)
a = 9.61
b = 0.16
f = 2E9
eta_Los = 1
eta_NLos = 20
H = 100
d = 500

class Prob_model:
    def P_LoS(self, a, b, H, d):
        x = H / d
        if x < -1 or x > 1:
            return None  # Return None if H/d is outside the domain of arcsin
        y = math.asin(x)
        denominator = 1 + a * math.exp(-b * y - a)
        result = 1 / denominator
        return result
    def P_NLos(self, a, b, H, d):
        value = Prob_model.P_LoS(self, a, b, H, d)
        return 1-value

    def PL_LoS(self, d, f, pi, c, eta_LoS):
        value = 20*math.log10(d)+20*math.log10(f)+20*math.log10(4*pi/c)+eta_LoS
        return value

    def PL_NLoS(self, d, f, pi, c, eta_NLoS):
        value = 20*math.log10(d)+20*math.log10(f)+20*math.log10(4*pi/c)+eta_NLoS
        return value

    def Average_Pathloss(self):
        PL_LoS = Prob_model.PL_LoS()
        PL_NLoS = Prob_model.PL_NLoS()
        P_LoS = Prob_model.P_LoS()
        P_NLoS = Prob_model.P_NLos()
        value = PL_NLoS*P_NLoS + PL_LoS*P_LoS
        return value

