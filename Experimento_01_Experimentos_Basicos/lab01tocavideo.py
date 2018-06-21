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
# DESCRICAO: lab01tocavideo.py 
#
# Realiza a leitura de um video salvo no diretorio do programa. 
# O video e exibido numa taxa de 30 frames por segundos.
# 
# ===========================================================

# importacao da bibliteca time (manipulacao de datas e temporizacao)
import time
#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv
 
cap = cv.VideoCapture('test.mp4') # cria um objeto de captura de video, utilzando o arquivo 'test.mp4' 

while(cap.isOpened()): # Enquanto o objeto de captura de video esta aberto...
	ret, frame = cap.read() # leitura de um frame do video. Se a leitura e feita, retorna 'true' na variavel 'ret'
	cv.imshow('frame', frame) # exibe o frame capturado em uma janela chamada 'frame'
	time.sleep(1/30.0) # aguarda um delay de 1/30 segundos (0,03 s)
	if cv.waitKey(1) & 0xFF == ord('q'):  # se a tecla 'q' for pressionada... (0xFF indica que somente o ultimo byte e verificado)
		break # saida do loop while
		
cap.release() # destroi o objeto de captura de video
cv.destroyAllWindows() # fecha as janelas abertas

