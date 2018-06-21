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
# DESCRICAO: lab01capvideo.py 
#
# O codigo cria um objeto de captura de frames da camera padrao e um objeto de gravacao de frames. 
# O video capturado é salvo no formato 'avi' em uma taxa de 20 frames por segundo e tamanho 640x480.
# 
# ===========================================================

#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv

cap = cv.VideoCapture(0) # cria um objeto de captura de video utilizando a camera padrao. 

fourcc = cv.cv.CV_FOURCC(*'XVID') # define metodo de compressao de videos no formato XviD MPEG-4 
out = cv.VideoWriter('saidavideo.avi', fourcc, 20.0, (640,480)) # cria o objeto de gravacao de videos

while(cap.isOpened()): # Enquanto o objeto de captura de video esta aberto...
	ret, frame = cap.read() # leitura de um frame do video. Se a leitura e feita, retorna 'true' na variavel 'ret'
	if ret==True: # se a leitura do frame e realizada...
		out.write(frame) # escreve o frame capturado no objeto de gravacao
		cv.imshow('frame', frame) # exibe a imagem salva em 'frame' em uma janela chamada 'frame'
		if cv.waitKey(1) & 0xFF == ord('q'): # se a tecla 'q' for pressionada... (0xFF indica que somente o ultimo byte e verificado)
			break # saida do loop while
	else: # se ocorre erro na leitura do frame...
		break # saida do loop while

cap.release() # destroi o objeto de captura de video
out.release() # destroi o objeto de gravacao de video
cv.destroyAllWindows() # fecha as janelas abertas
 

