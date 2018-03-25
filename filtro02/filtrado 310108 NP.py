#######################################
#UNIDAD DE INVESTIGACION 01
#CODIGO 03 - FILTRADO EXPRESION/INHIBICION
#NESTOR PALOMINOS 31.01.2018
#######################################

#INPUTS:

#Salida_Filtrada_Pseudomonas2.csv
#N;COG;GI;PI;LT;LT2;Entry;F1;F2;F3;F4;REV/UNR
#11;C;gi|28850536;AAO53616.1;PSPTO_0062;PSPTO_0062;Q88BF5;0;0;477120;0;unreviewed
#12;T;gi|28850538;AAO53618.1;PSPTO_0064;PSPTO_0064;Q88BF3;0;0;249520;0;unreviewed

#ESTRUCTURA DEL ARCHIVO PROTEIN.ACTIONS
#item_id_a;item_id_b;mode;action;is_directional;a_is_acting;score
#223283.PSPTO_0080;223283.PSPTO_4502;expression;inhibition;t;f;295
#223283.PSPTO_0080;223283.PSPTO_5040;expression;inhibition;t;t;810
#223283.PSPTO_0080;223283.PSPTO_5040;expression;inhibition;t;f;810
   
#VALOR DE EXPRESION para F1->parametros[8] , F2->parametros[9] ,F4->parametros[10]

tipo="expression"
caso="F4"

prot_interactions="223283.protein.actions.v10.5.csv"

c=0
if caso=="F1":
  c=8
if caso=="F2":
  c=9
if caso=="F4":
  c=10

#######################################[BUSCAR
def Buscar(dato):

  archivo = open("Salida_Filtrada_Pseudomonas.csv", "r")
  linea = archivo.readline()
  i=0

  while(linea!=""):
    
    linea = archivo.readline()
    parametros=linea.split(";")
    salida="-"
    
    x=""
 
    #CONSIDERANDO SOLO EXPRESADAS
    #if len(parametros)>9 and parametros[c]!="0" and (parametros[11])[:-1]=="reviewed":
    
    #CONSIDERANDO TODAS (EXPRESADAS Y NO EXPRESADAS
    if len(parametros)>9 and (parametros[11])[:-1]=="reviewed":

      expresion=parametros[c]
      x=parametros[4]
      
      try:
        #print "**"+dato[7:] +"="+x+" ->"+expresion
    
        if x==dato[7:]:
          salida=x+" >ok"
          #print salida
          #print parametros[11] ->CONFIRMA REVIEWED
          return 1
          break

      except:
          print "-"
    
    i+=1	  

  archivo.close()
  return 0


#######################################[EXPR
def Expr(dato,i):

  archivo = open("Salida_Filtrada_Pseudomonas.csv", "r")
  linea = archivo.readline()
  i=0
  
  while(linea!=""):
    
    linea = archivo.readline()
    parametros=linea.split(";")
    salida="-"

    #print parametros[4]+"-"+dato.replace("223283.", "")
    
    try:
     if parametros[4]==dato.replace("223283.", ""):
       return parametros[i]
       print parametros[4]+" - " +parametros[i]
    except:
       archivo.close()
       return 0


#######################################[MAIN

#ABRO EL ARCHIVO DE INTEERACCIONES (P1;P2;SCORE) Y BUSCO P1 Y P2 DENTRO DEL 
#ARCHIVO CON LOCUSTAG EXPRESADOS SEGUN F1,F2 O F4

base = open(prot_interactions, "r")
  
#CREA UN ARCHIVO DE SALIDA EN BLANCO
f = open (caso+" - interacciones_filtradas_EXP_all.csv", "w")
f.write("item_id_a;item_id_b;mode;action;is_directional;a_is_acting;score;exp1;exp2\n")
f.close()
  
p1=0
p2=0
score=""
  
linea = base.readline()
  

while(linea!=""):
  linea = base.readline()
  if linea[0:6]=="223283":
    datos=linea.split(";")
    #if datos[2]==tipo and datos[5]=="t":
    if datos[5]=="t":

      #print tipo
      #print linea
      #print "%%"+datos[0]+"##"+datos[1]
      
      p1=Buscar(datos[0])  
      p2=Buscar(datos[1])

      exp1=str(Expr(datos[0],c))
      exp2=str(Expr(datos[1],c))
    
      #datos[0]=item_id_a
      #datos[1]=item_id_b
      #datos[2]=mode
      #datos[3]=action
      #datos[4]=is_directional
      #datos[5]=a_is_acting
      #datos[6]=score 
 
      try:
       print ">>>>>>"+datos[0][7:]+";"+datos[1][7:]+";"+(datos[6])[:-1]+"-> " +str(p1)+";"+str(p2)+" - "+exp1+";"+exp2
      except:
       print "-"
     
      #SI AMBOS CODIGOS EXISTEN EN LA BASE DE LOCUS_TAG, ANEXA LA INTERACCION EN EL ARCHIVO DE SALIDA
      #ADEMAS SOLO SE CONSIDRARA LA DIRECCION (datos[5]) A->B PARA EVITAR REDUNDANCIAS
    
      if str(p1)=="1" and str(p2)=="1":
        print "&&&AGREGADA"
        f = open (caso+" - interacciones_filtradas_EXP_all.csv", "a")
        txt=linea.replace("223283.", "")[:-1]+";"+exp1+";"+exp2+"\n"
        f.write(txt)
        f.close()
      
      p1=0
      p2=0

base.close()

#OUTPUT

#>>>>>>PSPTO_0609;PSPTO_2383;544-> 1;1 - 91;386
#&&&
#reviewed
#>>>>>>PSPTO_0609;PSPTO_4147;715-> 1;1 - 91;569
#&&&
#reviewed

#interacciones_filtradas_EXP_all.csv
#item_id_a;item_id_b;mode;action;is_directional;a_is_acting;score;exp1;exp2
#PSPTO_0075;PSPTO_5150;binding;;f;t;248;15;739
#PSPTO_0077;PSPTO_0624;binding;;f;t;156;17;101
#PSPTO_0077;PSPTO_0617;catalysis;;t;t;499;17;95
#PSPTO_0077;PSPTO_0616;catalysis;;t;t;461;17;94
