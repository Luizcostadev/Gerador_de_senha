with open('vingadores.txt','r') as arquivo:
    vingadores = arquivo.readlines()

    for vingador in vingadores:
        vingador = vingador.strip()

        convite = f'Opa{vingador}!Vai ter um churras da turma de Messias e você está convidado(a),a turma conta com a presença de vocês!!'

        print(convite)

