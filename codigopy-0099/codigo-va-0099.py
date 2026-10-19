# Medina Anais NC 0099
# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os 
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0099",
    "rinoceronte.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
rinoceronte = cv2.imread(ruta_imagen)
# print(rinoceronte) muestra las matrices de la imagen
# convertir de BGR a RGB color rojo COLOR_BGR2RGB
nochi = cv2.cvtColor(rinoceronte, cv2.COLOR_BGR2RGB)
#v2.imshow("rinoceronte original 0099",rinoceronte)
cv2.imshow("rinoceronte color 0099",nochi)
cv2.waitKey(0)  # Tiempo de espera hasta presionar una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas

