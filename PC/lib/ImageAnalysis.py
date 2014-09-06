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

def hslToTargetRgb(hsl) :
    (H, S, L) = hsl
    if L < 0.1 :
        (R, G, B) = color.black  #black
    elif L > 0.40 :
        if S < 0.1 :
            (R, G, B) = color.white #white
        else :
            (R, G, B) = color.yellow
    else :
        H = int(H / 30.0) * 30

        if H == 330 : # red
            (R, G, B) = color.red
        elif H in (0, 30) : # orange
            (R, G, B) = color.orange
        elif H in (60, 90, 120) : # yellow
            (R, G, B) = color.yellow
        elif H == 150 : # green
            (R, G, B) = color.green
        elif H in (180, 210, 240, 270, 300) : #blue
            (R, G, B) = color.blue

        # delt = 1E9
        # for c in [color.red, color.green, color.blue, color.yellow, color.orange] :
        #     (Hc, Sc, Lc) = rgbToHsl(c)
        #     if abs(Hc-H) < delt :
        #         delt = abs(Hc-H)
        #         (R, G, B) = c
    return (R, G, B)





def trans(jpg) :
    (width, height) = jpg.size
    for x in range(width) :
        for y in range(height) :
            rgb = jpg.getpixel((x,y))
            (H, S, L) = rgbToHsl(rgb)
            # if L < 0.1 :
            #     S = 0.0
            #     L = 0.0
            # else:
            #     S = 1.0
            #     L = 0.5
            # H = int(H / 15.0)*15.0
            # rgb = hslToRgb((H, S, L))
            jpg.putpixel((x,y), hslToTargetRgb((H, S, L)))

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
