
"""


Auteur: anonyme

Interface: microbit

Nom du projet: main

Description: Nom du projet

Toolbox: vittascience

Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="Q,kM[wuNSj%]m+J-nb/J">distance_seuil</variable><variable id="+|s!f?:vC$LBpVd84!IK">robot</variable><variable id="owEt6J,jOr!2pvt8YI9-">ultrason</variable><variable id="k4:fC0;O58tSIP)*y$WP">ligne_gauche</variable><variable id="jUu$AUT0=Yf~JSgy//AG">ligne_droite</variable><variable id="A(X%^A%.q8)vLa2M:h~T">centre_distance</variable></variables><block type="on_start" id="BB@gUAreuNX5QweBK^4l" x="10" y="10"><statement name="DO"><block type="text_comment" id=".YaB-nVmStnql*=sl.+n"><field name="TEXT"> Initialisation des modules nécessaires</field><next><block type="text_comment" id="U]#xe(.t9R`jA;F6}X12"><field name="TEXT"> Créer une instance du robot</field><next><block type="variables_set" id="#P]cwD_Z1`u57BaZ3Ucb"><field name="VAR" id="+|s!f?:vC$LBpVd84!IK">robot</field><value name="VALUE"><block type="call_expression_editable_return" id="bc{EQI6BR3k$nuNdt5q."><field name="NAME">Robot</field></block></value><next><block type="text_comment" id="{!o%{}O9Q`]x=!oP6*GC"><field name="TEXT"> Configuration des capteurs</field><next><block type="variables_set" id="sx6Zi8{#iI;E~kXB*{Zx"><field name="VAR" id="owEt6J,jOr!2pvt8YI9-">ultrason</field><value name="VALUE"><block type="call_expression_return" id=":K8vkfvmD}c?H84ksh%C"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="S!apSY0kocJ:};:)]X,u"><field name="NAME">ultrasonic_sensor</field></block></value></block></value><next><block type="variables_set" id="1Bhz|ykm.N~k+r{IH+%`"><field name="VAR" id="k4:fC0;O58tSIP)*y$WP">ligne_gauche</field><value name="VALUE"><block type="call_expression_return" id="(,-ewo08!A4]yt,9?lFT"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="J7wPQ,X1OQUvNGmY2q@E"><field name="NAME">line_sensor_left</field></block></value></block></value><next><block type="variables_set" id="nU[BflB.W;D98=~-Hv~r"><field name="VAR" id="jUu$AUT0=Yf~JSgy//AG">ligne_droite</field><value name="VALUE"><block type="call_expression_return" id="@YOZmZ$YV-$6d*-[#84Y"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="|/v|{G2~v)JlLL5]z)1^"><field name="NAME">line_sensor_right</field></block></value></block></value><next><block type="text_comment" id="92pXhMWvyF(SFC:0D+`8"><field name="TEXT"> Variables globales</field><next><block type="variables_set" id="R(#{qA148-J)]c`i4Z%W"><field name="VAR" id="Q,kM[wuNSj%]m+J-nb/J">distance_seuil</field><value name="VALUE"><block type="math_number" id="CJf{9`tEl!^/Lo2Dy-Dx"><field name="NUM">0.8</field></block></value><next><block type="text_comment" id="X1ML9~%k*G$Zz1y+hne!"><field name="TEXT"> Seuil de détection de 0,8 m</field><next><block type="variables_set" id="6IJ.5j=-0@#*2TDadp7x"><field name="VAR" id="A(X%^A%.q8)vLa2M:h~T">centre_distance</field><value name="VALUE"><block type="math_number" id="8zSE9njyHu8932utTLnd"><field name="NUM">0.4</field></block></value><next><block type="text_comment" id="/%mg/zcvPmEFCwmh*kgE"><field name="TEXT"> Distance pour revenir au centre</field><next><block type="text_comment" id="OX*-p6k,:sFO!$)R!E3Y"><field name="TEXT"> Boucle principale</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block><block type="procedures_defnoreturn" id="]~`#5c+3OLb_f0RO`AD[" x="10" y="10"><mutation name="tourner_sur_place"></mutation><field name="NAME">tourner_sur_place</field><statement name="STACK"><block type="call_expression" id=":?L63]bmmsLe9!5Ps)Ht"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="V,n/V$g1.o^W0KX`_.PA"><mutation items="2"></mutation><field name="NAME">set_motors_speed</field><value name="items0"><block type="math_number" id="K,m.ztU:#pP(,-}+KP$o"><field name="NUM">-50</field></block></value><value name="items1"><block type="math_number" id="q1h{A67e%Mrsr,Y#6w7G"><field name="NUM">50</field></block></value></block></value><next><block type="text_comment" id="{SDpt]kv_02:wg)W245]"><field name="TEXT"> Tourne sur lui-même (vitesse négative à gauche et positive à droite)</field></block></next></block></statement></block><block type="procedures_defnoreturn" id="7kA}$8Ycpw?^isuUKcyT" x="10" y="10"><mutation name="avancer"></mutation><field name="NAME">avancer</field><statement name="STACK"><block type="call_expression" id="nT7YZrNt@tRj@tMFTDQ|"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="Na)v+`xA=b(w]C-u_DkQ"><mutation items="2"></mutation><field name="NAME">set_motors_speed</field><value name="items0"><block type="math_number" id="N%bs6t+sHrAnMin1~+*P"><field name="NUM">50</field></block></value><value name="items1"><block type="math_number" id="c}lbRja3X=|H{GF;R*dR"><field name="NUM">50</field></block></value></block></value><next><block type="text_comment" id="!T;4S[4#R_aR?kxLMVpg"><field name="TEXT"> Avance droit (vitesse égale des deux moteurs)</field></block></next></block></statement></block><block type="procedures_defnoreturn" id="Wt,h=oKtwd;hE;kLG0;k" x="10" y="10"><mutation name="reculer"></mutation><field name="NAME">reculer</field><statement name="STACK"><block type="call_expression" id="PmroR+v26o62)[IZb(gM"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="jPgLTD+,Or{1cG-U80sB"><mutation items="2"></mutation><field name="NAME">set_motors_speed</field><value name="items0"><block type="math_number" id="KC%pwSBK(GzHh1wi+9R."><field name="NUM">-50</field></block></value><value name="items1"><block type="math_number" id="40yRu$_*cTc2]!6xU6?U"><field name="NUM">-50</field></block></value></block></value><next><block type="text_comment" id="%$v@]ukDI6bzzozDj=t="><field name="TEXT"> Recule (vitesse négative des deux moteurs)</field></block></next></block></statement></block><block type="procedures_defnoreturn" id="*X|4oQ^)MUH[`@D/I.$u" x="10" y="10"><mutation name="stop_robot"></mutation><field name="NAME">stop_robot</field><statement name="STACK"><block type="call_expression" id="f{gfS1WjS2z{:,PG`-0;"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="j;EI*rZP?R}PP^1hA#EM"><mutation items="2"></mutation><field name="NAME">set_motors_speed</field><value name="items0"><block type="math_number" id="^iZ4[xr%PXjl(|#uP2p#"><field name="NUM">0</field></block></value><value name="items1"><block type="math_number" id="W{Jgn/ECUxSD$n4ORUQ0"><field name="NUM">0</field></block></value></block></value><next><block type="text_comment" id="P!*E2_1C3^ne_}P,pPfG"><field name="TEXT"> Arrête les moteurs</field></block></next></block></statement></block><block type="procedures_defreturn" id=".qL0q,(s17^sa-+o!2;g" x="10" y="10"><mutation name="detecter_presence"></mutation><field name="NAME">detecter_presence</field><statement name="STACK"><block type="text_comment" id="qI1;dN13[3k4L*I~Q8?b"><field name="TEXT"> Retourne True si une présence est détectée à moins de 0,8 m</field></block></statement><value name="RETURN"><block type="logic_compare" id="NlF1vMd^P6PB+ZKyXC|!"><field name="OP">LTE</field><value name="A"><block type="call_expression_return" id="Q2NvHZc6OWzV:j@-JUFV"><field name="NAME">ultrason</field><value name="chain"><block type="call_expression_editable_return" id="f~aEI8/[T;P}(:F=%MN?"><field name="NAME">get_distance</field></block></value></block></value><value name="B"><block type="variables_get" id="R!:7K4p?^CrYjId1?uc4"><field name="VAR" id="Q,kM[wuNSj%]m+J-nb/J">distance_seuil</field></block></value></block></value></block><block type="procedures_defreturn" id="xy]9OksK|h`OlHrFOXs6" x="10" y="10"><mutation name="detecter_ligne"></mutation><field name="NAME">detecter_ligne</field><statement name="STACK"><block type="text_comment" id="g2f(RZ!z~FQ/o[vj~r|U"><field name="TEXT"> Retourne True si la ligne blanche est détectée</field></block></statement><value name="RETURN"><block type="logic_operation" id="pR%ik44Uh#HN2|V_-Vdw"><field name="OP">AND</field><value name="A"><block type="logic_negate" id="e(b9W}ldU!.dhu~stBiR"><value name="BOOL"><block type="call_expression_return" id="=cOfr*`D=YdzM.T.*~=l"><field name="NAME">ligne_gauche</field><value name="chain"><block type="call_expression_editable_return" id="olsImK#;=,b)zQ(7E-uJ"><field name="NAME">get_line_detected</field></block></value></block></value></block></value><value name="B"><block type="logic_negate" id="H}`ie*!v`u5|Y!)otVQy"><value name="BOOL"><block type="call_expression_return" id="a1=er_ft@~s{Wv5L3GM9"><field name="NAME">ligne_droite</field><value name="chain"><block type="call_expression_editable_return" id="o[}gjm,D]etZU:3AzcWm"><field name="NAME">get_line_detected</field></block></value></block></value></block></value></block></value></block><block type="forever" id="M;L@|c??7BeJRhT4d~,R" x="10" y="10"><statement name="DO"><block type="procedures_callnoreturn" id="}iAW+F]!e~u`6diLiIa/"><mutation name="tourner_sur_place"></mutation><next><block type="controls_if" id="f*{|9}o1=i@CGaW,=@b4"><value name="IF0"><block type="procedures_callreturn" id="xA)#+%8OcEIO=HBU8!~h"><mutation name="detecter_presence"></mutation></block></value><statement name="DO0"><block type="procedures_callnoreturn" id="hk!wT})dYd(l+l!4MOfu"><mutation name="stop_robot"></mutation><next><block type="procedures_callnoreturn" id="%C[+2Z+i=?!r?*_r)q`="><mutation name="avancer"></mutation><next><block type="controls_whileUntil" id="!INX3QEtm[DKP.jP0uyq"><field name="MODE">WHILE</field><value name="BOOL"><block type="procedures_callreturn" id="a]R+xP#+64~S*E_t]Y:!"><mutation name="detecter_presence"></mutation></block></value><statement name="DO"><block type="call_expression" id="|wA^SrzVcX/*9pZs+%dI"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id="B`yN?JvCa`EtoErq.5F?"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_number" id="w-;onFM4h:(6(]T;lQAE"><field name="NUM">0.1</field></block></value></block></value><next><block type="text_comment" id="~#2^D~1*E8le^nFp:bu}"><field name="TEXT"> Continue d'avancer tant que la présence est détectée</field></block></next></block></statement></block></next></block></next></block></statement><next><block type="controls_if" id="[Hl+d)iM`p3B5/}bg8[j"><value name="IF0"><block type="procedures_callreturn" id="4d:[dnn!SJU,N}TbLcVs"><mutation name="detecter_ligne"></mutation></block></value><statement name="DO0"><block type="procedures_callnoreturn" id="ulhnc~W#|EIo7?KKl[.o"><mutation name="stop_robot"></mutation><next><block type="call_expression" id="CTDpM}%IE2YcjE%C6L;g"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id="NJX4%L[$Zh=Y}nFJ/3Y^"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_number" id="zC=d=c]W|Z!7`}:)m^9["><field name="NUM">0.5</field></block></value></block></value><next><block type="text_comment" id="WtiPPH)Kw)]2mPiHz]:_"><field name="TEXT"> Pause pour stabiliser</field><next><block type="call_expression" id="XdQ.vu6l^EX=HfW`0=r0"><field name="NAME">robot</field><value name="chain"><block type="call_expression_editable_return" id="@pSNe5$=,m|+B#/nC:}L"><mutation items="2"></mutation><field name="NAME">set_motors_speed</field><value name="items0"><block type="math_number" id="zw34$XsN]TPXDdv{boGb"><field name="NUM">-50</field></block></value><value name="items1"><block type="math_number" id="`brtz!XxJPWJVx1^3Qk%"><field name="NUM">50</field></block></value></block></value><next><block type="text_comment" id=";iBF,7~uB+PW_K@Z+[a}"><field name="TEXT"> Tourne à 180° (ajuster si nécessaire)</field><next><block type="call_expression" id="ig]E;(JVbY_U/?-=fI[!"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id="l)%9d!4iL%pJrV7:e:1W"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_number" id="r[X9sdRZ{v}/lkmtn]Xt"><field name="NUM">1.8</field></block></value></block></value><next><block type="text_comment" id="V4$w(68emRjdW.H]M8S3"><field name="TEXT"> Durée approximative pour effectuer un demi-tour</field><next><block type="procedures_callnoreturn" id="/;]d5GS9GdjibB9?|hT^"><mutation name="stop_robot"></mutation><next><block type="procedures_callnoreturn" id="jzG;wWxU1p(`;p2c~v%X"><mutation name="avancer"></mutation><next><block type="call_expression" id="g59oNdRO{#P`/`YX+K#J"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id=";!nIS}3nw?UhlcRly*LN"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_arithmetic" id="mSTvu?`R5W:chyP[l+[("><field name="OP">DIVIDE</field><value name="A"><block type="variables_get" id="M?z(};#0m~,17XQlKeZA"><field name="VAR" id="A(X%^A%.q8)vLa2M:h~T">centre_distance</field></block></value><value name="B"><block type="math_number" id="m8b:=`qY07GX[.-66YHj"><field name="NUM">0.05</field></block></value></block></value></block></value><next><block type="text_comment" id="h2gnwiYDZ,sANmMYT913"><field name="TEXT"> Avance de 0,4 m à une vitesse constante de 50 (ajuster si nécessaire)</field><next><block type="procedures_callnoreturn" id="!@Hp%9:BX_*d8|J}o5xe"><mutation name="stop_robot"></mutation></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement><next><block type="call_expression" id="*orEdaiYJ83dGK@fgwv/"><field name="NAME">time</field><value name="chain"><block type="call_expression_editable_return" id="Gsjwl[8P6f#-hMm%@CMh"><mutation items="1"></mutation><field name="NAME">sleep</field><value name="items0"><block type="math_number" id="627!Iqe)%Zo^2]AW0=T8"><field name="NUM">0.05</field></block></value></block></value><next><block type="text_comment" id="!$@AI5x5~dOgFy]xOaU0"><field name="TEXT"> Pause pour éviter une surcharge du processeur</field></block></next></block></next></block></next></block></next></block></statement></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *

def tourner_sur_place():
  robot.set_motors_speed(-50, 50)
  # Tourne sur lui-même (vitesse négative à gauche et positive à droite)

def avancer():
  robot.set_motors_speed(50, 50)
  # Avance droit (vitesse égale des deux moteurs)

def reculer():
  robot.set_motors_speed(-50, -50)
  # Recule (vitesse négative des deux moteurs)

def stop_robot():
  robot.set_motors_speed(0, 0)
  # Arrête les moteurs

def detecter_presence():
  # Retourne True si une présence est détectée à moins de 0,8 m
  return ultrason.get_distance() <= distance_seuil

def detecter_ligne():
  # Retourne True si la ligne blanche est détectée
  return not ligne_gauche.get_line_detected() and not ligne_droite.get_line_detected()

# Initialisation des modules nécessaires
# Créer une instance du robot
robot = Robot()
# Configuration des capteurs
ultrason = robot.ultrasonic_sensor()
ligne_gauche = robot.line_sensor_left()
ligne_droite = robot.line_sensor_right()
# Variables globales
distance_seuil = 0.8
# Seuil de détection de 0,8 m
centre_distance = 0.4
# Distance pour revenir au centre
# Boucle principale

while True:
  tourner_sur_place()
  if detecter_presence():
    stop_robot()
    avancer()
    while detecter_presence():
      time.sleep(0.1)
      # Continue d'avancer tant que la présence est détectée
  if detecter_ligne():
    stop_robot()
    time.sleep(0.5)
    # Pause pour stabiliser
    robot.set_motors_speed(-50, 50)
    # Tourne à 180° (ajuster si nécessaire)
    time.sleep(1.8)
    # Durée approximative pour effectuer un demi-tour
    stop_robot()
    avancer()
    time.sleep(centre_distance / 0.05)
    # Avance de 0,4 m à une vitesse constante de 50 (ajuster si nécessaire)
    stop_robot()
  time.sleep(0.05)
  # Pause pour éviter une surcharge du processeur
