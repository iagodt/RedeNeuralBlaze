from threading import Thread
from pathlib import Path
import tkinter
from PIL import Image, ImageTk
from customtkinter import *
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

sleep = time.sleep
clear = lambda:os.system('cls')

ChromeConfig = Options()
ChromeConfig.add_argument('--log-level=3')
ChromeConfig.add_argument('--headless')
ChromeConfig.add_argument('window-size=1000,800')
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
var9 = vela(9);var10 = vela(10);var11 = vela(11);var12 = vela(12);var13 = vela(13);var14 = vela(14);var15 = vela(15)
casasv = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15]
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
    var14.atualizar()
    var15.atualizar()

def atualizacaoautomatica():
    while True:
        AtualizarVariaveis()
        if att:
            attvars()
            break




set_appearance_mode('System')
set_default_color_theme('dark-blue')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class FrontEnd(CTk):
    Name = 'BlazeDT BOT'
    Width = 1024
    Height = 576

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #settings window
        self.title(FrontEnd.Name)
        self.geometry(f'{FrontEnd.Width}x{FrontEnd.Height}')
        self.resizable(False, False)
        #background

        attvars()
        self.casa1 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[0].valor,
                            width=50,
                            height=50
                            )
        self.casa1.place(y=63,x=65)
        self.casa2 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[1].valor,
                            width=50,
                            height=50
                            )
        self.casa2.place(y=63,x=125)
        self.casa3 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[2].valor,
                            width=50,
                            height=50
                            )
        self.casa3.place(y=63,x=185)
        self.casa4 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[3].valor,
                            width=50,
                            height=50
                            )
        self.casa4.place(y=63,x=245)
        self.casa5 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[4].valor,
                            width=50,
                            height=50
                            )
        self.casa5.place(y=63,x=305)
        self.casa6 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[5].valor,
                            width=50,
                            height=50
                            )
        self.casa6.place(y=63,x=365)
        self.casa7 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[6].valor,
                            width=50,
                            height=50
                            )
        self.casa7.place(y=63,x=425)
        self.casa8 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[7].valor,
                            width=50,
                            height=50
                            )
        self.casa8.place(y=63,x=485)
        self.casa9 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[8].valor,
                            width=50,
                            height=50
                            )
        self.casa9.place(y=63,x=545)
        self.casa10 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[9].valor,
                            width=50,
                            height=50
                            )
        self.casa10.place(y=63,x=605)
        self.casa11 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[10].valor,
                            width=50,
                            height=50
                            )
        self.casa11.place(y=63,x=665)
        self.casa12 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[11].valor,
                            width=50,
                            height=50
                            )
        self.casa12.place(y=63,x=725)
        self.casa13 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[12].valor,
                            width=50,
                            height=50
                            )
        self.casa13.place(y=63,x=785)
        self.casa14 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[13].valor,
                            width=50,
                            height=50
                            )
        self.casa14.place(y=63,x=845)
        self.casa15 = CTkLabel(
                            fg_color=('#38761d'),
                            text=casasv[14].valor,
                            width=50,
                            height=50
                            )
        self.casa15.place(y=63,x=905)


        self.saldo = CTkButton(text='logar',command=self.logar)
        self.saldo.pack()



        self.frame4x = CTkFrame(width=231,height=302,corner_radius=30,border_color='#7697c8',border_width=5)
        self.frame4x.place(x=69,y=197)
        
        self.quatrox = CTkSwitch(master=self.frame4x,text='Vela 4X', command=switch_vela4, onvalue='on', offvalue='off',bg_color='#212325')
        self.quatrox.place(x=68,y=52)
        self.ValordaAposta = CTkEntry(master=self.frame4x,placeholder_text='Valor da aposta')
        self.ValordaAposta.place(x=43,y=84)
        self.Butao5 = CTkButton(master=self.frame4x,text='Enviar',command=ValorSubmit)
        self.Butao5.place(x=43,y=124)

        self.frame3x = CTkFrame(width=231,height=302,corner_radius=30,border_color='#7697c8',border_width=5)
        self.frame3x.place(x=387,y=197)
        
        self.tresx = CTkSwitch(master=self.frame3x,text='Vela 3X', command=None, onvalue='on', offvalue='off',bg_color='#212325')
        self.tresx.place(x=68,y=52)
        self.ValordaAposta2 = CTkEntry(master=self.frame3x,placeholder_text='Valor da aposta')
        self.ValordaAposta2.place(x=43,y=84)
        self.Butao6 = CTkButton(master=self.frame3x,text='Enviar',command=ValorSubmit)
        self.Butao6.place(x=43,y=124)

        self.frame2x = CTkFrame(width=231,height=302,corner_radius=30,border_color='#7697c8',border_width=5)
        self.frame2x.place(x=722,y=197)
        
        self.doisx = CTkSwitch(master=self.frame2x,text='Vela 2X', command=None, onvalue='on', offvalue='off',bg_color='#212325')
        self.doisx.place(x=68,y=52)
        self.ValordaAposta3 = CTkEntry(master=self.frame2x,placeholder_text='Valor da aposta')
        self.ValordaAposta3.place(x=43,y=84)
        self.Butao7 = CTkButton(master=self.frame2x,text='Enviar',command=ValorSubmit)
        self.Butao7.place(x=43,y=124)

    def logar(self):
        self.LoginScreen = CTkToplevel(master=self)
        self.LoginScreen.focus_force()
        self.email = CTkEntry(self.LoginScreen,placeholder_text='Email Blaze')
        self.email.place(x=15,y=5)

        self.senha = CTkEntry(self.LoginScreen,placeholder_text='Senha Blaze',show='*')
        self.senha.place(x=15,y=45)
        self.senha.bind('<Return>',LogarBlaze)

        self.botao = CTkButton(master=self.LoginScreen,text='LOGAR',text_color='Black',
        command=LogarBlaze,
        fg_color='#ffffff',hover_color='#3d85c6'
        )
        self.botao.place(x=15,y=85)

def login(email,senha):
    emailI = driver.find_element(By.XPATH,'//*[@id="auth-modal"]/div[2]/form/div[1]/div/input')
    senhaI = driver.find_element(By.XPATH,'//*[@id="auth-modal"]/div[2]/form/div[2]/div/input')
    logar = driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button')
    emailI.click()
    emailI .send_keys(Keys.CONTROL,'a',Keys.DELETE)
    senhaI.click()
    senhaI.send_keys(Keys.CONTROL,'a',Keys.DELETE)
    emailI.send_keys(email)
    senhaI.send_keys(senha)
    logar.click()
    set_Aposta()

def set_Aposta():
    global quantia,AutoRetirar,Apostar
    sleep(3)
    try:
        quantia = driver.find_element(By.XPATH,'//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')    
        AutoRetirar = driver.find_element(By.XPATH,'//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[2]/div[1]/input')
        Apostar = driver.find_element(By.XPATH,'//*[@id="crash-controller"]/div[1]/div[2]/div[2]/button')

    except NoSuchElementException:
        print('email e ou senha incorretos')

def LoginCheck():
    try:
        global Saldo
        Saldo = driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/div[1]/div/a/div/div/div').text
    except NoSuchElementException:
        pass

def AtualizarCasas():
    attvars()
    if casasv[0].V >= 200:
        frontEnd.casa1.configure(fg_color=('#4CB250'),text=casasv[0].valor)
    else:
        frontEnd.casa1.configure(fg_color=('#D94444'),text=casasv[0].valor)


    if casasv[1].V >= 200:
        frontEnd.casa2.configure(fg_color=('#4CB250'),text=casasv[1].valor)
    else:
        frontEnd.casa2.configure(fg_color=('#D94444'),text=casasv[1].valor)


    if casasv[2].V >= 200:
        frontEnd.casa3.configure(fg_color=('#4CB250'),text=casasv[2].valor)
    else:
        frontEnd.casa3.configure(fg_color=('#D94444'),text=casasv[2].valor)


    if casasv[3].V >= 200:
        frontEnd.casa4.configure(fg_color=('#4CB250'),text=casasv[3].valor)
    else:
        frontEnd.casa4.configure(fg_color=('#D94444'),text=casasv[3].valor)


    if casasv[4].V >= 200:
        frontEnd.casa5.configure(fg_color=('#4CB250'),text=casasv[4].valor)
    else:
        frontEnd.casa5.configure(fg_color=('#D94444'),text=casasv[4].valor)


    if casasv[5].V >= 200:
        frontEnd.casa6.configure(fg_color=('#4CB250'),text=casasv[5].valor)
    else:
        frontEnd.casa6.configure(fg_color=('#D94444'),text=casasv[5].valor)


    if casasv[6].V >= 200:
        frontEnd.casa7.configure(fg_color=('#4CB250'),text=casasv[6].valor)
    else:
        frontEnd.casa7.configure(fg_color=('#D94444'),text=casasv[6].valor)


    if casasv[7].V >= 200:
        frontEnd.casa8.configure(fg_color=('#4CB250'),text=casasv[7].valor)
    else:
        frontEnd.casa8.configure(fg_color=('#D94444'),text=casasv[7].valor)


    if casasv[8].V >= 200:
        frontEnd.casa9.configure(fg_color=('#4CB250'),text=casasv[8].valor)
    else:
        frontEnd.casa9.configure(fg_color=('#D94444'),text=casasv[8].valor)


    if casasv[9].V >= 200:
        frontEnd.casa10.configure(fg_color=('#4CB250'),text=casasv[9].valor)
    else:
        frontEnd.casa10.configure(fg_color=('#D94444'),text=casasv[9].valor)


    if casasv[10].V >= 200:
        frontEnd.casa11.configure(fg_color=('#4CB250'),text=casasv[10].valor)
    else:
        frontEnd.casa11.configure(fg_color=('#D94444'),text=casasv[10].valor)


    if casasv[11].V >= 200:
        frontEnd.casa12.configure(fg_color=('#4CB250'),text=casasv[11].valor)
    else:
        frontEnd.casa12.configure(fg_color=('#D94444'),text=casasv[11].valor)


    if casasv[12].V >= 200:
        frontEnd.casa13.configure(fg_color=('#4CB250'),text=casasv[12].valor)
    else:
        frontEnd.casa13.configure(fg_color=('#D94444'),text=casasv[12].valor)


    if casasv[13].V >= 200:
        frontEnd.casa14.configure(fg_color=('#4CB250'),text=casasv[13].valor)
    else:
        frontEnd.casa14.configure(fg_color=('#D94444'),text=casasv[13].valor)


    if casasv[14].V >= 200:
        frontEnd.casa15.configure(fg_color=('#4CB250'),text=casasv[14].valor)
    else:
        frontEnd.casa15.configure(fg_color=('#D94444'),text=casasv[14].valor)

def AtualizarAutomatico():
    while True:
        AtualizarVariaveis()
        AtualizarCasas()

def attsaldo():
    global Saldo
    Saldo = driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/div[1]/div/a/div/div/div').text

def LogarBlaze(*args):
    login(frontEnd.email.get(),frontEnd.senha.get())
    LoginCheck()
    attsaldo()
    frontEnd.LoginScreen.destroy()
    frontEnd.saldo.configure(text=Saldo,command=attsaldo)



AutoRetirada = 2

ValorAposta = 0.01
ValorMSL2 = ValorAposta + ValorAposta/2
ValorMSL3 = 2*(ValorAposta + ValorAposta/2)

def ValorSubmit():
    global frontEnd
    global ValorAposta
    global ValorMSL3,ValorMSL2
    ValorAposta = float(frontEnd.ValordaAposta.get())
    ValorMSL2 = ValorAposta + ValorAposta/2
    ValorMSL3 = 2*(ValorAposta + ValorAposta/2)





def ApostaBasica():
    global ValorAposta
    quantia.click()
    quantia.send_keys(str(ValorAposta))
    AutoRetirar.click()
    AutoRetirar.send_keys('2')
    Apostar.click()

def gale1():
    global ValorAposta
    quantia.click()
    quantia.send_keys(str(ValorAposta*2))
    AutoRetirar.click()
    AutoRetirar.send_keys('2')
    Apostar.click()

def gale2():
    global ValorAposta
    quantia.click()
    quantia.send_keys(str(ValorAposta*4))
    AutoRetirar.click()
    AutoRetirar.send_keys('2')
    Apostar.click()

def aposta2MSL():
    global ValorAposta
    quantia.click()
    quantia.send_keys(str(ValorMSL2))
    AutoRetirar.click()
    AutoRetirar.send_keys('4')
    Apostar.click()

def aposta3MSL():
    global ValorAposta
    quantia.click()
    quantia.send_keys(str(ValorMSL3))
    AutoRetirar.click()
    AutoRetirar.send_keys('4')
    Apostar.click()



stopVela4 = False
def vela4():
        global stopVela4
        while True:
            atualizacaoautomatica()
            if casasv[0].V > 170:
                if casasv[0].V < 190:
                    ApostaBasica()
                    atualizacaoautomatica()
                    if att:
                        print(casasv[0].valor)
                        if casasv[0].V > 400:
                            acertos += 1
                        else:
                            gale1 += 1
                            aposta2MSL()
                            atualizacaoautomatica()
                            if att:
                                print(casasv[0].valor)
                                if casasv[0].V > 400:
                                    acertos += 1
                                else:
                                    gale2 += 1
                                    aposta3MSL()
                                    atualizacaoautomatica()
                                    if att:
                                        print(casasv[0].valor)
                                        if casasv[0].V > 400:
                                            acertos +=1 
                                        else:
                                            erros += 1 
            
            if stopVela4:
                break

def switch_vela4():
    process1 = Thread(target=vela4)
    if frontEnd.quatrox.get() == 'on':
        print('Velas 4x ativado')
        process1.start()

    elif frontEnd.quatrox.get() == 'off':
        global stopVela4
        stopVela4 = True
        print('Velas 4X desativado')
    
    


if __name__ == '__main__':
    frontEnd = FrontEnd()
    AtualizarCasas()
    process1 = Thread(target=AtualizarAutomatico).start()
    
    
    frontEnd.mainloop()