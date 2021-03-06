# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANT without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# Authors: Cl�udio Guimar�es Matos J�nior and supported by Welington Gon�alves Silva
# Created: 2022-06-20. Last update at 2022-06-20.

library(rlist)
library(bio3d)

setwd("C:\\JUNHOIC2022\\1-7NG6-ALD\\LIGANTES") #Definir diret�rio dos arquivos pdb

temp = list.files(pattern="*.pdb") #Lista de arquivos do diret�rio
print(temp)

N = length(temp); 		   #N�mero de arquivos do diret�rio

pdb_list = list()

for(i in 1:N){
  
  pdb <- read.pdb(file = temp[i])
  pdb_list <- list.append(pdb_list, pdb)
  
}

v = c()
for(i in 2:N){
print(rmsd(a=pdb_list[[1]], b=pdb_list[[i]], fit=TRUE))
  # guardar num vetor para criar grafico de distribuicao
  v = c(v, rmsd(a=pdb_list[[1]], b=pdb_list[[i]], fit=TRUE))
  
}
# plot(density(v))