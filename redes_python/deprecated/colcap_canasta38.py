#Red basica para Colcap canasta 38
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()

Colcap=["PFBCOLOM","GRUPOSURA","ECOPETROL","NUTRESA",
        "GRUPOARGOS","BCOLOMBIA","ISA","CEMARGOS",
        "PFAVAL","PFGRUPOARG","PFGRUPSURA","EEB",
        "EXITO","PFDAVVNDA","CORFICOLCF","BOGOTA",
        "PFCEMARGOS","CLH","CELSIA","PFAVH",
        "CNEC","CONCONCRET","BVC","ETB"
        ]
G.add_nodes_from(Colcap)


nx.draw_random(G,with_labels=True)
plt.show()