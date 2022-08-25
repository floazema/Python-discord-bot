from random import *

boss ={
    "                                              ,--,  ,.-.\n\
                ,                   \,       '-,-`,'-.' | ._\n\
               /|           \    ,   |\         }  )/  / `-,',\n\
               [ '          |\  /|   | |        /  \|  |/`  ,`\n\
               | |       ,.`  `,` `, | |  _,...(   (      _',\n\
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\\\n\
                \  \_\,``,   ` , ,  /  |         )         _,/\n\
                 \  '  `  ,_ _`_,-,<._.<        /         /\n\
                  ', `>.,`  `  `   ,., |_      |         /\n\
                    \/`  `,   `   ,`  | /__,.-`    _,   `\\\n\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \                                           {hp}\n\
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |\n\
                ,` )  | \_\       '-`  |  `(               \\\n\
               /  /```(   , --, ,' \   |`<`    ,            |\n\
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)\n\
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`\n\
       (-, \           ) \ ('_.-._)/ /,`    /\n\
       | /  `          `/ \\ V   V, /`     /\n\
    ,--\(        ,     <_/`\\     ||      /\n\
   (   ,``-     \/|         \-A.A-`|     /\n\
  ,>,_ )_,..(    )\          -,,_-`  _--`\n\
 (_ \|`   _,/_  /  \_            ,--`\n\
  \( `   <.,../`     `-.._   _,-`\n\
   `                      ```\n\
"
},
{

}

level = 1
hp = level * 1000 + randint(1, 1000)
numbers = []
operator = []
while(1):
    print("Level:",level)
    print(boss[0])
    operator = randint(1, 10)
    for i in range (int(level / 10 + 1)):
        if (level %10 >= 0 and level %10 <= 3):
            randint(700)
        if (level %10 >= 4 and level %10 <= 6):
            randint(5000)
        if (level %10 >= 4 and level %10 <= 6):
            randint(10000)
        numbers[i] = randint(1, 9)
    calcul = randint()
    input(calcul, "=")
    if (hp == 0):
        level += 1
        hp = level * 1000 + randint(1, 1000)