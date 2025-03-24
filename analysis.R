if (!dir.exists("cultures")) {
  cat("Erro: diretório 'cultures' não encontrado.\n")
  quit(status = 1)
}

csvfiles <- list.files("cultures", pattern = "\\.csv$", full.names = TRUE)
if (length(csvfiles) == 0) {
  cat("Erro: Sem arquivo CSV no diretório 'cultures'.\n")
  quit(status = 1)
}

for (file in csvfiles) {
  cat(sprintf("\n===== Analisando arquivo: %s =====\n", file))

  arqcsv <- read.csv(file, fileEncoding = "latin1")
  
  vetorArea <- numeric(nrow(arqcsv))

  for (i in 1:nrow(arqcsv)) {
    forma <- as.character(arqcsv[i, 2])
    base  <- as.numeric(arqcsv[i, 3])
    altura <- as.numeric(arqcsv[i, 4])
    if (forma == "Retângulo") {
      vetorArea[i] <- base * altura
    } else {
      vetorArea[i] <- (base * altura) / 2
    }
  }
  
  dados_numericos <- arqcsv[, sapply(arqcsv, is.numeric)]
  media_linhas <- rowMeans(dados_numericos, na.rm = TRUE)
  desvio_linhas <- apply(dados_numericos, 1, sd, na.rm = TRUE)
  
  arqcsv$Area <- vetorArea
  arqcsv$Media_Linha <- media_linhas
  arqcsv$Desvio_Padrao_Linha <- desvio_linhas
  
  cat("\nDados do arquivo:\n")
  print(arqcsv, row.names = FALSE)

  MediaRate <- mean(arqcsv$rate, na.rm = TRUE)
  DVRate <- sd(arqcsv$rate, na.rm = TRUE)
  MediaArea <- mean(arqcsv$Area, na.rm = TRUE)
  DVArea <- sd(arqcsv$Area, na.rm = TRUE)

  cat("\n--- Estatísticas Globais ---\n")
  cat(sprintf("Média de insumos (ml/m): %.2f\n", MediaRate))
  cat(sprintf("Desvio padrão de insumos (ml/m): %.2f\n", DVRate))
  cat(sprintf("Média da área cultivada: %.2f m²\n", MediaArea))
  cat(sprintf("Desvio padrão da área cultivada: %.2f m²\n", DVArea))
  cat("\n============================\n")
}
