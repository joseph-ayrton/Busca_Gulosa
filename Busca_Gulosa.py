# Grafo representando o mapa da Romênia (Capítulo 3 do Russell & Norvig)
mapa_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Heurística h(n): Distância em linha reta de cada cidade até BUCARESTE
heuristica_bucareste = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def busca_gulosa(inicio, objetivo, grafo, heuristica):
    # Fronteira: (valor_h, cidade_atual, caminho_ate_aqui)
    fronteira = [(heuristica[inicio], inicio, [inicio])]
    visitados = set()
    passo = 1
    
    print(f" INICIANDO BUSCA GULOSA PELA MELHOR ESCOLHA (Greedy Best-First Search)")
    print(f" Origem: {inicio} -> Destino: {objetivo}")
    
    while fronteira:
        # Ordena a fronteira pelo menor h(n)
        fronteira.sort(key=lambda x: x[0])
        
        print(f"--- PASSO {passo} ---")
        print("Estado atual da Fronteira (Ordenada por h(n) decrescente de distância):")
        for h, cid, cam in fronteira:
            print(f"  > {cid} [h(n) = {h}] | Caminho percorrido: {' -> '.join(cam)}")
        
        # Remove o nó com menor h(n)
        h_atual, cidade_atual, caminho = fronteira.pop(0)
        
        print(f"\n[ESCOLHA] Cidade com menor h(n) selecionada para expansão: {cidade_atual} (h = {h_atual})")
        
        # Teste de Objetivo
        if cidade_atual == objetivo:
            print(f"\n✓ OBJETIVO ENCONTRADO! Chegamos a {objetivo}.")
            return caminho
            
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            print(f"Cidades já expandidas até agora: {list(visitados)}")
            
            # Gerando os logs para os vizinhos
            vizinhos_adicionados = []
            vizinhos_ignorados = []
            
            for vizinho, _ in grafo.get(cidade_atual, []):
                if vizinho in visitados:
                    vizinhos_ignorados.append(f"{vizinho} (Já expandido)")
                else:
                    novo_caminho = caminho + [vizinho]
                    fronteira.append((heuristica[vizinho], vizinho, novo_caminho))
                    vizinhos_adicionados.append(f"{vizinho} [h = {heuristica[vizinho]}]")
            
            if vizinhos_adicionados:
                print(f"Novos nós adicionados à fronteira: {', '.join(vizinhos_adicionados)}")
            if vizinhos_ignorados:
                print(f"Vizinhos ignorados: {', '.join(vizinhos_ignorados)}")
                
        else:
            print(f"⚠️ {cidade_atual} já foi expandida anteriormente. Pulando geração de filhos.")
            
        print("-" * 50 + "\n")
        passo += 1
                    
    return None

# Execução do teste
caminho_final = busca_gulosa('Arad', 'Hirsova', mapa_romenia, heuristica_bucareste)

print(" RESULTADO FINAL")

if caminho_final:
    print(f"Caminho ideal pela Busca Gulosa:\n{' -> '.join(caminho_final)}")
else:
    print("Não foi possível encontrar um caminho.")