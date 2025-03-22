if(!dir.exists("cultures")) {
    cat("Erro: diretório não encontrado")
    quit(status = 1)
}

csvfiles <- list.files("cultures", pattern = "\\.csv$", full.names = TRUE)

if (length(csvfiles) == 0 ) {
    cat("Erro: Sem arquivo csv no diretório")
    quit(status = 1)
}

for (file in csvfiles){

#Lendo CSV -> local: Diretório destino + FarmTech_Solutions-main\cultures
#Obs: passando fileEncoding = "latin1" para tratar o problema de acentos.

arqcsv = read.csv(file, fileEncoding = "latin1")


#Verificando o total de linhas (culturas) :
#t_linhas <- nrow(arqcsv4)
#print(t_linhas)

#Criando vetor para inserir os calculos por linha, e depois adicionando na tabela.
vetorArea = c()


#Loop para tratativa dos registros do CSV importado

for (cultures in range(1,nrow(arqcsv)) ) {
  #print(arqcsv[cultures,2])
  #print (arqcsv[cultures])
  #print (cultures)
  #vetorArea[cultures] = cultures
  
  if (arqcsv[cultures,2] == "Retângulo"){
    #print ("Retangulo")
    vetorArea[cultures] = (arqcsv[cultures,3] * arqcsv[cultures,4])
  }
  
  else {
    vetorArea[cultures] = ((arqcsv[cultures,3] * arqcsv[cultures,4]) / 2)
  }
  
} 


dados_numericos <- arqcsv[, sapply(arqcsv, is.numeric)]
media_linhas <- rowMeans(dados_numericos, na.rm = TRUE)
desvio_linhas <- apply(dados_numericos, 1, sd, na.rm = TRUE)

arqcsv

arqcsv$Area <- vetorArea
arqcsv$media_linha <- media_linhas
arqcsv$desvio_padrao_linha <- desvio_linhas

print(arqcsv)

MediaRate <- mean(arqcsv$rate, na.rm = TRUE)
print(paste("A média de insumos(ml/m)' é de:", MediaRate))

DVRate <- sd(arqcsv$rate, na.rm = TRUE)
print(paste("O Desvio padrão de insumos(ml/m) (Sem separação de tipo) ' é de:", DVRate))

MediaArea <- mean(arqcsv$Area, na.rm = TRUE)
print(paste("A média da area cultivada é:", MediaArea))

DVArea <- sd(arqcsv$Area, na.rm = TRUE)
print(paste("O desvio padrão da area cultivada (Sem separação de tipo) é:", DVArea))
}