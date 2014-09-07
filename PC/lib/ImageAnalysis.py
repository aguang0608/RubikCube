def rgbToHsl(rgb) :
    (R, G, B) = rgb
    (R, G, B) = (R/255.0, G/255.0, B/255.0)
    maxV = max(R, G, B)
    minV = min(R, G, B)

    if maxV == minV :
        H = 0.0
    elif maxV == R and G >= B :
        H = 60.0 * ( G - B ) / ( maxV - minV ) 
    elif maxV == R and G < B :
        H = 60.0 * ( G - B ) / ( maxV - minV ) + 360.0 
    elif maxV == G :
        H = 60.0 * ( B - R ) / ( maxV - minV ) + 120.0
    elif maxV == B :
        H = 60.0 * ( R - G ) / ( maxV - minV ) + 240.0

    L = ( maxV + minV ) / 2.0

    if abs(L) < 1E-9 or maxV == minV :
        S = 0.0
    elif 0.0 < L and L <= 0.5 :
        S = ( maxV - minV ) / ( 2.0 * L )
    elif L > 0.5 :
        S = ( maxV - minV ) / ( 2.0 - 2.0 * L )

    #print (H, S, L)

    return (H, S, L)

def hslToRgb(hsl) :
    (H, S, L) = hsl

    #print 'HSL = ',H,S,L
    if abs(S) < 1E-9 :
        (R, G, B) = (L, L, L)
    else :
        if L < 0.5 :
            q = L * ( 1.0 + S )
        else :
            q = L + S - ( L * S )
        p = 2.0 * L - q
        Hk = H / 360.0
        tR = Hk + 1.0/3.0
        tG = Hk
        tB = Hk - 1.0/3.0

        def colorTrans(tC) :

            if tC < 0.0 :
                tC += 1.0
            if tC > 1.0 :
                tC -= 1.0
            #print tC,p,q
            if tC < 1.0/6.0 :
                return p + ( ( q - p ) * 6.0 * tC )
            elif 1.0/6.0 <= tC and tC < 1.0/2.0 :
                return q
            elif 1.0/2.0 <= tC and tC < 2.0/3.0 :
                return p + ( ( q - p ) * 6.0 * ( 2.0/3.0 - tC ) )
            else :
                return p

        (R, G, B) = (colorTrans(tR), colorTrans(tG), colorTrans(tB))

        #print R, G, B
    (R, G, B) = (int(R * 255.0), int(G * 255.0), int(B * 255.0))

    return (R, G, B)

class color :
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 102, 0)
    toStr = {
        black  : 'black',
        white  : 'white',
        red    : 'red',
        green  : 'green',
        blue   : 'blue',
        yellow : 'yellow',
        orange : 'orange'
    }

def hslToTargetRgb(hsl) :
    # (H, S, L) = hsl
    # if L < 0.1 :
    #     (R, G, B) = color.black  #black
    # elif L > 0.58 :
    #     if S < 0.1 :
    #         (R, G, B) = color.white #white
    #     else :
    #         (R, G, B) = color.yellow
    # else :
    #     H = int(H / 30.0) * 30

    #     if H == 330 : # red
    #         (R, G, B) = color.red
    #     elif H in (0, 30) : # orange
    #         (R, G, B) = color.orange
    #     elif H in (60, 90) : # yellow
    #         (R, G, B) = color.yellow
    #     elif H in (120, 150) : # green
    #         (R, G, B) = color.green
    #     elif H in (180, 210, 240, 270, 300) : #blue
    #         (R, G, B) = color.blue

        # delt = 1E9
        # for c in [color.red, color.green, color.blue, color.yellow, color.orange] :
        #     (Hc, Sc, Lc) = rgbToHsl(c)
        #     if abs(Hc-H) < delt :
        #         delt = abs(Hc-H)
        #         (R, G, B) = c
    (H, S, L) = hsl
    targetHsl = {
        color.blue:(205.00, 0.33, 0.50),#blue
        #color.white:(168.00, 0.10, 0.70),#white
        color.red:(347.72, 0.19, 0.46),#red
        color.green:(155.67, 0.16, 0.37),#green
        color.orange:(17.894, 0.33, 0.60),#orange
        color.yellow:(84.578, 0.38, 0.56)#yellow
    }
    rgb = color.black
    disMin = 1E9
    for col in targetHsl :
        #print col
        (TH, TS, TL) = targetHsl[col]
        #print (TH, TS, TL)
        dis1 = (TH-H) if (TH>=H) else (TH-H+360)
        dis2 = (H-TH) if (H>=TH) else (H-TH+360)
        dis = dis1 if (dis1<dis2) else dis2
        if dis < disMin :
            disMin = dis
            rgb = col
    if rgb == color.green and L > 0.45 :
        rgb = color.white
    (R, G, B) = rgb

    return (R, G, B)



# blue.jpg
# DBL (97, 142, 176) (205.82278481012656, 0.3333333333333333, 0.5352941176470588)
# DBM (90, 134, 167) (205.71428571428572, 0.3043478260869565, 0.503921568627451)
# DLM (89, 132, 166) (206.4935064935065, 0.3019607843137255, 0.5)
# DBR (83, 125, 156) (205.47945205479454, 0.3054393305439331, 0.46862745098039216)
# DMM (77, 123, 155) (204.6153846153846, 0.33620689655172414, 0.45490196078431366)
# DFL (81, 126, 155) (203.5135135135135, 0.3135593220338983, 0.46274509803921565)
# DRM (76, 120, 150) (204.32432432432432, 0.32743362831858414, 0.44313725490196076)
# DFM (77, 121, 151) (204.32432432432432, 0.324561403508772, 0.44705882352941173)
# DFR (75, 117, 147) (205.0, 0.32432432432432423, 0.43529411764705883)
# white.jpg
# DBL (180, 198, 195) (169.99999999999994, 0.13636363636363633, 0.7411764705882353)
# DBM (178, 193, 186) (152.0, 0.10791366906474821, 0.7274509803921568)
# DLM (173, 187, 180) (150.00000000000006, 0.09333333333333317, 0.7058823529411764)
# DBR (168, 184, 181) (168.75000000000006, 0.10126582278481013, 0.6901960784313725)
# DMM (164, 179, 177) (172.0, 0.08982035928143699, 0.6725490196078432)
# DFL (158, 177, 171) (161.05263157894734, 0.10857142857142851, 0.6568627450980392)
# DRM (159, 174, 171) (167.99999999999994, 0.08474576271186443, 0.6529411764705882)
# DFM (156, 171, 166) (160.00000000000003, 0.08196721311475395, 0.6411764705882352)
# DFR (151, 166, 161) (159.99999999999997, 0.07772020725388604, 0.6215686274509804)
# red.jpg
# DBL (154, 108, 118) (346.95652173913044, 0.18548387096774188, 0.5137254901960784)
# DBM (149, 103, 113) (346.95652173913044, 0.18253968253968256, 0.49411764705882355)
# DLM (142, 96, 105) (348.2608695652174, 0.19327731092436978, 0.4666666666666667)
# DBR (140, 94, 104) (346.95652173913044, 0.1965811965811966, 0.45882352941176474)
# DMM (134, 88, 98) (346.95652173913044, 0.20720720720720723, 0.43529411764705883)
# DFL (136, 91, 101) (346.6666666666667, 0.19823788546255505, 0.44509803921568625)
# DRM (132, 88, 97) (347.72727272727275, 0.20000000000000004, 0.43137254901960786)
# DFM (130, 84, 94) (346.95652173913044, 0.21495327102803738, 0.41960784313725485)
# DFR (124, 84, 92) (348.0, 0.19230769230769232, 0.40784313725490196)
# green.jpg
# DBL (99, 126, 110) (144.44444444444446, 0.12000000000000002, 0.4411764705882353)
# DBM (86, 120, 106) (155.29411764705884, 0.16504854368932034, 0.403921568627451)
# DLM (86, 118, 104) (153.75, 0.1568627450980392, 0.4)
# DBR (78, 112, 96) (151.76470588235293, 0.17894736842105258, 0.37254901960784315)
# DMM (69, 106, 91) (155.67567567567568, 0.2114285714285715, 0.3431372549019608)
# DFL (69, 106, 93) (158.9189189189189, 0.2114285714285715, 0.3431372549019608)
# DRM (69, 104, 89) (154.28571428571428, 0.2023121387283237, 0.3392156862745098)
# DFM (70, 98, 86) (154.28571428571428, 0.16666666666666663, 0.3294117647058824)
# DFR (68, 97, 84) (153.10344827586206, 0.17575757575757575, 0.32352941176470584)
# orange.jpg
# DBL (199, 156, 133) (20.909090909090914, 0.37078651685393255, 0.6509803921568628)
# DBM (194, 149, 127) (19.70149253731344, 0.3544973544973544, 0.6294117647058823)
# DLM (188, 141, 121) (17.910447761194035, 0.3333333333333335, 0.6058823529411765)
# DBR (185, 140, 122) (17.142857142857153, 0.3103448275862068, 0.6019607843137255)
# DMM (179, 132, 116) (15.238095238095255, 0.2930232558139534, 0.5784313725490196)
# DFL (175, 131, 114) (16.72131147540982, 0.2760180995475113, 0.5666666666666667)
# DRM (173, 130, 115) (15.517241379310331, 0.26126126126126126, 0.5647058823529412)
# DFM (169, 128, 113) (16.071428571428577, 0.2456140350877193, 0.5529411764705883)
# DFR (165, 125, 108) (17.894736842105257, 0.24050632911392408, 0.5352941176470588)
# yellow.jpg
# DBL (169, 206, 119) (85.51724137931035, 0.47027027027027024, 0.6372549019607843)
# DBM (164, 198, 112) (83.72093023255813, 0.4300000000000001, 0.607843137254902)
# DLM (161, 195, 110) (84.0, 0.4146341463414633, 0.5980392156862745)
# DBR (155, 187, 107) (84.0, 0.37037037037037024, 0.5764705882352941)
# DMM (153, 186, 101) (83.29411764705883, 0.3811659192825112, 0.5627450980392157)
# DFL (152, 186, 104) (84.8780487804878, 0.3727272727272727, 0.5686274509803921)
# DRM (148, 181, 99) (84.14634146341463, 0.35652173913043483, 0.5490196078431373)
# DFM (146, 180, 97) (84.57831325301206, 0.3562231759656654, 0.5431372549019609)
# DFR (141, 172, 94) (83.84615384615384, 0.319672131147541, 0.5215686274509804)


def toTarget(jpg) :
    (width, height) = jpg.size
    for x in range(width) :
        for y in range(height) :
            rgb = jpg.getpixel((x,y))
            (H, S, L) = rgbToHsl(rgb)
            jpg.putpixel((x,y), hslToTargetRgb((H, S, L)))
    lsPoint = [[195, 65, 10, 'DBL'],[140, 105, 10, 'DBM'],[235, 120, 10, 'DLM'],[90, 145, 10, 'DBR'],[180, 160, 10, 'DMM'],[265, 165, 10, 'DFL'],[130, 190, 10, 'DRM'],[215, 200, 10, 'DFM'],[170, 225, 10, 'DFR']]
    for poi in lsPoint :
        (px, py, width, partX) = poi
        cnt = {
                color.black :   0,
                color.white :   0,
                color.red   :   0,
                color.green :   0,
                color.blue  :   0,
                color.yellow    :   0,
                color.orange    :   0
            }

        for x in range(px, px+width) :
            for y in range(py, py+width) :
                cnt[jpg.getpixel((x,y))] += 1
                jpg.putpixel((x,y), color.black)
        maxC = color.black
        for c in (color.black, color.white, color.red, color.green, color.blue, color.yellow, color.orange) :
            if cnt[c] > cnt[maxC] :
                maxC = c
        print partX, maxC, color.toStr[maxC]

def getTarget(jpg) :
    lsPoint = [[195, 65, 10, 'DBL'],[140, 105, 10, 'DBM'],[235, 120, 10, 'DLM'],[90, 145, 10, 'DBR'],[180, 160, 10, 'DMM'],[265, 165, 10, 'DFL'],[130, 190, 10, 'DRM'],[215, 200, 10, 'DFM'],[170, 225, 10, 'DFR']]
    for poi in lsPoint :
        (px, py, width, partX) = poi
        (SR, SG, SB) = (0, 0, 0)
        for x in range(px, px+width) :
            for y in range(py, py+width) :
                (R, G, B) = jpg.getpixel((x,y))
                SR += R
                SG += G
                SB += B
                jpg.putpixel((x,y), color.black)
        SR /= (width-1)*(width-1)
        SG /= (width-1)*(width-1)
        SB /= (width-1)*(width-1)
        (H, S, L) = rgbToHsl((SR, SG, SB))
        print partX, (SR,SG,SB), (H,S,L)



def medianFiltering(jpg) :
    (width, height) = jpg.size
    bef = {}
    for x in range(width) :
        for y in range(height) :
            bef[(x,y)] = jpg.getpixel((x,y))
    for x in range(width) :
        for y in range(height) :
            (r, g, b) = (0, 0, 0)
            for tx in range(x-1, x+2) :
                for ty in range(y-1, y+2) :
                    r += bef[( (tx+width)%width, (ty+height)%height )][0]
                    g += bef[( (tx+width)%width, (ty+height)%height )][1]
                    b += bef[( (tx+width)%width, (ty+height)%height )][2]
            r /= 9
            g /= 9
            b /= 9
            jpg.putpixel((x,y), (r,g,b))


