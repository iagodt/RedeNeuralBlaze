import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import neat

sleep = time.sleep
clear = lambda:os.system('cls')


ChromeConfig = Options()
ChromeConfig.add_argument('--log-level=3')
ChromeConfig.add_argument('--headless')    
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico,options=ChromeConfig)
driver.get('https://blaze.com/pt/games/crash?modal=auth&tab=login')




class vela:
    def __init__(self, Nvela):
        self.nvela = Nvela
        self.var = driver.find_element(By.XPATH,f'//*[@id="crash-recent"]/div[2]/div[2]/span[{self.nvela}]').text
    def atualizar(self):
        self.var = driver.find_element(By.XPATH,f'//*[@id="crash-recent"]/div[2]/div[2]/span[{self.nvela}]').text
        self.valor = self.var
        self.V = int(float(self.var[:4])*100)
var1 = vela(1);var2 = vela(2);var3 = vela(3);var4 = vela(4);var5 = vela(5);var6 = vela(6);var7 = vela(7);var8 = vela(8);
var9 = vela(9);var10 = vela(10);var11 = vela(11);var12 = vela(12);var13 = vela(13)
casasv = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13]
def attvars():
    var1.atualizar()
    var2.atualizar()
    var3.atualizar()
    var4.atualizar()
    var5.atualizar()
    var6.atualizar()
    var7.atualizar()
    var8.atualizar()
    var9.atualizar()
    var10.atualizar()
    var11.atualizar()
    var12.atualizar()
    var13.atualizar()
ck1 = driver.find_element(By.XPATH,'//*[@id="crash-recent"]/div[2]/div[2]/span[1]').text
def AtualizarVariaveis():
    global ck1
    global att
    c1 = driver.find_element(By.XPATH,'//*[@id="crash-recent"]/div[2]/div[2]/span[1]').text
    while True:
        if ck1 == '':
            ck1 = driver.find_element(By.XPATH,'//*[@id="crash-recent"]/div[2]/div[2]/span[1]').text
        elif ck1 != c1:
            att = True
            return
        else:
            ck1 = driver.find_element(By.XPATH,'//*[@id="crash-recent"]/div[2]/div[2]/span[1]').text
            att = False     

acertos = 0
erros = 0
def main(genomas, config):
    global att
    global acertos
    global erros
    redes = []
    lista_genomas = []
    for _, genoma in genomas: #criar rede neural
        rede = neat.nn.FeedForwardNetwork.create(genoma, config)
        redes.append(rede)
        genoma.fitness = 0
        lista_genomas.append(genoma)
    #while True:
    k = 100
    attvars()
        #print(casasv[0].V,casasv[1].V,casasv[2].V,casasv[3].V,casasv[4].V,casasv[5].V,casasv[6].V,
        #casasv[7].V,casasv[8].V,casasv[9].V,casasv[10].V,casasv[11].V,casasv[12].V)
    for i, genoma in enumerate(lista_genomas): #analise e previsão

        output = redes[i].activate((casasv[0].V,casasv[1].V,casasv[2].V,casasv[3].V,casasv[4].V,casasv[5].V,casasv[6].V,
                                    casasv[7].V,casasv[8].V,casasv[9].V,casasv[10].V,casasv[11].V,casasv[12].V))
            
            
        if output[0] > 0.5:
            prev = 200
        else:
            k -= 1
            prev = 100
    print(f'Chance de acerto: {k}')
    if k >= 50:
            print(f'entrar após {casasv[0].valor}\n')
    else:
            print('Não entrar\n')
    while True:
        AtualizarVariaveis()
        if att:
            break
        else:
            AtualizarVariaveis()
    attvars()
    if k >= 50:
        if casasv[0].V >= 200:
            acertos += 1
        else:
            erros += 1
    clear()
    print(f'Resultado: {casasv[0].valor}')
    print(f'Acertos: {acertos}\nErros: {erros}\n')
    for i, genoma in enumerate(lista_genomas):
            if casasv[0].V >= 200:
                if prev > 199:
                    lista_genomas[i].fitness += 15
                #else:
                    #lista_genomas[i].fitness -= 1
            else:
                if prev > 199:
                    lista_genomas[i].fitness -= 10
                    lista_genomas.pop(i)
                    redes.pop(i)
                #else:
                    #lista_genomas[i].fitness += 2



def run(config_file): #configurar rede neural
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)


    populacao = neat.Population(config)

    populacao.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    populacao.add_reporter(stats)
    populacao.run(main, 10000)




if __name__ == '__main__':
    localdir = os.path.dirname(__file__)
    config_path = os.path.join(localdir, 'config.txt')

    run(config_path)