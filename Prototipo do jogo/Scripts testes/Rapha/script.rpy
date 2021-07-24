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
    # Início da fase do mestre murilo
    # Recepção

    n "Pela porta entrava uma figura um tanto estranha..."
    n "Você não sabia ao certo como reagir, mas precisava dar continuidade na consulta."

    menu:
        "Bom dia senhor!":
            m "3 M3s7r3 p4R4 v0C3, s3u b00m3r!"
        "...":
            m "B0m d14! P0r f4v0r m3 ch4m3 d3 M3s7r3..."
        "Nossa que cara de acabado, qual seu problema seu cringe?":
            m "D3p01s 1r3i c0nt4t4r m3u 4dv0g4d0 s3u 0T4R10, p0d3m0s pr0ss3gu1r?"
            $pontosCringe += 1
            p "Me desculpe senhor, sim..."
            m "M3 ch4m3 d3 M3s7r3, s3u b00m3r!"

    # Motivo da visita

    menu:
        "Bem, qual o motivo da sua visita?":
            m "... M3s7r3!"
            menu:
                "...":
                    m "C3rt0, 4p3s4r d4 su4 f4lt4 d3 r3sp31t0, 1r31 3xpl1c4r m3us pr0bl3m4s..."
                "M3s7r3, qual o motivo da sua visita?":
                    m "0bR1g4d0, b3m... 1r3i 3xpl1c4r m3us pr0bl3m4s..."
        "Pra que raios você veio aqui?":
            n "O cliente para por um instante se perguntando realmente se ele deveria ir embora..."
            n "Porém ele se lembra de uma vez que ele se confessou para uma amiga..."
            n "Em um shopping..."
            n "Lotado..."
            n "Durante o dia dos namorados..."
            n "Com uma caixa de som e um microfone..."
            n "E apesar das vaias e flores no lixo em sua memória..."
            n "Ele finalmente se recorda que tem problemas a tratar."
            m "1nf3l1zm3nt3 1r3i 3xpl1c4r m3us pr0bl3m4s, tr4t3 d3 s3r um pr0f1ss10n4l d3c3nt3..."
        "Diga M3s7r3, a que devo a honra?":
            m "0bR1g4d0, 1r3i 3xpl1c4r m3us pr0bl3m4s..."

    m "Pr1m31r4m3nt3 4s p3ss04s d1z3m qu3 0 m3u j31t0 d3 f4l4r é cr1ng3..."
    m "3u t3nt31 v4r10s m3t0d0s 3 s3nt1 ap3n4s um4 p3qu3n4 r3duç4o n4 m1nh4 m4n1a..."
    m "3x1st3 4lg0 qu3 3u p0ss0 f4z3r?"

    menu:
        ""

    # Questionamentos
    # Discussões
    # Sugestões
    # Reação final
    # Conclusões
    # Despedida

    # Fim da fase
    jump exit_mestreMurilo

label eGarota:
    # Início da fase da e-garota



    # Fim da fase
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
