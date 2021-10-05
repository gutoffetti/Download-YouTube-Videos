from os import remove
from pytube import YouTube, streams

###### BASE CODE
# Cria objeto com url do vídeo a ser baixado
#video = YouTube('https://www.youtube.com/watch?v=1j_E8SSVpdY')

# Configura a melhor qualidade de vídeo
#stream = video.streams.get_highest_resolution()

# Faz o download do vídeo e o salva na pasta "x". (cria a pasta "x" no diretório em que o arquivo .py está)
#stream.download(output_path='./download')
###### BASE CODE


# Asking the user where are the complete local file with video links
file_path = input('Insira o caminho completo do arquivo com o links para download:')
#local file for tests: C:\Users\Gustavo\Desktop\TesteDownloadYT\LinksDownload.txt

# Asking the complete path where the user want to save the videos
save_path = input('Insira o caminho completo da pasta em que você deseja salvar seus vídeos:')
#local file for tests: C:\Users\Gustavo\Desktop\downloadteste

# Reading the files to extract the links
with open(file_path, 'r') as file: # personal observation: r before the file path to produce a raw string.
    links = file.readlines()

# Saving the links on a list and informing the user if the file have any invalid link, and where.
videos_yt = [];
for line, link in enumerate(links):
    if 'www.youtube.com' in link:
        videos_yt.append(link);
    else: 
        print('Linha {} não possui um link válido.'.format(line+1));

# Downloading the videos and informing, with the title, if the download was successfully completed
for link in videos_yt:
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path= save_path)
    print('O vídeo: {} foi baixado com sucesso!'.format(video.title));

print('Os vídeos foram salvos no caminho informado: {}'.format(save_path))