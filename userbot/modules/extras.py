from userbot import bot
from userbot.events import register
from telethon import events


@register(outgoing=True, pattern="^.leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Group kek!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sar This is Not A Chat`')
                    
@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@register(outgoing=True, pattern="^.gey$")  
async def gey(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭━━━╮╭━━━╮╭╮╱╱╭╮`" 
                     "`\n┃╭━╮┃┃╭━╮┃┃╰╮╭╯┃`" 
                     "`\n┃┃╱╰╯┃┃╱┃┃╰╮╰╯╭╯`" 
                     "`\n┃┃╭━╮┃╰━╯┃╱╰╮╭╯`"
                     "`\n┃╰┻━┃┃╭━╮┃╱╱┃┃`"
                     "`\n╰━━━╯╰╯╱╰╯╱╱╰╯`")
        
   
@register(outgoing=True, pattern="^.xd$")  
async def xd(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭━╮╭━╮╭━━━╮`"
                     "`\n╰╮╰╯╭╯╰╮╭╮┃`"
                     "`\n╱╰╮╭╯  ┃┃┃┃`"
                     "`\n╱╭╯╰╮  ┃┃┃┃`"
                     "`\n╭╯╭╮╰╮╭╯╰╯┃`"
                     "`\n╰━╯╰━╯╰━━━╯`") 

@register(outgoing=True, pattern="^.fail$")  
async def fail(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `" 
                     "`\n████▌▄▌▄▐▐▌█████ `"    
                     "`\n████▌▄▌▄▐▐▌▀████ `"       
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")    
          
@register(outgoing=True, pattern="^.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `" 
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"       
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `" 
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `") 

@register(outgoing=True, pattern="^.mp$")
async def mp(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭━╮╭━╮╭━━╮╭━━━╮╭━━━╮╭━━╮╭━━━╮╭━╮╱╭╮`" 
                     "`\n┃┃╰╯┃┃╰┫┣╯┃╭━╮┃┃╭━╮┃╰┫┣╯┃╭━╮┃┃┃╰╮┃┃`" 
                     "`\n┃╭╮╭╮┃╱┃┃╱┃╰━━╮┃╰━━╮╱┃┃╱┃┃╱┃┃┃╭╮╰╯┃`" 
                     "`\n┃┃┃┃┃┃╱┃┃╱╰━━╮┃╰━━╮┃╱┃┃╱┃┃╱┃┃┃┃╰╮┃┃`" 
                     "`\n┃┃┃┃┃┃╭┫┣╮┃╰━╯┃┃╰━╯┃╭┫┣╮┃╰━╯┃┃┃╱┃┃┃`" 
                     "`\n╰╯╰╯╰╯╰━━╯╰━━━╯╰━━━╯╰━━╯╰━━━╯╰╯╱╰━╯`" 
                     "`\n╭━━━╮╭━━━╮╭━━━╮╭━━━╮╭━━━╮╭━━━╮`" 
                     "`\n┃╭━╮┃┃╭━╮┃┃╭━╮┃┃╭━╮┃┃╭━━╯╰╮╭╮┃`" 
                     "`\n┃╰━╯┃┃┃╱┃┃┃╰━━╮┃╰━━╮┃╰━━╮╱┃┃┃┃╱╭╮`" 
                     "`\n┃╭━━╯┃╰━╯┃╰━━╮┃╰━━╮┃┃╭━━╯╱┃┃┃┃╭╯╰╮`" 
                     "`\n┃┃╱╱╱┃╭━╮┃┃╰━╯┃┃╰━╯┃┃╰━━╮╭╯╰╯┃╰╮╭╯`" 
                     "`\n╰╯╱╱╱╰╯╱╰╯╰━━━╯╰━━━╯╰━━━╯╰━━━╯╱╰╯`" )
           
@register(outgoing=True, pattern="^.gtfo$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n███████████████████████████████ `" 
                     "`\n█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█ `" 
                     "`\n█───────█──────█───────█──────█ `" 
                     "`\n█──███──███──███──███▄▄█──██──█ `" 
                     "`\n█──███▄▄███──███─────███──██──█ `" 
                     "`\n█──██───███──███──██████──██──█ `" 
                     "`\n█──▀▀▀──███──███──██████──────█ `" 
                     "`\n█▄▄▄▄▄▄▄███▄▄███▄▄██████▄▄▄▄▄▄█ `" 
                     "`\n███████████████████████████████ `") 
                       
            
@register(outgoing=True, pattern="^.fag$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     "`\n█       STFU FAGGOT'S`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               
            
@register(outgoing=True, pattern="^.taco$")  
async def taco(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n{\__/}`"
                     "`\n(●_●)`"
                     "`\n( >🌮 Want a taco?")
   
@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")
        
        
@register(outgoing=True, pattern="^.tf$")  
async def tf(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")  
       
                  
@register(outgoing=True, pattern="^.gei$")            
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈NIGGA U GEI`"
                    "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")    

@register(outgoing=True, pattern="^.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@register(outgoing=True, pattern="^.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")

@register(outgoing=True, pattern="^.hey$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@register(outgoing=True, pattern="^.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
"`\n┗━━┻━┛`")
