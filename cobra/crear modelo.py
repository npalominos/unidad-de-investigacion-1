from __future__ import print_function

from cobra import Model, Reaction, Metabolite
from cobra.flux_analysis import flux_variability_analysis
import cobra.test


def MostrarSistema():
	out = open("modelo.txt", "a")
	
	print('%i reaction' % len(model.reactions))
	print('%i metabolites' % len(model.metabolites))
	print('%i genes' % len(model.genes))
	
	out.write('%i reaction' % len(model.reactions)+"\n")
	out.write('%i metabolites' % len(model.metabolites)+"\n")
	out.write('%i genes' % len(model.genes)+"\n")
	
	print("")
	out.write("\n")
	
	print("Reactions")
	print("---------")
	out.write("Reactions"+"\n")
	out.write("---------"+"\n")
	
	i=0
	for x in model.reactions:
	    print("%s : %s" % (x.id, x.reaction))
	    out.write("%s : %s" % (x.id, x.reaction)+"\n")
	    i+=1
        print(str(i)+" REACCIONES")
        out.write(str(i)+" REACCIONES"+"\n")
	
	print("")
	print("Metabolites")
	print("-----------")
	
	out.write("\n")
	out.write("Metabolites"+"\n")
	out.write("-----------"+"\n")
	
	i=0
	for x in model.metabolites:
	    print('%9s : %s' % (x.id, x.formula))
	    out.write('%9s : %s' % (x.id, x.formula)+"\n")
	    i+=1
        print(str(i)+" METABOLITOS")
        out.write(str(i)+" METABOLITOS"+"\n")	    

	print("")
	print("Genes")
	print("-----")
	
	out.write("\n")
	out.write("Genes"+"\n")
	out.write("-----"+"\n")
	
	i=0
	for x in model.genes:
	    associated_ids = (i.id for i in x.reactions)
	    print("%s is associated with reactions: %s" %
		  (x.id, "{" + ", ".join(associated_ids) + "}"))
	    out.write("%s is associated with reactions: %s" %
		  (x.id, "{" + ", ".join(associated_ids) + "}")+"\n")
        print(str(i)+" GENES")
        out.write(str(i)+" GENES"+"\n")	
	out.write("#############################################################\n")



########################################[TEST
def Test():
	model = Model('TEST')

	nombre="test_reaction"
	reaction = Reaction(nombre)
	reaction.name = '3 oxoacyl acyl carrier protein synthase n C140 '
	reaction.subsystem = 'Cell Envelope Biosynthesis'
	reaction.lower_bound = 0.  # This is the default
	reaction.upper_bound = 1000.  # This is the default

	reaction.add_metabolites({

	    Metabolite('malACP_c',formula='C14H22N2O10PRS',name='Malonyl-acyl-carrier-protein',compartment='c'): -1.0,
	    Metabolite('h_c', formula='H', name='H', compartment='c'): -1.0,
	    Metabolite('ddcaACP_c',formula='C23H43N2O8PRS',name='Dodecanoyl-ACP-n-C120ACP',compartment='c'): -1.0,
	    Metabolite('co2_c', formula='CO2', name='CO2', compartment='c'): 1.0,
	    Metabolite('ACP_c',formula='C11H21N2O7PRS',name='acyl-carrier-protein',compartment='c'): 1.0,
	    Metabolite('3omrsACP_c',formula='C25H45N2O9PRS',name='3-Oxotetradecanoyl-acyl-carrier-protein',compartment='c'): 1.0
	})

	reaction.reaction 
	reaction.gene_reaction_rule = '( STM2378 or STM1197 )'
	reaction.genes

	model.add_reactions([reaction])

	print('%i reaction' % len(model.reactions))
	print('%i metabolites' % len(model.metabolites))
	print('%i genes' % len(model.genes))

	MostrarSistema()

	model.objective = nombre
	print(model.objective.expression)
	print(model.objective.direction)


#########AGREGAR METABOLITOS
def AgregarMetabolito(reaccion,metabolito):
	metabolitos=[]
	archivo = open("metabolitos.csv", "r")

	#primera linea titulos (saltar)
	linea = archivo.readline()

	m=1
	while(linea!=""):
	   #try:
	    linea = archivo.readline()	
	    parametro=linea.split(";")
	    #print("m"+str(m)+": "+parametro[0])
	    m+=1
	    if(parametro[0]==metabolito):
	      id_met=parametro[0][:len(parametro[0])-3]
	      cpd=parametro[1]
	      descripcion=parametro[2]
	      form=parametro[4]
	      compartimento=parametro[0][len(parametro[0])-2:len(parametro[0])-1] 
	      print(" >"+id_met+" "+cpd+" "+descripcion+" "+form+" "+compartimento)


	      reaccion.add_metabolites({Metabolite(id_met,formula=form,name=descripcion,compartment=compartimento):1.0})  
	      
	      
	   #except:
	    #break
	   
	archivo.close()


#########AGREGAR REACCIONES
def AgregarReacciones(model):
	archivo = open("reacciones.csv", "r")
	#primera linea titulos (saltar)
	linea = archivo.readline()
	r=1
	i=0
	while(linea!=""):

	    linea = archivo.readline()

	    parametro=linea.split(";")
	    
	    if(len(parametro)>0):

             try:
              #extraigo parametros

	      id_rxn=parametro[0]
	      descripcion=parametro[1]
	      formula=parametro[2]
	      subsystem=parametro[7]
	      lbound=parametro[9]
	      ubound=parametro[10]
	      
	      out = open("modelo.txt", "a")
	      out.write("$$$AGREGANDO REACCION "+str(i)+":  id:"+id_rxn+" %desc:"+descripcion+" %form:"+formula+" %subst:"+subsystem+" %lb:"+lbound+" %ub"+ubound+"\n")
	      i+=1
	      out.close
	      
	      #defino la reaccion
	      reaction = Reaction(id_rxn)
	      reaction.name = descripcion
	      reaction.subsystem = subsystem
	      reaction.lower_bound = float(lbound)
	      reaction.upper_bound = float(ubound)
	      
	      ###########HAY QUE AGREGAR CADA METABOLITO DE LA REACCION Y SUS PROPIEDADES
	      ###########SIN TENER QUE AGREGAR TODA LA LISTA
	      
	      segmento=formula.split(" ")
	      
	      #ejemplo de reaccion  34hpp[c] + o2[c]  -> co2[c] + hgentis[c] 

	      for metabolito in segmento:
		 #elimino caracteres + -> y espacio
		 if(len(metabolito)>3):
		   #print("    $$"+metabolito)
		   AgregarMetabolito(reaction,metabolito)
	      ###########
	      
	      reaction.reaction 
	      reaction.gene_reaction_rule = '( STM2378 or STM1197 )'
	      reaction.genes   
	      model.add_reactions([reaction])
	      MostrarSistema()
	      print("#############################################################")
	      
	      print("r"+str(r)+": "+id_rxn+" >"+formula)
	      r+=1
             except:
	      break
	    
	archivo.close()

	MostrarSistema()

###########################[MAIN

model = Model('PSEUDOMONAS SYRINGAE NP2018')

out = open("modelo.txt", "w")
out.close
AgregarReacciones(model)

##GUARDAR MODELO
cobra.io.save_matlab_model(model, "testNP.mat")
cobra.io.write_sbml_model(model, "testNP.xml")

##FBA
solution = model.optimize()
print(solution)
solution.objective_value

model.optimize().objective_value

model.summary()

flux_variability_analysis(model, model.reactions[:10])

cobra.flux_analysis.flux_variability_analysis(model, model.reactions[:10], fraction_of_optimum=0.9)
	    

model.optimize()
model.summary(fva=0.95)

	    
