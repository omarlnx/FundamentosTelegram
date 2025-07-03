#Importaciones y configuración
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from pprint import pprint
from random import randint

load_dotenv()
#chat_id = 1737086827



# === Funciones auxiliares ===
def procesar_texto_funcion(texto):
    # Lógica de procesamiento de texto
    texto_modificado = texto.replace('.com', '.mx', 1).removeprefix('https//:').removesuffix('.mx')
    return texto_modificado

# === Handlers para cada comando ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Usuario: {update.message.chat.id}, a ejecutado el comando /start')
    """Envía un mensaje de bienvenida"""
    nombre_usuario = update.message.chat.first_name
    welcome_msg = f'''¡Hola! {nombre_usuario} Aprenderemos como usar el lenguaje  Pyhton en este proyecto.\n\n
    Comandos disponibles:\n
    /procesar <texto> - Procesa el texto con reglas de ejemplo\n
    /playlist Laurita garza, La desentendida, agua salada, Friday in my love, Fallaste corazon\n
    '''
    await update.message.reply_text(welcome_msg)


async def procesar_texto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Usuario: {update.message.chat.id}, a escrito :{context.args} , es un a lista. Obtenemos str: {context.args[0]}')

    '''Usar update.message.text para obtener todo el mensaje.
       Usar context.args para obtener solo los argumentos después del comando.'''
    mensaje_recibido = context.args[0]
    print(f'Usuario: {update.message.chat.id}-{update.message.chat.first_name}: a escrito un mensaje: "{mensaje_recibido}"')
    resultado = procesar_texto_funcion(mensaje_recibido)
    await update.message.reply_text(f"Texto procesado: <code>{resultado}</code>", parse_mode='HTML')
    print(f'Respuesta: "{resultado}", enviada al usuario : {update.message.chat.id}')

'''
    async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Repite el mensaje del usuario"""
    object_update = update
    #print(f'Onbjeto recibido deste telegram : {object_update.to_dic}') #Muestra los datos obtenidos

    mensaje_recibido = update.message.text
    print(f'Usuario: {update.message.chat.id}, a escrito un mensaje: "{mensaje_recibido}"')
    #Mensaje inicial para el usuario despues de escribir la palabra

    #Mensaje inicial despues de obtener texto ingresado por usuario
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🔄 Modificacion del texto usando .repace() .removeprefix() removesuffix() ")

    #await update.message.reply_text(f'Mensaje original: "{mensaje_recibido}"')
    await update.message.reply_text(f"parse_mode='HTML': <code>{mensaje_recibido}</code>",parse_mode='HTML')

    msj_modificado = mensaje_recibido.replace('.com', '.mx', 1)
    await update.message.reply_text(f'Mensaje modicado: "<code>{msj_modificado}</code>"', parse_mode='HTML')
    msj_remove_prefix = msj_modificado.removeprefix('https//:')
    await update.message.reply_text(f'Prefijo eliminado: "<code>{msj_remove_prefix}</code>"', parse_mode='HTML')
    msj_suffix = msj_remove_prefix.removesuffix('.mx')
    await update.message.reply_text(f'Sufijo eliminado: "<code>{msj_suffix}</code>"', parse_mode='HTML')
    #Enviar mensajes sin contexto fuera del hilo de la conversacion
    # Paradigma proactivo send.message Necesitamos el chat id 
    await context.bot.send_message(chat_id=update.effective_chat.id, text="👍 Proceso finalizado con éxito!")
'''

#region Gestión de Playlist Musical
#    Crea una lista `playlist` con al menos 5 canciones (strings).
#    a) Imprime la playlist completa.
#    b) Mueve la primera canción al final de la playlist.
#    c) Elimina una canción específica por su nombre.
#    d) Inserta una nueva canción en la segunda posición.
#    e) Imprime la playlist final ordenada alfabéticamente de forma permanente.
#endregion 
async def procesar_playlist (update: Update, context: ContextTypes.DEFAULT_TYPE )->None:
    #    a) Imprime la playlist ingresada por el usuario completa.
    playlist_usuario = context.args
    print(f'Usuario: {update.message.chat.id}, a enviado su playlist :{playlist_usuario}')
    # playlist :['ADondeVas,', 'Fryday,', 'LaVacaLola,', 'AguaSalada']#Posterior eliminar ','
    #lista_playlist = " ".join(playlist_usuario)
    await update.message.reply_text(f'''{update.message.chat.first_name} tienes la mejor playlist 🪗👯‍♀️\n\n{playlist_usuario}''')

    #    b) Mueve la primera canción al final de la playlist.
    primer_cancion = playlist_usuario.pop(0)
    playlist_usuario.append(primer_cancion)
    await update.message.reply_text(f'➡️Primera por ultima cancion ⬅️\n\n{playlist_usuario}')

    #    c) Elimina una canción específica por su nombre, usaremos random.
    #   El bot determinara que cancion eliminar
    posicion_aletaoria = randint(0,3)
    print(f'Numero aleatorio generado {posicion_aletaoria}')
    cancion_eliminada = playlist_usuario[posicion_aletaoria]
    print(f'Cancio aleatoria seleccionada {cancion_eliminada}')
    playlist_usuario.remove(playlist_usuario[posicion_aletaoria])
    await update.message.reply_text(f'{update.message.chat.first_name} Lo sentimos el bot ha elimindo una cancion al azar 🤖⚡️❌ {cancion_eliminada.removesuffix(',')}\nPlaylist actualizada:\n {playlist_usuario}')

    #    d) Inserta una nueva canción en la segunda posición.
    playlist_usuario.insert(0, 'Gracias a la vida')
    await update.message.reply_text(f'El bot te ha siguerido la primer cancion en tu playlist 🤖👯‍♀️➡️①\n{playlist_usuario}')

    #    e) Imprime la playlist final ordenada alfabéticamente de forma permanente.
    playlist_usuario.sort()
    await update.message.reply_text(f'Te comparto tu playlist oredenada de manera alfabetica:🔤\n{playlist_usuario}')


    







# === main() para registrar handlers y arrancar el bot ===

def main() -> None:
    """Configura y ejecuta el bot"""
    # Obtiene el token de las variables de entorno
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    if not TOKEN:
        raise RuntimeError(
            "No se encontró el token.")
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("procesar", procesar_texto))
    application.add_handler(CommandHandler("playlist", procesar_playlist))

    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    
    print("🤖 Bot iniciado correctamente")
    application.run_polling()

if __name__ == '__main__':
    main()

