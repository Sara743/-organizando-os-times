# Funçao para resolver o problema
def formar_times():

    # Leitura dos dados de entrada
    N,T = map(int, input().split())
    alunos = []
    
    # # Leitura dos alunos e seus níveis de habilidade
    for _ in range(N):
        nome, habilidade = input().split()
        alunos.append((nome,int(habilidade)))
            
    # Ordena os alunos pela habilidade de forma decrescente
    alunos.sort(key=lambda x: -x[1])
     
    # Inicializa os times
    times = [[] for _ in range(T)]
     
    # Distribui os alunos nos times de forma alterada
    for i in range(N):
        times[i% T].append(alunos[i][0])
         
    # Para cada time, organiza os jogadores em ordem alfabética
    for i in range(T):
        times[i].sort()
         
    # Exibe os times conforme o formatosolicitado
    for i in range(T):
        print(f"Time {i + 1}")
        for jogador in times[i]:
            print(jogador)
        print() # Linha em branco após cada time
         
formar_times()