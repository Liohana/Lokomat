##Código: Uso do Lokomat

## Tarefa 1 - Aquisição de dados:
  
Var: m, param, v, d
  
## Tarefa 2 - Preparo do paciente e do ambiente de aquisição:
  
Var: cinto, exo, esteira, monitor
  
## Tarefa 3 - Lokomat:
  
#3.1 - Início da coleta:
   Início
   Leia m
   Se Cinto = True então
   Execute Pocisionamento e elevação do paciente
   Fim_se
  
#3.2 - Posicionamento do paciente no Lokomat:
   Leia param
   Execute acoplamento do Lokomat
 
#3.3 - Início da coleta:
   Se Esteira ligada = True então
     Se Feedback visual = True então
    		Execute Iniciar a marcha
  	    Execute Iniciar feedback visual
  	  Fim_se
   Fim_se
  
#3.4 - Análise do desenvolvimento do paciente e fim da coleta:
   Leia v, d
   Se Bom desempenho = True então
   Enquanto Bom desempenho = True
    	Execute Aumento da participação do paciente
    	Leia v, d
   Fim_se
   Senão
   Então Mantenham o ritmo
   Fim