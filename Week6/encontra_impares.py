def encontra_impares(l, i=0, lista_impares=[]):
    try:
        impar = l[i] if l[i]%2!=0 else None
        i+=1
        if impar:
            lista_impares.append(impar)
        return encontra_impares(l,i,lista_impares)
    except:
        return lista_impares



#listas = [0,1,2,3,4,5,6,7,8,9]
#print(encontra_impares(listas))