#!/usr/bin/env python 
#Instalar pytube
#pip3 install pytube
from pytube import YouTube
import sys
import csv
import os

#Configuração para execução
#Individual
#   python3 youtube.py https://youtu.be/csZyzaq0kQA
#CSV
#   python3 youtube.py /caminho/arquivo.csv
#       Layout Arquivo CSV
#           Apenas 1 coluna, com os nomes/ou pastas(*)
#ex arquivo csv
#   *PASTA1
#   http://youtu.be/xptoXXXXXX01
#   http://youtu.be/xptoXXXXXX02
#   http://youtu.be/xptoXXXXXX03
#   *PASTA2
#   http://youtu.be/xptoXXXXXX0A
#--------------------------------------------------
# Após execução
#   /PASTA1
#   |_ xptoXXXXXX01.mp4
#   |_ xptoXXXXXX02.mp4
#   |_ xptoXXXXXX03.mp4
#   /PASTA2
#   |_ xptoXXXXXX0A.mp4

param = sys.argv[1]
if param.find("http") >= 0:
    #Download 1 video com link por parâmetro
    url = sys.argv[1]
    #Bloco para realização do download do vídeo do youtube
    yt = YouTube(url)
    #first = primeira opção de dowload
    yt.streams.first().download('.')
else:
    #Download a partir de leitura de arquivo CSV
    #linhas iniciadas por * geram a criação de uma nova pasta para os vídeos na sequência
    
    #Inicia o caminho da pasta
    pasta = ""
    #Capta o caminho da pasta onde está sendo executado a chamada do script
    pasta_exec = os.getcwd()
    # Verifica se o arquivo do parâmetro é um CSV
    if param.find(".csv") >=0:
        with open(param) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if row[0].find("*") == 0:
                    pasta = row[0]
                    #Substitui o identificador de pasta(*) por "/" para a criacao da subpasta
                    pasta = pasta.replace("*","/")
                    try:
                        #Cria a subpasta, conforme identificado no CSV
                        os.mkdir(pasta_exec+pasta)
                    except OSError: 
                        print ("Creation of the directory %s failed" % pasta)
                    else:
                        print ("Successfully created the directory %s " % pasta) 
                    pasta = pasta_exec+pasta
                    # Acessa a pasta para utilização da saída dos downloads na sequência
                    os.chdir(pasta)
                else:
                    #print(row[0])
                    #Bloco para realização do download do vídeo do youtube
                    yt = YouTube(row[0])
                    #get_highest_resolution = maior resolução
                    yt.streams.get_highest_resolution().download()