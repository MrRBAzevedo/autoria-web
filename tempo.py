tempo = 0
amigos = []
entradas = []
n = int(input())

for i in range(n):
    tipo, amigo = input().split()
    entradas.append(tipo)

    if tipo == 'R':
        
        found = False
        for a in amigos:
            if a['nome'] == amigo:
                found = True
                a['R'] = tempo

        if not found:
            a = {'nome' : amigo, 'R' : tempo, 'T' : 0}
            amigos.append(a)

        if i != 0:
            if entradas[i - 1] != 'T':
                tempo += 1
        else:
            tempo += 1

    elif tipo == 'E':
        
        for a in amigos:
            if a['nome'] == amigo:
                dur = tempo - a['R']
                a['T'] += dur

        if entradas[i - 1] != 'T':
                tempo += 1

    elif tipo == 'T':
        if entradas[i - 1] != 'T':
            tempo -= 1

        tempo += int(amigo)

for a in amigos:
    print(a['nome'], a['T'])
