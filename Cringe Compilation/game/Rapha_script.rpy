# Personagens
define p = Character("@Prot__agonista")
define o = Character("O CARECA")
define g = Character("Guitarrista de guy")
define m = Character("M3s7r3 MuR1l0")
define s = Character("Senhor das Trevas")
define r = Character("Rainha do Gado")
define f = Character("E-GAROTA")
define n = Character("Narrador")

# Imagens
image image_bg = "images/Background.png"
image image_p = "images/MainCharacter.png"
image image_m = "images/Murilo.png"

# Variáveis globais
define pontosCringe = 0

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

    # These display lines of dialogue.

    n "Nosso protagonista estava muito empolgado para o seu primeiro dia de trabalho como terapeuta."
    n "Toc... toc..."
    n "Seu primeiro cliente havia chegado!"

    menu:
        "Bom dia!":
            m "..."
        "Tranquilo como esquilo?":
            m "R3sp31T3 o S3u M3s7r3"
            $pontosCringe += 1
        "...":
            m "B0m d14!"
    menu:
        "Bem, como foi o seu dia senhor?":
            m "M3s7r3..."
        "Bem, como foi o seu dia mestre?":
            m "M3s7r3..."
        "Bem, como foi o seu dia M3s7r3?":
            m "..."

    m "B3m, 3st0u c0m um pr0bL3m4!"
    n "Oque aconteceu?"
    m "T0d0s diz3m qu3 m3u m0d0 d3 f4lAR é CR1NG3..."
    m "3u n4o S31 o qu3 f4z3r..."

    menu:
        "O que é cringe?":
            m "S3u b00m3r p0dr3, v0c3 s3 f0rMOU A0nd3 m3sm0?"
            n "Você está 1 ponto mais cringe"
            $pontosCringe += 1
        "Você deveria tentar mudar seus hábitos no seu ritmo.":
            m "C0m0?"
            p "Você poderia tentar diminuir a sua aparência c001, reduzindo a quantidade de números nas suas frases."
        "Mas quem fala cringe que é realmente cringe.":
            m "M4s v0c3 f4l0u CR1NG3 s3u B00m3R"
            n "Você está 1 ponto mais cringe"
            $pontosCringe += 1



    # This ends the game.

    return
