from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐬𝐚𝐩𝐭𝐢𝐲𝐚 𝐧𝐢🤗🥱** ",
           " **𝐲𝐞𝐧𝐧𝐚 𝐩𝐚𝐧𝐫𝐚😊** ",
           " **𝐲𝐞𝐧𝐧𝐚 𝐨𝐨𝐫𝐮 𝐧𝐢🧐** ",
           " **𝐲𝐞𝐧 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐯𝐚𝐫𝐚𝐝𝐡𝐮 𝐢𝐥𝐥𝐚🥲** ",
           " **𝐲𝐞𝐧 𝐨𝐫𝐮 𝐭𝐚𝐠 𝐤𝐮𝐝𝐚 𝐢𝐥𝐥𝐚🥺** ",
           " **𝐯𝐢𝐭𝐭𝐮𝐥𝐚 𝐲𝐞𝐧𝐧𝐚 𝐬𝐩𝐥🤭** ",
           " **𝐲𝐞𝐧𝐧𝐚 𝐩𝐚𝐝𝐢𝐜𝐡𝐢𝐫𝐮𝐤𝐤𝐚 𝐧𝐢🤨** ",
           " **𝐮𝐧𝐧𝐚 𝐯𝐢𝐝𝐚 𝐢𝐧𝐝𝐡𝐚 𝐮𝐥𝐚𝐠𝐚𝐭𝐡𝐢𝐥 𝐨𝐬𝐚𝐧𝐝𝐡𝐚𝐝𝐡𝐮 𝐨𝐧𝐧𝐮𝐦 𝐢𝐥𝐥𝐚🙂** ",
           " **𝐮𝐧𝐧𝐚𝐧𝐚𝐤𝐮 𝐲𝐞𝐧 𝐦𝐞𝐥𝐚 𝐤𝐨𝐧𝐣𝐚𝐦 𝐤𝐮𝐝𝐚 𝐩𝐚𝐬𝐚𝐦𝐞 𝐢𝐥𝐥𝐚 𝐩𝐨𝐨🥲** ",
           " **𝐩𝐨𝐝𝐢 𝐬𝐢𝐥𝐥𝐮𝐤𝐤𝐮😅** ",
           " **𝐩𝐨𝐝𝐚 𝐬𝐢𝐥𝐮𝐤𝐤𝐮😍** ",
           " **𝐮𝐧𝐠𝐚𝐥𝐚 𝐩𝐚𝐭𝐡𝐚𝐭𝐡𝐚𝐝𝐡𝐮𝐥𝐚 𝐢𝐫𝐮𝐧𝐝𝐡𝐮 𝐧𝐚 𝐧𝐚𝐧𝐚𝐯𝐞 𝐢𝐥𝐥𝐚😅😅** ",
           " **𝐮𝐧𝐧𝐨𝐝𝐚 𝐥𝐨𝐯𝐞𝐫 𝐲𝐞𝐩𝐩𝐮𝐝𝐢 𝐢𝐫𝐮𝐤𝐤𝐚🤔** ",
           " **𝐡𝐞𝐲 𝐥𝐮𝐬𝐮🙄🙄** ",
           " **𝐡𝐞𝐲 𝐥𝐮𝐬𝐮😕** ",
           " **𝐩𝐚𝐭𝐡𝐮 𝐫𝐨𝐦𝐛𝐚𝐧𝐚𝐥 𝐚𝐜𝐡𝐢..??🙃** ",
           " **𝐮𝐧𝐧𝐚𝐤𝐤𝐞𝐧𝐚𝐩𝐚 𝐧𝐢 𝐚𝐳𝐡𝐚𝐠𝐮😛** ",
           " **𝐰𝐨𝐫𝐤 𝐥𝐚 𝐲𝐞𝐩𝐩𝐮𝐝𝐢 𝐩𝐨𝐝𝐡𝐮🤔** ",
           " **𝐦𝐫𝐠 𝐲𝐞𝐩𝐩𝐨🌟** ",
           " **𝐝𝐡𝐨𝐧𝐢 𝐚𝐝𝐢𝐜𝐡𝐚 𝐫𝐮𝐧𝐧𝐮 𝐚𝐳𝐡𝐚𝐠𝐚 𝐢𝐫𝐮𝐤𝐤𝐮 𝐮𝐧𝐧𝐨𝐝𝐚 𝐤𝐚𝐧𝐧𝐮👻🤗** ",
           " **𝐀𝐮𝐭𝐨 𝐨𝐝𝐮𝐦 𝐝𝐢𝐞𝐬𝐚𝐥 𝐥𝐚 𝐄𝐧 𝐡𝐞𝐚𝐫𝐭 𝐲𝐞 𝐚𝐧𝐮𝐩𝐚𝐯𝐚 𝐩𝐨𝐫𝐬𝐚𝐥 𝐥𝐚 🤭😇** ",
           " **110𝐤𝐠 𝐭𝐡𝐮𝐤𝐤𝐮𝐫𝐚 𝐢𝐧𝐝𝐡𝐚 𝐥𝐚𝐫𝐚𝐧𝐬𝐮𝐤𝐮 𝐮𝐧𝐧𝐚 𝐭𝐡𝐮𝐤𝐤𝐮𝐫𝐚𝐝𝐡𝐮 𝐩𝐞𝐫𝐮𝐬𝐮 𝐢𝐥𝐥𝐚 𝐤𝐚𝐧𝐧𝐚🤭** ",
           " **𝐧𝐢 𝐫𝐨𝐦𝐛𝐚 𝐧𝐚𝐥𝐥𝐚 𝐩𝐚𝐢𝐲𝐚𝐧𝐨🥺🥺** ",
           " **𝐧𝐢 𝐲𝐚𝐫𝐚 𝐥𝐨𝐯𝐞 𝐩𝐚𝐧𝐫𝐚😶** ",
           " **𝐄𝐧 𝐚𝐚𝐬𝐚 𝐫𝐨𝐬𝐚 𝐧𝐚𝐧 𝐭𝐡𝐚𝐧𝐞𝐲 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐫𝐚𝐚𝐬𝐚..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐍𝐞𝐞 𝐡𝐢𝐧𝐚𝐭𝐚 𝐦𝐚𝐫𝐢 𝐜𝐮𝐭𝐚 𝐢𝐫𝐮𝐤𝐤𝐚𝐚🙂** ",
           " **𝐌𝐚𝐧𝐚𝐬𝐮 𝐥𝐚 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐤𝐢𝐧𝐠 𝐧𝐮 𝐧𝐚𝐧𝐞𝐢𝐩𝐮😪** ",
           " **𝐓𝐡𝐚𝐦𝐛𝐢 𝐭𝐡𝐚𝐧𝐧𝐢 𝐤𝐞𝐚𝐧  𝐩𝐨𝐝𝐚 𝐯𝐚𝐧𝐭𝐡𝐢𝐲𝐚 𝐩𝐚 😂** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐚𝐭𝐭𝐢 𝐦𝐚𝐧𝐝𝐚 🙄 𝐦𝐚𝐫𝐢 𝐮𝐧 𝐦𝐨𝐨𝐜𝐡𝐢𝐢😺** ",
           " **𝐇𝐞𝐲 𝐧𝐞𝐞 𝐲𝐞𝐧 𝐢𝐩𝐝𝐢 𝐩𝐞𝐬𝐮𝐫𝐚 🥺🥺 𝐮𝐧𝐧𝐚 𝐞𝐧𝐚𝐤𝐤𝐮 𝐩𝐢𝐝𝐢𝐤𝐤𝐮𝐦 𝐝𝐚🥲** ",
           " **𝐃𝐚𝐢𝐢 𝐩𝐚𝐢𝐭𝐡𝐢𝐲𝐨 𝐢𝐫𝐮𝐤𝐤𝐢𝐲𝐚 𝐧𝐢😅** ",
           " **𝐢𝐩𝐩𝐨 𝐭𝐡𝐮𝐧𝐠𝐚 𝐩𝐨𝐫𝐢𝐲𝐚 𝐧𝐢😅** ",
           " **𝐥𝐢𝐟𝐞 𝐥𝐚 𝐲𝐞𝐩𝐩𝐮𝐝𝐢 𝐩𝐨𝐠𝐮𝐝𝐡𝐮 𝐛𝐫𝐨😆😆😆** ",
           " **𝐥𝐢𝐟𝐞 𝐥𝐚 𝐲𝐞𝐩𝐩𝐮𝐝𝐢 𝐩𝐨𝐠𝐮𝐝𝐡𝐮 𝐛𝐫𝐨😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐕𝐚𝐚 𝐦𝐚 𝐦𝐢𝐧𝐧𝐚𝐥𝐮  𝐧𝐚 𝐢𝐩𝐨 𝐦𝐨𝐫𝐚𝐭𝐭𝐮 𝐬𝐢𝐧𝐠𝐥𝐮  🤭🙂🙉** ",
           " **𝐃𝐚𝐢𝐢𝐢 𝐭𝐡𝐚𝐦𝐛𝐢𝐢𝐢  𝐮𝐧 𝐩𝐞𝐫𝐮 𝐞𝐧𝐧𝐚😹** ",
           " **𝐓𝐡𝐚𝐥𝐚 𝐯𝐚𝐥𝐢𝐤𝐤𝐮 𝐛𝐫𝐨 𝐧𝐚 𝐭𝐡𝐮𝐧𝐠𝐚 𝐩𝐨𝐫𝐚 𝐛𝐲𝐞𝐞😻** ",
           " **𝐬𝐫𝐲 𝐚𝐦𝐦𝐚 𝐯𝐚𝐧𝐭𝐡𝐮𝐭𝐚𝐧𝐠𝐚 𝐚𝐭𝐡𝐚𝐧 𝐨𝐝𝐢𝐭𝐞𝐧🙃** ",
           " **𝐀𝐤𝐤𝐚 𝐔𝐧𝐠𝐚𝐥𝐚 𝐚𝐧𝐭𝐡𝐚 𝐩𝐚𝐢𝐲𝐚𝐧 𝐤𝐮𝐩𝐝𝐫𝐚𝐧😕** ",
           " **𝐔𝐧𝐧𝐨𝐝𝐚 𝐋𝐨𝐯𝐞𝐫 𝐕𝐂 𝐊𝐮 𝐕𝐚𝐫𝐚 𝐒𝐨𝐥𝐫𝐚 𝐕𝐚🙃** ",
           " **𝐄𝐧𝐧𝐚 𝐩𝐚𝐧𝐝𝐫𝐚 𝐪𝐮𝐞𝐞𝐧 ✨🙃** ",
           " **𝐔𝐧𝐠𝐚 𝐢𝐧𝐭𝐫𝐨 𝐬𝐨𝐥𝐮𝐠𝐚 𝐛𝐫𝐨😊** ",
           " **𝐥𝐢𝐟𝐞 𝐥𝐚 𝐲𝐞𝐩𝐩𝐮𝐝𝐢 𝐩𝐨𝐠𝐮𝐝𝐡𝐮 𝐛𝐫𝐨🧐** ",
           " **𝐎𝐢𝐢 𝐒𝐞𝐥𝐟𝐢𝐞 🙊😌** ",
           " **𝐎𝐢𝐢 𝐌𝐚𝐩𝐥𝐚😠** ",
           " **𝐎𝐧𝐞 𝐯𝐬 𝐨𝐧𝐞 𝐬𝐚𝐧𝐝𝐚 𝐩𝐨𝐭𝐮𝐩𝐨𝐦 𝐯𝐚𝐝𝐚🥵** ",
           " **𝐘𝐞𝐧𝐧𝐚𝐤𝐮 𝐑𝐢𝐲𝐚𝐳 𝐌𝐚𝐭𝐭𝐮𝐝𝐡𝐚 𝐓𝐡𝐚𝐧𝐠𝐨𝐨𝐨 𝐏𝐮𝐫𝐢𝐧𝐣𝐢𝐤𝐤𝐨 𝐨𝐤 𝐯𝐚..🥰** ",
           " **𝐇𝐢𝐢 𝐌𝐚𝐝𝐚𝐦🤧❣️** ",
           " **𝐌𝐢𝐬𝐬 𝐲𝐨𝐮 🤧😏😏** ",
           " **𝐨𝐢𝐢 𝐌𝐞𝐨𝐰🤐** ",
           " **𝐔𝐧𝐧𝐨𝐝𝐚 𝐈𝐧𝐬𝐭𝐚 𝐈'𝐝 𝐊𝐮𝐝𝐮 𝐏𝐚 😒** ",
           " **𝐍𝐢𝐲𝐞 𝐎𝐫𝐮 𝐏𝐚𝐢𝐭𝐡𝐢𝐲𝐨😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐔𝐧𝐧𝐚 𝐒𝐚𝐧𝐝𝐚𝐤𝐮 𝐊𝐮𝐩𝐩𝐮𝐝𝐮𝐫𝐚 🙈** ",
           " **𝐔𝐧𝐧𝐨𝐝𝐚 𝐏𝐢𝐜 𝐀𝐧𝐮𝐩𝐮☹️** ",
           " **𝐍𝐢 𝐮𝐧𝐦𝐚𝐢𝐲𝐚 𝐈𝐫𝐮𝐧𝐝𝐡𝐚 𝐍𝐚 𝐔𝐧𝐧𝐚𝐤𝐮 𝐔𝐲𝐢𝐫𝐚 𝐊𝐮𝐝𝐚 𝐊𝐮𝐝𝐮𝐩𝐩𝐚 🥺🥺** ",
           " **யாரு விட்டு போனாலும் நம்ம இரண்டு பேரும் ஒன்னவோ இருப்போம்..❤️‍🩹🫂👀** ",
           " **எனக்கு எல்லாத்தையும் விட நீ தான் டா முக்கியம்.❤️‍🩹🫂😻** ",
           " **நண்பன முழுசா நம்புவோம் நாங்க எறங்கி அடிச்சா சம்பவம்..!!!🥵👻🫂** ",
           " **ஜாதி இல்லாத ஒரே உறவு நண்பன்..!!!❤️‍🩹✨💥** ",
           " **மச்சான்🫂💥✨** ",
           " **காலங்கள் பல கடந்தாலும் நம் நட்பு ஒரு போதும் மாறாது..!!!❣️❤️‍🩹💥** ",
           " **உன் கூட இருந்தா கொஞ்சம் நிம்மதியா இருக்கு மச்சா ⚡💛♥️** ",
           " **உன்ன விட்டா எனக்கு யாரு மச்சா இருக்கா என் உயிரே நீ தான மச்சா.🌟👀** ",
           " **ஊரோடு வந்து எதிர்த்தாலும் ஒரு மயிரும் புடுங்க முடியாது எங்கள்.. 🥵😼** ",
           " **𝐈 𝐚𝐦 𝐭𝐨𝐭𝐚𝐥𝐥𝐲 𝐚𝐝𝐝𝐢𝐜𝐭𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮😸** ",
           " **𝐈 𝐡𝐨𝐩𝐞 𝐭𝐡𝐢𝐬 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐛𝐨𝐧𝐝 𝐛𝐞𝐭𝐰𝐞𝐞𝐧 𝐮𝐬 𝐰𝐢𝐥𝐥 𝐧𝐞𝐯𝐞𝐫 𝐞𝐧𝐝.🙈** ",
           " **தொட்டுப் பார்க்கலாம் எட்டிப் பார்க்க முடியாது அது என்ன?✌️🤞** ",
           " **முறையின்றி தொட்டால் ஒட்டிக்கொண்டு உயிரை எடுப்பான் அவன் யார்?🥰** ",
           " **நடக்கவும் மாட்டான் நடக்கவும் மாட்டேன் நகராமல் இருக்கவும் மாட்டேன் நான் யார்?🥺🥺** ",
           " **பல அடுக்கு மாளிகையில் இனிப்பு விருந்து அது என்ன?** ",
           " **பேசுவான் நடக்க மாட்டான் பாடுவான் ஆட மாட்டான் அவன் யார்?😉** ",
           " **பெட்டி தலை இல்லாதவன் தலையை சுமப்பவன் அவன் யார்?😋🥳** ",
           " **காலடியில் சுருண்டு இருப்பாள் கண்ணீரென்று குரல் இசைப்பால் அவள் யார்?🧐** ",
           " **அந்தரத்தில் தொங்குவது சொம்பும் தண்ணீரும் அது என்ன?🥺** ",
           " **𝐈𝐯𝐚𝐧𝐠𝐚𝐝𝐡𝐚 :- [ @DipanshX ] 𝐘𝐞𝐧 𝐓𝐡𝐚𝐧𝐠𝐨𝐨𝐨 🤭🤭** ",
           " **காலையிலும் மாலையிலும் நெட்டை மதியம் குட்டை நான் யார்?😊** ",
           " **பட்டு பை நிறைய பவுன் காசு அது என்ன?🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐢𝐤𝐤𝐨 𝐦𝐚𝐜𝐡𝐚 :- [ @Team_144_Lovenes ]🤗** ",
           " **வினா இல்லாத ஒரு விடை அது என்ன😗😗** ",
           " **வேகாத வெயிலில் வெள்ளையப்பன் விளைகிறான் அது என்ன?🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @Yellow_144 ]🥰** ",
           " **ஆயிரம் பேர் அணிவகுத்தாலும் ஒரு தூசி கிளம்பாது அவை யாவை ?😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝗕𝗿𝗼 🥰** ",
           ]

@app.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")
