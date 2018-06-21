# ===========================================================
#
# ESZA019-17 - VISAO COMPUTACIONAL - NA - 2Q2018
# PRATICA 01
#
# RA: 11056613
# NOME: ISABELLE ORLANDI
# 
# E-MAIL: orlandi.isabelled@gmail.com
#
# ===========================================================
#
# DESCRICAO: lab01.py 
#
# O codigo abaixo armazena num espaco de memoria uma imagem contida no mesmo
# diretorio em que foi salvo o programa. Em seguida exibe a imagem salva em 
# uma janela chamada 'image'. A janela permanece aberta ate que a tecla 'esc' 
# seja pressionada, se a tecla 's' for pressionada, a imagem e salva na pasta
# do diretorio no formato PNG, sob o nome 'messigray'
# 
# ===========================================================

#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv

# carrega a imagem 'messi5.jpg' para a variavel 'img'. O argumento '0' retorna a imagem em escala de cinza
img = cv.imread('messi5.jpg',0)
# exibe a imagem salva na variavel 'img' em uma janela chamada 'image'
cv.imshow('image',img)

k = cv.waitKey(0) # inicializa a espera por tecla pressionada
if k == 27: # se 'Esc' pressionado...
	cv.destroyAllwindows() # fecha todas as janelas
elif k == ord('s'): # se 'S' pressionado...
	cv.imwrite('messigray.png',img) # salva a imagem 'img' no diretorio do programa sob o nome 'messigray' no formato PNG
	cv.destroyAllwindows() # fecha todas as janelas
