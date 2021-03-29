#9 heterograma
palabra_original=input("Ingresa la palabra a verificar si es un heterograma:")
palabra=list(palabra_original.lower())
dicc_aux={}

es_o_no='SI'

for c in palabra:
	if c.isalpha():									#Esta linea esta ya que en la practica daba como ejemplo de heterograma "no-se-duplica" 
		dicc_aux[c]=dicc_aux.get(c,0)+1				#Si no hay "c" en dicc_aux, lo crea con 0, si hay, le suma 1
		
for i in dicc_aux:
	if (dicc_aux[i]>1):
		es_o_no='NO'

print ('La palabara {} {} es un heterograma'.format (palabra_original, es_o_no))
		
