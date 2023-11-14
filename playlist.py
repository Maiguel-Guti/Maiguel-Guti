def main(clave_api, playlist_id, videos_por_pagina = 50):
    # videos_por_pagina son Maximo 50 por request, podria bajarse y usar time() para no saturar de requests
    flag = 0
    total_videos = 1
    siguiente_pagina = ''
    borrados = 0

    # Output
    video_ids = []
    canciones = []
    canales = []

    from googleapiclient.discovery import build

    youtube = build(serviceName='youtube', version='v3', developerKey = clave_api)

    while len(canciones) < total_videos:
        # El if es para la primera iteracion, cuando todavia no se usa PageToken

        #### Tratar de hacer este if/else una funcion #######

        if flag == 0:
            playlist = youtube.playlistItems().list(
            part ='snippet', # Este incluye los titulos
            playlistId = playlist_id,
            maxResults = videos_por_pagina #, Valor máximo de videos por request, default = 5
            # PageToken = ? ver si se puede sustituir con None
            )
            respuesta = playlist.execute()

            # Estas variables son para preparar la entrada al else:
            flag = 1
            total_videos = respuesta['pageInfo']['totalResults'] # Total de videos en la lista

        else:
            #codigo con PageToken
            print("Progreso: ",round(len(canciones)*100/total_videos, 1),"%")

            playlist = youtube.playlistItems().list(
            part ='snippet', # Este incluye los titulos
            playlistId = playlist_id,
            maxResults = videos_por_pagina, 
            pageToken = siguiente_pagina
            )
            respuesta = playlist.execute()

            #total_videos = respuesta['pageInfo']['totalResults'] # Total de videos en la lista

        # Se guardan las ids, canciones y canales de cada playlist en unas listas
        for video in range(len(respuesta['items'])):
            video_ids.append(respuesta['items'][video]['snippet']['resourceId']['videoId']) # [video] es porque items es una lista de diccionarios para cada video
            canciones.append(respuesta['items'][video]['snippet']['title'])
            try:
                canales.append(respuesta['items'][video]['snippet']['videoOwnerChannelTitle'])
            except:
                canales.append('[Video borrado]')
                borrados += 1 # los videos borrados no tienen la infor de channelTitle

        # Nueva forma devuelve None (sin error, en caso de que no haya Page Token)
        siguiente_pagina = respuesta.get('nextPageToken')

        # try:
        #     siguiente_pagina = respuesta['nextPageToken']
        # except:
        #     siguiente_pagina = None
        #     print("Fin, OwO el error")

    #########
    
    youtube.close()
    print("Videos borrados: ", borrados)

    return canciones, canales, video_ids

if __name__ == '__main__':
    print("-------------------------")
    import pandas as pd
    from os import environ
    api = environ['API_KEY']

    campos = main(
        clave_api = api, 
        playlist_id = "PLZPVLfJKqBg5M-htqE14ZL3Khl_jGlorq", 
        videos_por_pagina = 50)
    # Me gusta: PLZPVLfJKqBg5M-htqE14ZL3Khl_jGlorq
    # Pensar: PLZPVLfJKqBg7hnS3tj_JoWteN363xbuL3

    tabla = [['Cancion', 'Canal','Video ID']]
    for i in range(len(campos[0])): tabla.append([campos[0][i],campos[1][i],campos[2][i]])
    print('Creando csv...')

    import pandas as pd
    df = pd.DataFrame(tabla)
    df.to_csv("playlist_output.csv", encoding = 'utf-16', sep='#')


# Notas:
# Para saber nombres de cada video debo acceder a los IDs de video que devuelve la playlist, luego usar video.list()
# Cada request solo devuelve 50 videos de la playlist por pagina, hay que revisar cada pagina para obtener todos usando pageToken