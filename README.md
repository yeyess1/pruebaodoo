# pruebaodoo


1.Instalar el modulo: Spoti - ys

2. Ir a modelos, external.py y agregar la url del servicio de odoo, nombre de la Base de datos, usuario y clave del usuario de odoo, despeues ejecutar el archivo para insertar los generos.

![image](https://user-images.githubusercontent.com/92695542/192436095-473ffebc-34f3-4bdc-8997-4bdcce65892a.png)


3. Debido al tiempo no autentique mi propio token, por lo que hay que agregarlo:
  abrir el enlace y dar click en GET Token 
  ![image](https://user-images.githubusercontent.com/92695542/192434814-4eb29197-27ea-4559-9d38-7022bd515a10.png)
 Copiar el token y agregarlo, en Models, res.partner linea 47, eg:
 
 ![image](https://user-images.githubusercontent.com/92695542/192434975-f36de613-9b6a-4aac-802e-7eb2f5d100d4.png)
 
4. Actualizar el modulo Spoti - ys.

5. Ya en la UI, ir al modulo Contacts, crear un contacto, seleccionar en el campo generos los generos a cosultar.

6. Se almacenan las urls en el campo Links recomendados. 

