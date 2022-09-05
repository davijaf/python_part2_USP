def menor_nome(nomes):
    short = nomes[0].strip().capitalize()
    for name in range(len(nomes)):
        if len(nomes[name].strip().capitalize()) < len(short.strip().capitalize()):
            short = nomes[name].strip().capitalize()
    return short

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José

menor_nome(['maria', ' josé ', '   PAULO', 'Catarina   '])
# deve devolver José

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
menor_nome(['maria', ' josé ', '   PAULO', 'Catarina   '])
menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina'])
menor_nome(['zé', ' lu', 'fê'])