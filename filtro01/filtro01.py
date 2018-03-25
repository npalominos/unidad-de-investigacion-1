#######################################
#UNIDAD DE INVESTIGACION 01
#CODIGO 01 - LOCUSTAG + CODIGOS UNIPROT
#NESTOR PALOMINOS 2018
#######################################





def Buscar(dato):
  anotaciones = open("AE016853-02-09.txt", "r")
  
  locus_tag=""
  protein_id=""
  
  linea = anotaciones.readline()
  
  while(linea!=""):
    linea = anotaciones.readline()
    if linea.find("/protein_id") >= 0:
        protein_id=linea
    if linea.find("/locus_tag") >= 0:
        locus_tag=linea
    if linea.find(dato) >= 0:
        print "$$$$$$$"
        print "protein_id:"+protein_id
        print "locus_tag:"+locus_tag	

  anotaciones.close()



#################[MAIN

archivo = open("archivo.csv", "r")

linea = archivo.readline()
i=0

while(linea!=""):
  linea = archivo.readline()
  if linea.find("[Pseudomonas syringae]") >= 0:
   print str(i)+";"+linea
   dato = linea[5:13]
   print dato
   Buscar(dato)   
  i+=1	  

archivo.close()