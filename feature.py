def toText(n):
    n = int(n)
    if n<10:
        if n==1: return "uno"
        elif n==2: return "dos"
        elif n==3: return "tres"
        elif n==4: return "cuatro"
        elif n==5: return "cinco"
        elif n==6: return "seis"
        elif n==7: return "siete"
        elif n==8: return "ocho"
        else: return "nueve"
    elif n<100:
        if(n <20):
            if n==10: return "diez"
            elif n==11: return "once"
            elif n==12: return "doce"
            elif n==13: return "trece"
            elif n==14: return "catorce"
            elif n==15: return "quince"
            else: return "dieci"+toText(n%10)
        elif n==20: return "veinte"
        elif n<30 and n%10 != 0: return "veinti"+toText(n%10)
        elif n==30: return "treinta"
        elif n<40 and n%10 != 0: return "treinta y "+toText(n%10)
        elif n==40: return "cuarenta"
        elif n<50 and n%10 != 0: return "cuarenta y "+toText(n%10)
        elif n==50: return "cincuenta"
        elif n<60 and n%10 != 0: return "cincuenta y "+toText(n%10)
        elif n==60: return "sesenta"
        elif n<70 and n%10 != 0: return "sesenta y "+toText(n%10)
        elif n==70: return "setenta"
        elif n<80 and n%10 != 0: return "setenta y "+toText(n%10)
        elif n==80: return "ochenta"
        elif n<90 and n%10 != 0: return "ochenta y "+toText(n%10)
        elif n==90: return "noventa"
        else: return "noventa y "+toText(n%10)
    elif n<1000:
        if n==100: return "cien"
        elif n<200 and n%100!=0: return "ciento "+toText(n%100)
        elif n < 500:
            if n%100 == 0: return toText(n//100)+"cientos"
            else: return toText(n//100)+"cientos "+toText(n%100)
        elif n==500: return "quinientos"
        elif n < 600: return "quinientos "+toText(n%100)
        elif n==600: return "seiscientos"
        elif n < 700: return "seiscientos "+toText(n%100)
        elif n==700: return "setecientos"
        elif n < 800: return "setecientos "+toText(n%100)
        elif n==800: return "ochocientos"
        elif n < 900: return "ochocientos "+toText(n%100)
        elif n==900: return "novecientos"
        elif n < 1000: return "novecientos "+toText(n%100)
    elif n<1000000:
        if n//1000 == 1:
            if n%1000 == 0: return "mil"
            return "mil "+toText(n%1000)
        else:
            if n%1000 == 0: return(toText(n//1000)+"mil")
            return toText(n//1000)+" mil "+toText(n%1000)
    elif n<1000000000000:
        if n==1000000: return "un millon"
        elif n//1000000 == 1: return "un millon "+toText(n%1000000)
        elif n%1000000 != 0: return toText(n//1000000)+" millones "+toText(n%1000000)
        else: return toText(n//1000000)+" millones"
    elif n<1000000000000000000:
        if n==1000000000000: return "un billon"
        elif n//1000000000000 == 1: return "un billon "+toText(n%1000000000000)
        elif n%1000000000000 != 0: return toText(n//1000000000000)+" billones "+toText(n%1000000000000)
        else: return toText(n//1000000000000)+" billones"

if __name__ == '__main__':
  print("El numero digitado fue: " + toText(input("Digite un numero entero: "))
