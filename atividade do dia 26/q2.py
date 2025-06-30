'''
   Você recebeu uma lista com informações de times de futebol do campeonato brasileiro, 
   onde cada sub-lista contém os dados de um time no seguinte formato:

   [nome_do_time, jogos_vencidos, jogos_empates, jogos_derrotas, gols_marcados, gols_sofridos]


   1) Implemente um código para adicionar a cada time:

      a) Adicionar após a quantidade de derrotas a quantidade total de pontos, 
         considerando que uma vitória vale 3 pontos e um empate vale 1 ponto.

      b) Após a quantidade de gols sofridos o saldo de gols, que é a diferença entre 
         gols marcados e gols sofridos.

      
   2) Após adicionar essas informações, ordene a lista dos times seguindo os critérios 
      abaixo (do maior para o menor):

      a) Pontos
      b) Vitórias
      c) Saldo de gols
      d) Gols marcados

   3) Exiba a lista final ordenada, mostrando todas as informações de cada time, 
      incluindo os pontos e saldo de gols adicionados.
'''

lstTimes = [
            ['Atlético Mineiro', 20, 8, 7, 53, 26]    , ['Bahia', 12, 10, 11, 39, 37],
            ['Botafogo', 14, 12, 8, 46, 29]           , ['Ceará', 10, 11, 14, 34, 43],
            ['Corinthians', 18, 9, 10, 50, 31]        , ['Cruzeiro', 9, 14, 10, 33, 33],
            ['Flamengo', 23, 7, 7, 62, 27]            , ['Fluminense', 15, 11, 9, 44, 32],
            ['Fortaleza', 11, 13, 11, 36, 35]         , ['Grêmio', 13, 9, 15, 38, 43],
            ['Internacional', 16, 8, 13, 45, 39]      , ['Juventude', 8, 13, 15, 30, 44],
            ['Mirassol', 10, 10, 17, 32, 46]          , ['Palmeiras', 22, 9, 6, 58, 25],
            ['Red Bull Bragantino', 14, 8, 16, 40, 45], ['Santos', 13, 11, 14, 39, 41],
            ['São Paulo', 17, 7, 14, 48, 38]          , ['Sport', 11, 12, 15, 35, 42],
            ['Vasco da Gama', 9, 15, 14, 33, 40]      , ['Vitória', 7, 13, 18, 28, 47]
         ]

# ----------------------------------------------------------------------
# Questão 01
lstTimes = [
    [nome, v, e, d, v * 3 + e, gm, gs, gm - gs]
    for nome, v, e, d, gm, gs in lstTimes
]

# ----------------------------------------------------------------------
# Questão 02
# TODO: Fazer na sala de aula no dia 01/07/2026
# TODO: Pesquisar a função SORT() usando funções LAMBDA


# ----------------------------------------------------------------------
# Questão 03
print("\nTabela Final do Campeonato (ordenada):\n")
print(f"{'Time':<22} {'V':>2} {'E':>2} {'D':>2} {'Pts':>4} {'GM':>4} {'GS':>4} {'SG':>4}")
print("-" * 50)

for time in lstTimes:
    print(f"{time[0]:<22} {time[1]:>2} {time[2]:>2} {time[3]:>2} {time[4]:>4} {time[5]:>4} {time[6]:>4} {time[7]:>4}")
