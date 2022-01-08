Solucions_08_01_2022 = "alpí altiplà ampit ampla ampli àmplia apa apaïsat àpat apatia api aplàsia aplatat aplita apta aspa aspat aspi atiplat impala impia lampassat lampista lapil·li lapsa lipasa llamp llampat llapa llapassa llapis llapissa malapta malpaís malplà mapa massapà matapà mississipià paia pai-pai país paisà pal pala palaí palaia palat palatal palatí palista pal·la palla pallassa pallat pal·li pàl·lia pal·lial pallissa palm palma palmàs palmat palmitat palp palpís pam pampa pap papà papa papaia papal papat papil·la papil·litis papista pas passa passamà passa-passa passat passi pàssim past pasta pastat pastilla pastim pastís patapam patata patí pati patilla pia pila pili pim-pam pipa pipí pis pisa pisà pispa pista pistil pistil·lat pit pita pitalassa pitam piti pítia pítima pla plapa plasma plat plata platí psalm psammita psi salispàs salispassa salpa salpàs salpassa sap sapa saplà simpatia simplista sipai sípia talp talpa tampa tap tapa tapall tapàs tapí tàpia tapís tapit tàpsia timpà tip tipa tipi mississipià papil·litis passa-passa pistil·lat salispassa"
Paraules_Encertades = []

ParaulesJugador1 = []
ParaulesJugador2 = []
ParaulesJugador3 = []
ParaulesJugador4 = []


def IntrodueixParaula(IdJugador,string):
    if string in Solucions_08_01_2022:
        if string not in Paraules_Encertades:
            Paraules_Encertades.append(string)

            if IdJugador == "Jugador1":
                ParaulesJugador1.append(string)
            if IdJugador == "Jugador2":
                ParaulesJugador2.append(string)
            if IdJugador == "Jugador3":
                ParaulesJugador3.append(string)
            if IdJugador == "Jugador4":
                ParaulesJugador4.append(string)

def PuntuacioFinal(ParaulesJugador1,ParaulesJugador2,ParaulesJugador3,ParaulesJugador4):
    PuntsJ1 = len(ParaulesJugador1)
    PuntsJ2 = len(ParaulesJugador2)
    PuntsJ3 = len(ParaulesJugador3)
    PuntsJ4 = len(ParaulesJugador4)

    print ("Jugaror1 =",PuntsJ1,"Jugaror2 =",PuntsJ2,"Jugaror3 =",PuntsJ3,"Jugaror4 =",PuntsJ4)
    if PuntsJ1 == max(PuntsJ1,PuntsJ2,PuntsJ3,PuntsJ4):
        print("Guanya Jugador1")
    if PuntsJ2 == max(PuntsJ1,PuntsJ2,PuntsJ3,PuntsJ4):
        print("Guanya Jugador2")
    if PuntsJ3 == max(PuntsJ1,PuntsJ2,PuntsJ3,PuntsJ4):
        print("Guanya Jugador3")
    if PuntsJ4 == max(PuntsJ1,PuntsJ2,PuntsJ3,PuntsJ4):
        print("Guanya Jugador4")


#El jugador nª4 i el nª3 escriuren la paraula "ampit". Com que el Jugador4 l'ha escrit primer els punts són per a ell i el nª3 no puntua.
#El jugador nª1 escriu la paraula "ensaimada". Com que no es una de les solucions no puntua.
IntrodueixParaula("Jugador4","ampit")
IntrodueixParaula("Jugador3","ampit")
IntrodueixParaula("Jugador1","ensaimada")

print (PuntuacioFinal(ParaulesJugador1,ParaulesJugador2,ParaulesJugador3,ParaulesJugador4))

