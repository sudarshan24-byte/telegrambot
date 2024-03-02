# 29932859 /translate en How are you

from pyrogram import Client, filters
from googletrans import Translator
# from moviepy.editor import VideoFileClip
import os

bot = Client(
    'Translation Bot',
    api_id = '', # Your API ID here
    api_hash = '', # Your API Hash code
    bot_token= '' # Your Telegram Bot Token
)

translator = Translator()

help_command = '''
Namaste This is a help command
This bot can translate any text to your preferred language.

/start - Start the bot and see help.
/help - See this helpful message again.
/translate [language code] [text to be translated] - To translate the given text into the specified language.
/langcode - For Language Code.
'''

translate_command = '''
Use the /translate command and then type in your language and the message you want to be translated.
For example if you wanted to translate "How are you" into Hindi you would say:
/translate hi How are you
Here 'hi' is the language code in which you want to translate the text.

For language code use /langcode command.
'''


langcode_command = '''
Supported languages:
af: afrikaans
sq: albanian
am: amharic
ar: arabic
hy: armenian
az: azerbaijani
eu: basque
be: belarusian
bn: bengali
bs: bosnian
bg: bulgarian
ca: catalan
ceb: cebuano
ny: chichewa
zh-cn: chinese (simplified)
zh-tw: chinese (traditional)
co: corsican
hr: croatian
cs: czech
da: danish
nl: dutch
en: english
eo: esperanto
et: estonian
tl: filipino
fi: finnish
fr: french
fy: frisian
gl: galician
ka: georgian
de: german
el: greek
gu: gujarati
ht: haitian creole
ha: hausa
haw: hawaiian
iw: hebrew
he: hebrew
hi: hindi
hmn: hmong
hu: hungarian
is: icelandic
ig: igbo
id: indonesian
ga: irish
it: italian
ja: japanese
jw: javanese
kn: kannada
kk: kazakh
km: khmer
ko: korean
ku: kurdish (kurmanji)
ky: kyrgyz
lo: lao
la: latin
lv: latvian
lt: lithuanian
lb: luxembourgish
mk: macedonian
mg: malagasy
ms: malay
ml: malayalam
mt: maltese
mi: maori
mr: marathi
mn: mongolian
my: myanmar (burmese)
ne: nepali
no: norwegian
or: odia
ps: pashto
fa: persian
pl: polish
pt: portuguese
pa: punjabi
ro: romanian
ru: russian
sm: samoan
gd: scots gaelic
sr: serbian
st: sesotho
sn: shona
sd: sindhi
si: sinhala
sk: slovak
sl: slovenian
so: somali
es: spanish
su: sundanese
sw: swahili
sv: swedish
tg: tajik
ta: tamil
te: telugu
th: thai
tr: turkish
uk: ukrainian
ur: urdu
ug: uyghur
uz: uzbek
vi: vietnamese
cy: welsh
xh: xhosa
yi: yiddish
yo: yoruba
zu: zulu
'''



@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, 'Namaste This is a Text Translator Bot!')


@bot.on_message(filters.command('help'))
def command1(bot, message):
    bot.send_message(message.chat.id, help_command)


@bot.on_message(filters.command('translate'))
def command1(bot, message):
    if len(message.command) > 1:
        langcode = "".join(message.command[1])
        text = " ".join(message.command[2:])
        print(message.command)
        print(text)
        print(langcode)
        translated_text = translator.translate(text, src="auto", dest=langcode).text
        message.reply_text(translated_text)
    else:
        message.reply_text(translate_command)


        
class BotCode:
    @staticmethod
    @bot.on_message(filters.command('langcode'))
    def handle_langcode_command(bot, message):
        bot.send_message(message.chat.id, langcode_command)


# def convert_to_gif(video_path, gif_path):
#     clip = VideoFileClip(video_path)
#     clip.write_gif(gif_path)


# @bot.on_message(filters.video)
# async def video_to_gif(bot, message):
#     video = message.video
#     video_path = await bot.download_media(message=video)
#     gif_path = video_path.replace(".mp4", ".gif")
#     convert_to_gif(video_path, gif_path)
#     await message.reply_animation(animation=gif_path)
#     os.remove(video_path)
#     os.remove(gif_path)

print('Running....')
bot.run()