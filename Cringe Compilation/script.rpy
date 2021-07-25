# Personagens
define p = Character("@Prot__agonista")
define c = Character("O CARECA the guy")
define m = Character("M3s7r3 MuR1l0")
define e = Character("E-GAROTA")
define n = Character("Narrador")

# Imagens
image image_bg = "images/Background.png"
image image_p = "images/MainCharacter.png"
image image_m = "images/Murilo.png"
image image_e = "images/E-GAROTA.png"

# Variáveis globais
define pontosCringe = 0
define minimoDePontosCringe = 4

# Início do jogo
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene image_bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show image_m
    show image_e at left

    # Narrador no início do jogo.

    n "Nosso protagonista estava muito empolgado para o seu primeiro dia de trabalho como terapeuta."
    n "Toc... toc..."
    n "Seu primeiro cliente havia chegado!"

    # Fases de diálogo.

    jump mestreMurilo
    label exit_mestreMurilo:
    jump eGarota
    label exit_eGarota:
    jump oCarecaTheGuy
    label exit_oCarecaTheGuy:

    # Seleção do final, mudar o minimo de pontos cringe na linha 15 para ajustes.

    if pontosCringe >= minimoDePontosCringe:
        jump finalCringe
    else:
        jump finalNorm

    n "Sem final"

    # Fim do jogo.
    return

label mestreMurilo:
    # Escreva a fase aqui
    jump exit_mestreMurilo

label eGarota:
    # Escreva a fase aqui
    jump exit_eGarota

label oCarecaTheGuy:
    # Escreva a fase aqui
    jump exit_oCarecaTheGuy

label finalCringe:
    # Escreva a fase aqui
    return

label finalNorm:
    # Escreva a fase aqui
    return
