"""
Created on May 09th 2022
@author: Silvana R Nobre
"""
import math

def PennsylvaniaYield(Age, SiteLst, ForestTypeLst, EcoRegionLst, Stock) -> float:
    # Gilabert, H., Manning, P.J., McDill, M.E., Sterner, S., 2010.
    #    Sawtimber yield tables for Pennsylvania forest management planning.
    #    North. J. Appl. For. 27, 140–150. https://doi.org/10.1093/njaf/27.4.140

    # Function to calculate Total Net sawtimber volume
    # coefficients
    #--------------------------------------------------
    # Intercepter; Age coefficient
    alfa = {0:9.65161,1:-79.67558}
   # Sites coefficients
    beta = {1:0.48990, 2:0, 3:-0.90516}
    # Forest Types coefficients
    phi = {1:0.23674, 2:0.55308, 3:0.05102, 4:0.31938, 5:0, 6:-0.04277, 7:0.46172}
    # Ecological Regions coefficients
    gamma = {}
    gamma[1] = -0.19182
    gamma[2] = 0
    gamma[3] = 0
    gamma[4] = 0
    gamma[5] = 0.37972
    gamma[6] = 0
    gamma[7] = 0
    gamma[8] = 0.40850
    gamma[9] = 0
    gamma[10] = 0
    gamma[11] = 0
    gamma[12] = 0
    gamma[13] = 0
    # Stock coefficients
    lda = {}
    lda["stocked"] = 0
    lda["understocked"] = -0.41902

    x_alfa = alfa[0]
    if Age > 0:
       x_alfa += alfa[1]/Age
    x_beta = 0
    for iSite in SiteLst:
        x_beta += beta[iSite]
    x_phi = 0
    for iFType in ForestTypeLst:
        x_phi += phi[iFType]
    x_gamma = 0
    for iERegion in EcoRegionLst:
        x_gamma += gamma[iERegion]
    x_lambda = lda[Stock]

    x = x_alfa + x_beta + x_phi + x_gamma + x_lambda
    x = math.exp(x)
    return x

if __name__ == '__main__':
    Age = 80
    SiteLst = [1]
    ForestTypeLst = [4]
    EcoRegionLst = [9]

    Stock = "stocked"
    NetVolume = PennsylvaniaYield(Age, SiteLst, ForestTypeLst, EcoRegionLst, Stock)
    print(NetVolume)

    Stock = "understocked"
    NetVolume = PennsylvaniaYield(Age, SiteLst, ForestTypeLst, EcoRegionLst, Stock)
    print(NetVolume)

    NetVolume = PennsylvaniaYield(30, [1], [1], [9], "stocked")
    print(NetVolume)



