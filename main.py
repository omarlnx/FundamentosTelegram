#Importaciones y configuración
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
#chat_id = XXXXXXXXX



# === Funciones auxiliares ===
def procesar_texto_funcion(texto):
    # Lógica de procesamiento de texto
    texto_modificado = texto.replace('.com', '.mx', 1).removeprefix('https//:').removesuffix('.mx')
    return texto_modificado

# === Handlers para cada comando ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Usuario: {update.message.chat.id}, a ejecutado el comando /start')
    """Envía un mensaje de bienvenida"""
    welcome_msg = (
        "¡Hola! Soy tu bot de eco. 👂🏻\n\n"
        "Comandos disponibles:\n"
        "/procesar <texto> - Procesa el texto con reglas de ejemplo\n"
        "/playlist - Gestiona tu playlist musical\n"
        )
    await update.message.reply_text(welcome_msg)


async def procesar_texto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Usuario: {update.message.chat.id}, a escrito :{context.args} , es un a lista. Obtenemos str: {context.args[0]}')

    '''Usar update.message.text para obtener todo el mensaje.
       Usar context.args para obtener solo los argumentos después del comando.'''
    mensaje_recibido = context.args[0]
    print(f'Usuario: {update.message.chat.id}, a escrito un mensaje: "{mensaje_recibido}"')
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

    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    
    print("🤖 Bot iniciado correctamente")
    application.run_polling()

if __name__ == '__main__':
    main()

