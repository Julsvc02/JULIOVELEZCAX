
import random

from pyfiglet import figlet_format
print(figlet_format("EL CLUB", font = "standard" ))

input()

print(' ')

J1 = "Desgarrador"
J2 = "Ninja"
J3 = "As"

print("Desgarrador:")
input()
print(
    'Es un  ucraniano asesino que busca vengar la muerte de su padre ante los rusos que lo asesinaron a sangre fria con la motosierra  de su padre. ')
input()

print("Usa un casco antidisturbios y un chaleco antibalas para cualquier percance.")


input()

print("Arma = Motosierra")
input()
print("Fuerza = 9")
print("Sigilo = 3")
print("Resistencia = 10")
print("Alcance = 2")
print("Velocidad = lenta")
print('')
input()
input()

print("Ninja:")
input()
print(
    'Es un ex militar de combate reclutado por Rusia y traído desde Japón,'
)
input()
print(" en realidad esta en allá para infligir daño a la nación rusa, arruinando sus planes con su katana.")
input()


print("Arma = Katana") 
input()
print("Fuerza = 8")
print("Sigilo = 10")
print("Resistencia = 5")
print("Alcance = 2")
print("Velocidad = rápido")
input()
input()

print("As:")
input()
print(
    'Es un ex espía ruso que fabrica sus propios trajes, fue traicionado por los rusos cuando trabajaba para ellos, '
)
input()
print("matando a su familia y revelando su identidad.")
input()

print("Arma = Francotirador silenciado")
input()

input()
print("Fuerza = 6")
print("Sigilo = 9")
print("Resistencia = 4")
print("Alcance = 10")
print("Velocidad = Medio")
input()
input()


print("MISION 1")
input()
print("El gobierno Ruso tiene información confidencial en la bóveda de un banco ya que el “protector” (un agente del gobierno ruso) tiene una bóveda en el banco más seguro del mundo.")
input()
print("""               ^
                _______     ^^^
               |xxxxxxx|  _^^^^^_
               |xxxxxxx| | [][]  |
            ______xxxxx| |[][][] |
           |++++++|xxxx| | [][][]|               
           |++++++|xxxx| |[][][] |
           |++++++|_________ [][]|
           |++++++|=|=|=|=|=| [] |
           |++++++|=|=|=|=|=|[][]|
___________|++HH++|  _HHHH__|   _________   _________  _________
         _______________   ______________      ______________
__________________  ___________    __________________    ____________""")

print('El objetivo de los personajes es robar esa información para derrocar a Rusia 🇷🇺.')
input()

print("La información contiene información militar y personal sobre el líder de Rusia, lo cual puede servir para extorsión o para derrocarlo.")
input()
input()
#while principal

while True:
    print("CHECKPOINT....")
    input()
    print("Elige un personaje para la mision:")
    J = input("-")
    print('')
    input()

    if (J == "Desgarrador"):
       print("Desgarrador llega en una camioneta (estilo van de atraco)") 
       input()
       print("Entra al banco sin pensarlo, inicia a hacer una masacre desde la puerta principal hasta encontrar al guardia de la bóveda y le mete una golpiza hasta que logra convencerlo de que le abra la bóveda.")
       input()
       print("Una vez que abren la bóveda, Desgarrador roba la información y asesina al guardia, ahora tiene que escapar.")
       input()

        
       AB =input("Quieres usar la salida principal (A) o la puerta de emergencia (B) ? ")
       input()
      
       if AB == "B":
        print("Sigues:")
        input()
        print("Desgarrador siguió vivo y robó el chip")
        break
         
       if AB == "A":
        input()
        print("Acabo el juego PERDISTE") 
        input()
        print("al salir se le habia informado a la guardia rusia del ataque y te mataron de un tiro de francotirador,(te estaban esperando por esa puerta).")  
        continue

      
    if (J == "Ninja"):
      
       print("Ninja llega caminando como una ciudadano común al banco,")
       input()
       print("por la ventana principal lanza granadas de humo y entra por ahí mismo,") 
       input()

       print(" como hay humo y nadie ve los guardias están confundidos y aterrados,")

       input()
       print("Ninja empieza a matar guardia por guardia (como está el humo nadie lo ve al mero estilo Batman), una vez todos los guardias están muertos,")
       input()
       print("Ninja entra a la bóveda sin problema")
       input()
       print("(al ser un ninja sabe como entrar y salir sin ser notado, ademas que tiene experiencia con las cajas fuertes de los bancos)")
       input()
       print(" y roba la información.")
       input()
       print("Se escapa por las sombra haciendo una pose típica de ninja.")
        

       AC = input("Quieres lanzar granadas de humo afuera del banco y salir por la puerta principal (A) o prefieres quedarte y esperar a que entren los militares y infiltrarte (B) ?")

      
       if AC == "B":
        print("Ninja sigue y se inflitra entre los soldados, los soldados piensan que te escapaste y vuelven a la base contigo.")
        break
        
        
       if AC == "A": 
         print("")
         print("Acabo el juego PERDISTE")
         input()
         print("Al salir se le habia informado a la guardia rusa del ataque y te mataron de un tiro de francotirador, te estaban esperando por esa puerta,")
         input()
         print("(Tu granada de humo se disipo en el aire.)") 
         input()
         continue

        
    if (J == "As"):
      
        print("As se colocó en un edificio cercano al banco ya que su arma es un francotirador,") 
        input()
        print("con el arma intento abatir al guardia de la puerta trasera")
        input()
      
        n=input("Choose: 1,2 or 3")

        if n=="1":
          print("With the gun he shot down the guard at the back door and impersonated him with his disguise ability,")
          input()
          print("being inside, he wanted to enter the vault directly but a guard saw him and started the shooting,")
          input()
          print("the problem is that As his gun is a sniper, so he did not last long and died.")
          continue
          

        elif n=="2":
          print("Ace misses the shot and is spotted, ")
          input()
          print("now the Russian guards are after him, trying to escape he requests a rescue helicopter, ")
          
          input()
          print("his team sends the helicopter to him but the Russian team intercepted Ace's call,")
          input()
          print("now the Russians called their nearby military bases to be on the lookout for the rescue helicopter and shoot it down in case they see it, ")
          input()
          print("Ace tries to escape doing parkour through the buildings trying to reach the escape point for the helicopter to rescue him while the Russians chase him, ")
          input()
          print("Ace manages to reach the escape point and is saved by the helicopter")
          break

          
        else:
          print("Ace misses the shot and is discovered, ")
          input()
          print("now the Russian guards go after him,")
          input()
          print(" Ace, realizing that he has been discovered decides to eliminate all the Russians, ")
          input()
          
          print("Ace manages to keep the combat for a while but his sniper is going to be his biggest problem,")
          input()

          print("after a few minutes the Russians get to As and assassinate him.")
          continue

          input()


print("END OF MISSION:")   
input()
print("Once escaping from the bank, the characters head to an airport where there is a plane waiting for them, ")
input()
print("In the inter between the bank and the airport there is a chase.")
input()

while True:
  print("CHECKPOINT....")
  input()
  print("Choose your character for the next mission (Desgarrador, Ninja, As):")
  H = input("-")
  print('')
  input()
  print("MISSION 2:")
  input()
  print("Place: Nuclear Bucke")
  input()
  
  print("""  ________  
      (( /========\
      __/__________\____________n_
  (( /              \_____________]
    /  =(*)=          \
    |_._._._._._._._._.|         !
(( / __________________ \       =o
  | OOOOOOOOOOOOOOOOOOO0 |   = """)
  
  input()
  print("On the plane the leader of the characters who is anonymous, (he never shows his face only his voice) ")
  input()
  print("Informs them that as a consequence of the coup they made in the bank... ")
  
  input()
  print("the Russian government is looking to launch nuclear missiles at Kiev. ")
  input()
  
  print("The leader orders them to go to the nuclear bucke and prevent the missiles from being launched.")
  
  if H=="Desgarrador":
    print("Desgarrador arrives to the place by parachuting (a few km from the bucke),")
    input()
    print("once on land, Desgarrador ambushes a guard who was patrolling the area and kills him with the chainsaw, ")
    input()
    print("the guard had a truck and with it Desgarrador goes directly to the main entrance of the bucke to ram the truck ")
    input()
    print("(the defenses of the bucke shoot Desgarrador making this an epic scene, this part of the ramming with the truck is a cinematic). ")
    input()
    print("Once inside, Desgarrador goes to where the main missile computer is, making a massacre in the process.")
    input()
    
    d=input("Do you want to Destroy the Bucke (A), Dismantle the Bucke (B) or Try to deactivate the Misil (C)?")

    if d=="A":
      print("Once Desgarrador Destroyes the bucke, the mission is over...")
      input()
      print("the Russians arrive at the place to take revenge on whoever did this to them, ")
      input()
      print("Desgarrador takes one of the Russians patrols and starts the chase, ")
      
      input()
      print("during the chase Desgarrador eliminated most of the Russians and the rest could not keep up with him. ")
      input()
      print("After that, Desgarrador heads to the escape point that was agreed upon in the plane in this case, a mountain.")
      break

    if d=="B":
      print("Once Desgarrador Dismantles  the bucke, the mission is over...")
      input()
      print("the Russians arrive at the place to take revenge on whoever did this to them, ")
      
      input()
      print("Desgarrador takes one of the Russians patrols and starts the chase, ")
      input()
      print("during the chase Desgarrador eliminated most of the Russians and the rest could not keep up with him. ")
      input()
      print("After that, Desgarrador heads to the escape point that was agreed upon in the plane in this case, a mountain.")
      break
    

    if d=="C":
      print("Once Desgarrador Tries to deactivate the bucke, the mission is over...")
      input()
      print("the Russians arrive at the place to take revenge on whoever did this to them, ")
      input()
      print("Desgarrador takes one of the Russians patrols and starts the chase, ")
      input()
      print("during the chase Desgarrador eliminated most of the Russians and the rest could not keep up with him. ")
      input()
      print("After that, Desgarrador heads to the escape point that was agreed upon in the plane in this case, a mountain.")
      break


  if H=="Ninja":
    print("Ninja jumps out of the plane towards the bucke, instead of using a parachute Ninja uses a gliding suit (squirrel style). ")
    input()
    print("He enters the base where the missile exits (top), but in turn the missile is fired. ")
    input()
    print("He is now in a race against time to prevent the missile from reaching Kiev. ")
    input()
    print("Once inside and without anyone seeing him, ")
    input()
    print("Ninja starts to make his way through the entire bucke killing everything in his path until he reaches the main computer (from where the missile was launched).")
    input()
    print("Once Ninja is in the computer he has three options:")
    input()
    b=input("Do you want to Destroy the Bucke (A), Dismantle the Bucke (B) or Try to deactivate the Misil (C)?")

    if b=="A":
      print("Ninja Destroyes the bucke and leaves away from it")
      input()
      
    elif b=="B":
      print("Ninja Dismantles the bucke, and then he leaves...")
      input()
      
    else:
      print("Ninja deactivates the misil and leaves from there")
      input()

    print("Once the mission is over, the Russians arrive at the place to take revenge on whoever did this to them, ")
    input()
    print("NInja knows that he will have to face them if he wants to escape, ")
    input()
    print("but he also knows that he doesn't have many chances because they are outnumbered. ")
    input()
    print("So ninja camouflages himself in the trees of the forest and starts taking down the enemies one by one stealthily ")
    input()
    arma = [1, 2, 3, 4]
    destino = random.choice(arma)
    r = destino
    
    if (r == 1):
      print("Ninja just knocks all Russians out")
      input()    
    elif(r== 2):
      print("Ninja eliminates all Russians with his Katana")
      input()

    elif (r== 3):
      print("Ninja eliminates all Russians with his Katana..")
      input()

    else:
      print("Ninja just knocks all Russians out")
      input()

    print("Finishing with the Russians ninja goes to the escape point that was agreed on the plane. ")
    break

  if H=="As":
    print("Ace arrives to the place by parachuting (looking for the highest part nearby),")
    input()
    print("already in the highest part Ace camouflages with the environment and stays waiting with his sniper. ")
    input()
    print("With that same sniper and his experience of camouflage.. ")
    input()
    print("Ace begins to eliminate all the defenses of the bucke.")
    input()
    print("Once the defenses are eliminated, Ace enters the bucke with one of the guards' rifles pretending to be one of them ")
    print("(he disguises himself as one of them), which allows him to get to the main computer without any problem. Since he is technically one of them (guards)")
    input()
    m=input("Do you want to Destroy the Bucke (A), Dismantle the Bucke (B) or Try to deactivate the Misil (C)?")

    if m=="A":
      print("Ace Destroyes the bucke and leaves away from it")
      input()
      
    elif m=="B":
      print("Ace Dismantles the bucke, and then he leaves...")
      input()
      
    else:
      print("Ace deactivates the misil and leaves from there")
      input()
    print("Once the mission is over, the Russians arrive on site to take revenge on whoever did this to them,")
    input()
    u=input("Choose 1 or 2:")
    if u=="1":
      print("Ace pretends to be a wounded guard and is put on a Russian patrol to transfer him to a base where he can be cured. ")
      input()
      print("On the way, Ace stabs them to death (surgical knife) and steals the patrol to go to the escape point that was agreed on the plane.")
      break

    
    if u=="2":
      print("Ace climbs a tree (camouflaged) and begins to eliminate the Russians with his sniper. ")
      input()
      print("Let us leave their fate in the hands of the universe.")
      input()
      fate = [1, 2]
      destino = random.choice(fate)
      r = destino

      if r==1:
        print("Ace is discovered and he dies")
        continue

      if r==2:
        print("Ace manages to shoot down most of them, but when he was about to die, a helicopter arrives to his rescue and saves him.")
        input()
        break


while True:
  print("CHECKPOINT")
  input()
  print("Choose your character for the next mission (Desgarrador, Ninja, As):")
 
  O = input("-")
  
  print("MISSION 3:")
  input()
  print("Place: Pekin, China")
  input()
  print("The characters know that they have just entered a situation against the clock, ")
  input()
  print("the attack on the bank and preventing the nuclear missile from reaching Kiev has greatly enraged the Russians who are now going to use their secret plan (it is the strongest), ")
  input()
  print("this secret plan is located in China (more specifically in Beijing).")
  input()
  print("Now the characters have to go to Beijing to dismantle the Russians' plan ")
  input()
  print("(the characters know about the plan thanks to the information they stole from the bank in the first mission).")
  input()

  x=input("Which vehicle would you like to have in this MIssion?")

  if O=="Desgarrador":
    print("Desgarrador's",x,"arrives in the nearest rural area of Beijin")
    input()
    print("to steal a motorcycle and go unnoticed. ")
    input()
    print("Once he enters the rural area, he starts looking for a motorcycle to get to Beijing")
    input()
    input()
    print("...")
    input()
    print("by hook or by crook.")
    input()

    break
    

  if O=="Ninja":
    print("Ninja's",x,"gets as close as he can to the nearest Russian military base ")
    input()
    print("so that Ninja can infiltrate and get into one of the vehicles on its way to Beijing .")
    input()
    input()
    print("undetected")
    input()

    break

  if O=="As":
    print("Ace's",x,"arrives in the rural area closest to Beijing ")
    input()
    print("for Ace to pose as a military man  ")
    input()
    print("so that he can infiltrate the Russian army and...")
    input()
    print("be escorted to Beijing by the Russians.")
    input()
    input()

    break

print("END OF THE GAME")
input()
print("If you liked the game please leave a like")
input()

u=input("Leave a like: YES/NO:")

if u=="YES":
  print("Thank you for liking our game!")
  input()
  print("Would you like a second part of this game?")
  input()
  ñ=input("YES/NO")

  if ñ=="YES":
    print("Thank you for your opinion :)")
    input()
    print("We will work on it")
    input()

  if ñ=="NO":
    print("Well, we could do it better I think")
    input()
    print("It was a project for school anyways")
    input()

elif ñ=="NO":
  print("Why?")
  input()
  print("Did you find any bugs or errors in our game?")
  e=input("YES/NO")

  if e=="YES":
    print("Sorry to hear that")
    input()
    print("We will work on fixing them")
    input()

  if e=="NO":
    print("Glad to hear that")
    input()
    print("Then why didnt you like the game?")
    input()
    print("Leave your recommendations here:")
    y=input("---------")

print("CREDITS:")
input()
print("Created by:")
input()
print("Juan Manuel Morales Molina")
input()
print("Pedro Solis Ortega")
input()
print("Gael Uribe Isla")
input()
print("Julio Alberto Velez Carranza")
input()