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
# DESCRICAO: lab01camera.py 
#
# O codigo cria um objeto de captura de frames da camera padrao, converte os frames para escala de cinza
# e os exibe continuamente ate a tecla 'q' ser pressionada. A exibicao de frames em sequencia gera na janela
# de exibicao um video. 
# 
# ===========================================================

#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv

cap = cv.VideoCapture(0) # cria um objeto de captura de video utilizando a camera padrao. 

while(True): # loop infinito 
	ret, frame = cap.read() # leitura de um frame do video. Se a leitura e feita, retorna 'true' na variavel 'ret'
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # aloca o frame capturado, em escala de cinza, na variavel 'gray'
	cv.imshow('frame', gray) # exibe a imagem salva em 'gray' em uma janela chamada 'frame'
	if cv.waitKey(1) & 0xFF == ord('q'): # se a tecla 'q' for pressionada... (0xFF indica que somente o ultimo byte e verificado)
		break # saida do loop while

cap.release() # destroi o objeto de captura de video
cv.destroyAllWindows() # fecha as janelas abertas