class Statistics():
    
    def __init__(self, gabarito_formatado, respostas_formatadas):

        self.gabarito = gabarito_formatado
        self.numero_de_questoes = len(gabarito_formatado)
        self.respsotas = respostas_formatadas
        self.numero_de_participantes = len(respostas_formatadas)

        self.acerto_absoluto_total = 0
        self.acerto_percentual_total = 0
        self.acerto_percentual_efetivo = 0  # sem as provas zeradas
        self.provas_zeradas = 0
        self.questoes_respondidas_total = self.numero_de_participantes * self.numero_de_questoes


        self.acertos_individuais = list() # list( (numero_de_acertos, percentual_de_acertos, nome) )

        self.__construir_estatisticas()


    def __construir_estatisticas(self):

        soma_acertos_percentuais = 0
        soma_acertos_totais = 0
        
        for aluno in self.respsotas: 
            questoes = self.respsotas[aluno]

            acertos = 0
            for numero, resposta in questoes.items():
                if resposta.upper() == self.gabarito[numero].upper():
                    acertos += 1
            
            acerto_percentual = acertos/self.numero_de_questoes

            soma_acertos_totais += acertos
            soma_acertos_percentuais += acerto_percentual

            if acertos == 0:
                self.provas_zeradas += 1

            self.acertos_individuais.append((acertos, acerto_percentual, aluno))
        
        
        self.acertos_individuais.sort(reverse=True) # da maior nota pra menor
        
        self.acerto_absoluto_total = soma_acertos_totais
        self.acerto_percentual_total = soma_acertos_percentuais/self.numero_de_participantes
        self.acerto_percentual_efetivo = soma_acertos_percentuais/(self.numero_de_participantes-self.provas_zeradas)


    def get_data(self):
        data = {
            'geral':{
                'acerto_percentual':self.acerto_percentual_total,
                'acerto_absoluto':self.acerto_absoluto_total,
                'acerto_percentual_efetivo':self.acerto_percentual_efetivo,
                'provas_zeradas':self.provas_zeradas
            },
            'individual': self.acertos_individuais
        }
        return data


    def print_data(self):
        sepatator = "--------------------------------------------------------------------"
        print(sepatator)
        print("Total")
        print("\tAcerto percentual:", self.acerto_percentual_total)
        print("\tProvas zeradas: ", self.provas_zeradas)
        print("\tAcerto efetivo:", self.acerto_percentual_efetivo)
        print()
        print("Individual\n\n")
        for aluno in self.acertos_individuais: #aluno=(numero_de_acertos, percentual_de_acertos, nome)
            print("\tNome:", aluno[2])
            print("\tAcerto absoluto:", aluno[0])
            print("\tAcerto percentual", aluno[1])
            print()
        print(sepatator)