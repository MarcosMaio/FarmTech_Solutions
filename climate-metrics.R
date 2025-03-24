library(httr)
library(jsonlite)

latitude <- -22.9068
longitude <- -43.1729

url <- paste0("https://api.open-meteo.com/v1/forecast?latitude=", latitude,
              "&longitude=", longitude, "&current_weather=true")

response <- GET(url)


if (response$status_code != 200) {
  cat("Erro ao acessar a API meteorológica.\n")
  quit(status = 1)
}

weather_data <- fromJSON(rawToChar(response$content))

cat("Clima Atual:\n")
cat("Temperatura:", weather_data$current_weather$temperature, "°C\n")
cat("Velocidade do Vento:", weather_data$current_weather$windspeed, "km/h\n")
cat("Direção do Vento:", weather_data$current_weather$winddirection, "°\n")
