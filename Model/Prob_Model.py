class Prob_model:
    def P_LoS(self):
        value = 0
        return value
    def P_NLos(self):
        value = Prob_model.P_LoS()
        return 1-value

    def PL_LoS(self):
        value = 0
        return value

    def PL_NLoS(self):
        value = 0
        return value

    def Average_Pathloss(self):
        PL_LoS = Prob_model.PL_LoS()
        PL_NLoS = Prob_model.PL_NLoS()

        value = PL_NLoS + PL_LoS

        return value

