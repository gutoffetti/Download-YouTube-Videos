from pytube import YouTube

# Cria objeto com url do vídeo a ser baixado
video = YouTube('https://www.youtube.com/watch?v=1j_E8SSVpdY')


# Configura a melhor qualidade de vídeo
stream = video.streams.get_highest_resolution()




# Faz o download do vídeo e o salva na pasta "x". (cria a pasta "x" no diretório em que o arquivo .py está)
stream.download(output_path='./download')