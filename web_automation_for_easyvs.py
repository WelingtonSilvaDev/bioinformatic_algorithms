#cspell:disable

'''                                            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                                            AUTOMAÇÃO WEB PARA VIRTUAL SCREENING NO EASYVS
                                                                FEITO POR WELINGTON GONÇALVES SILVA
                                                            UNIVERSIDADE FEDERAL DE ITAJUBÁ - UNIFEI    
                                                                                2022                                                                           
                                                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                                                                
                                Observação: este script foi criado para auxiliar um expert no processo de triagem virtual/virtual screening  
                                na plataforma EasyVS. Imprevistos (erros, resposta lenta) durante o processamento podem ocorrer, portanto é
                                crucial a supervisão do fluxo de forma a se evitar problemas maiores. No mais, agradeço a você por estar 
                                utilizando ambos programas, este e o EasyVS. Obrigado!
                                Welington Gonçalves Silva - UNIFEI                             GitHub: https://github.com/WelingtonSilvaDev                                                                                                                   
                                                                                                                                                                  
                                                                                                                                                                       '''
'''
Este script foi pensado para Windows. Caso alguém interessar, pode adaptá-lo para Linux.
Última atualização feita em: 31-01-2022

'''
'''
Caso vc não tenha instalado o pacote PySimpleGUI, vá até
o prompt de comando e use (win): 
pip install PySimpleGUI
'''
import sys
from asyncio.base_futures import _FINISHED
from genericpath import exists
from optparse import Values
import pdb
from tkinter import BROWSE
from tracemalloc import stop
import pyautogui as pa
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox


''' 
import PySimpleGUI as sg 
class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Material1')
       
        #layout
        layout = [
            [sg.Text('PDB ID', size=(6,0)), sg.Input(size=(6,0), key='pdb_id')],
            [sg.Checkbox('Keep Waters', key='waters'), sg.Checkbox('Heteroatoms', key='heteroatoms')],
            [sg.Button('Ok')]
        ]
        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        #extrair os dados da tela
        self.button, self.values = janela.Read()
    def Iniciar(self):
        pdb_id = self.values['pdb_id']
        waters = self.values['waters']
        heteroatoms = self.values['heteroatoms']
        #print(f'PDB ID: {pdb_id}\nWaters:{waters}\nHeteroátomos: {heteroatoms}')
        
tela = TelaPython()
tela.Iniciar() '''

messagebox.showwarning('ATENÇÃO!', 'Seu computador será controlado automaticamente a partir de agora. Aguarde a finalização. Clique em OK.')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''' AQUI abaixo o usuário altera o diretório/caminho do executável 'chromedriver' '''
driver = webdriver.Chrome(r'C:\automation\chromedriver') # <--------diretório do chromedriver.exe no seu computador
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
AQUI o usuário altera os parâmetros para rodar o script. Todos os parâmetros dizem respeito às opções a se marcar/preencher no EasyVS. (1 = sim, 0 = não)

'''
pdb_id = '5d5r'     #PDB ID code
heteroatoms = 1     #Manter heteroátomos no alvo original?
waters = 0          #Manter águas/waters no alvo original?

coordinates_ = 1;   #Fornecer manualmente as coordenadas do box?

if coordinates_:    #Em caso afirmativo para coordenadas manuais, preencha-as abaixo:
    x_coordinate = 10;
    y_coordinate = 15;
    z_coordinate = 30;

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def coordinates ():
    #I want to provide 3D coordinates X Y Z
    #1
    buttonxyz = driver.find_element(By.XPATH,'//*[@id="user_coordinates"]')
    buttonxyz.click()
    time.sleep(0.35)
    #2 - X
    buttonx = driver.find_element(By.XPATH,'//*[@id="pos_x_manual"]')
    buttonx.click()
    time.sleep(0.25)
    buttonx.clear()
    buttonx.send_keys(x_coordinate)
    time.sleep(0.3)
    
    #3 - Y
    buttony = driver.find_element(By.XPATH,'//*[@id="pos_y_manual"]')
    buttony.click()
    time.sleep(0.25)
    buttony.clear()
    buttony.send_keys(y_coordinate)
    time.sleep(0.3)
    
    #4 - Z
    buttonz = driver.find_element(By.XPATH,'//*[@id="pos_z_manual"]')
    buttonz.click()
    time.sleep(0.25)
    buttonz.clear()
    buttonz.send_keys(z_coordinate)
    time.sleep(0.4)

    # get http://biosig.unimelb.edu.au/easyvs/
driver.get("http://biosig.unimelb.edu.au/easyvs/")
    
# Maximize the window and let code stall 
time.sleep(0.3)
driver.maximize_window()
time.sleep(1)
    
#STEP 1
buttonpdb = driver.find_element(By.XPATH, '//*[@id="pdbid_input"]')
buttonpdb.click()
time.sleep(0.1)
#colocar ID PDB

buttonpdb.send_keys(pdb_id)
time.sleep(0.5)
 
    #ou então fazer upload de arquivo .pdb:
        #buttonarchive = driver.find_element_by_xpath('//*[@id="pdb_file"]')
        #buttonarchive.click()
    #Keep waters ou Keep heteroatoms
if waters:
        #Keep waters (MANTENDO):
        button_het = driver.find_element(By.XPATH,'//*[@id="keepWaters"]').click()
        time.sleep(0.9)
if heteroatoms:
        #Keep heteroatoms (MANTENDO):
        button_het = driver.find_element(By.XPATH,'//*[@id="keepHetatm"]').click()
        time.sleep(0.9)
#next step
buttonnext = driver.find_element(By.XPATH,'//*[@id="pdb_form"]/div[4]/div/div/button')
buttonnext.click()
time.sleep(15)

#STEP2
#Advanced Docking Parameters (adp)
buttonadp= driver.find_element(By.XPATH, '//*[@id="headingOne"]/h5/a')
buttonadp.click()
time.sleep(0.4)
    
#Selecting the box size
#coordenadas automaticas:
if coordinates_:
        coordinates()

#next step
time.sleep(0.2)        
buttonnext = driver.find_element(By.XPATH,'//*[@id="next_button"]')
buttonnext.click()
time.sleep(4)

#STEP3
button_select_all = driver.find_element(By.XPATH,'//*[@id="drugbank"]')
button_select_all.click()
time.sleep(0.2)
#custom, RO5, RO3?
button_rd = driver.find_element(By.XPATH,'//*[@id="rd_notfilter"]')
button_rd.click()
time.sleep(0.2)

#Similarity
button_process = driver.find_element(By.XPATH,'//*[@id="btnFilter"]')
button_process.click()
time.sleep(30)

#next step
button_final = driver.find_element(By.XPATH,'//*[@id="next_button"]')
button_final.click()

time.sleep(15)

#COLETA A URL ATUAL DO BROWSE
link = driver.current_url 

def excel():
    #Os comandos abaixo são a automação para abertura do Excel e salvamento do PDB ID com LINK do EASYVS
    pa.press('winleft')
    time.sleep(1)
    pa.write('excel')
    time.sleep(1)
    pa.press('enter')
    time.sleep(5)
    pa.hotkey('ctrl', 'n')
    time.sleep(0.7)
    pa.press('enter')
    time.sleep(0.7)
    pa.press('enter')
    time.sleep(1)
    pa.write(pdb_id.upper())
    time.sleep(1)
    pa.press('right')
    time.sleep(1)
    pa.write(link)
    time.sleep(0.5)
    pa.press('enter')
    time.sleep(0.6)
    pa.hotkey('ctrl', 'b')
    time.sleep(0.8)
    pa.press('enter')
    time.sleep(1)
    pa.hotkey('ctrl', 'f4')
    time.sleep(1)
    messagebox.showinfo('SALVO!', 'O arquivo Excel foi salvo com sucesso.\nSomente a aba do arquivo foi fechada para evitar problemas.')
    time.sleep(1)
    messagebox.showinfo(f'ATENÇÃO!', 'Código finalizado. Uso liberado!\nFeito por Welington Silva - UNIFEI') 
    
excel()


sys.exit() #fim de codigo (pode remover se colocá-lo o fim do codigo)


