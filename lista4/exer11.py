alunos_3a_serie = 0
maior_qtd_livros_4a_serie = 0
alunos_3a_serie_sem_gosto_redacao = 0
total_alunos = 0

while True:
    serie = int(input(primeira, segunda, terceira, quarta))
    if serie == 0:
        break
    
    livros = int(input(10, 20))
    gosta_redacao = int(input(50%))
    
    total_alunos += 1
    
    if serie == 3:
        alunos_3a_serie += 1
        if gosta_redacao == 0:
            alunos_3a_serie_sem_gosto_redacao += 1
    elif serie == 4:
        if livros > maior_qtd_livros_4a_serie:
            maior_qtd_livros_4a_serie = livros

if alunos_3a_serie == 0:
    perc_nao_gostam_redacao_3a_serie = "IMPOSSIVEL CALCULAR % NENHUM ALUNO NA 3a SERIE!"
else:
    perc_nao_gostam_redacao_3a_serie = "{:.1%}".format(alunos_3a_serie_sem_gosto_redacao / alunos_3a_serie)

print(f"ALUNOS 3a SERIE:{alunos_3a_serie}")
print(f"MAIOR QTD LIVROS 4a SERIE:{maior_qtd_livros_4a_serie}")
print(f"NAO GOSTAM REDACAO 3a SERIE:{perc_nao_gostam_redacao_3a_serie}")
