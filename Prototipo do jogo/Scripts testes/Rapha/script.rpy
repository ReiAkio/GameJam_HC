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

    # Questionamentos

    menu:
        "Você poderia me falar mais sobre esses métodos que você tentou?":
            m "B3m, um d3l3s f01 ut1l1z4r 4qu3l3s s1t3s d3 t3st3 d3 d1g1t4c4o..."
            m "3u p3ns31 qu3 c0m0 3ss3s s1t3s 3st40 n0rm41s 3u p0d3r14 m3 f0rç4r 4 f1c4r n0rm4l t4mb3m."
            m "P0r3m 3u f1qu31 c0m p0ntu4c40 nul4 3m t0d0s 0s t3st3s, 3 4p4r3nt3m3nt3 3u n40 m3lh0r31 n4d4..."
            menu:
                "Nossa você é horrível cara...":
                    $pontosCringe += 1
                    m "..."
                    m "V0c3 t3m 4lgum4 sug3st40?"
                "Você tentou mais algum método?":
                    m "3u... t4mb3m t3nt31 p4r4r d3 c0nsum1r 0br4s sh0un3n m4s..."
                    m "N40 qu3r0 m41s f4l4r s0br3 3st3 m3t0d0..."
                    n "Você se identifica pelo seu cliente e fica triste por um instante..."
                    m "C0m0 3u p0ss0 m3lh0r4r?"
        "Se os métodos não funcionaram, você nunca vai melhorar então.":
            m "B3m j4 qu3 v0c3 3st4 4ssum1nd0 qu3 3 um 1nc0mp3t3nt3 4cr3d1t0 qu3 4c4b4m0s p0r 4qu1, n40?"
            menu:
                "Sim, já vai tarde seu cringe":
                    m "4d3us..."
                    $pontosCringe += 1
                    n "O seu primeiro cliente saiu insatisfeito..."
                    n "Talvez você deva reconsiderar seu look para... atrair mais clientes?"
                    jump exit_mestreMurilo
                "Não, eu quero dizer que os métodos não irão te ajudar mais, mas eu posso pensar em algo..."
                    m "4gr4d3ç0, 3nt40... c0m0 3u p0ss0 m3lh0r4r?"

    # Sugestões

    p "Você poderia tentar entrar em contato com um fonoaudiólogo":
    m "S1m, m1nh4 m43 f01 4 pr1m31r4 4 sug3r1r 1ss0..."
    n "O seu cliente suspira desmotivado..."
    m "P0r3m n40 func10n0u...."
    "Sendo assim, você poderia tentar recitar certas partes de um livro sem ouvir sua própria voz."
    m "3ss3 m3t0d0 s0 func10n4 3m f1lm3s..."
    m "S1m, 3u j4 t3nt31..."
    p "Que você tentar um teste de recitar palavras?"
    m "p0d3 s3r."
    p "Tente recitar..."
    menu:
        "Urubu":
            m "Urubu"
            p "Isso! Você falou certo, vamos tentar mais uma vez..."
            menu:
                "Um":
                    m "Um"
                    p "Execelente, eu não vejo problemas aqui, agora tente falar normalmente!"
                    m "Hmmm eu não sei se..."
                    m "FUNCIONOUUUUU!"
                    m "EU ESTOU CURADOOO, MUITO OBRIGADO DOUTOR!"
                    n "A alegria estampada no rosto de seu cliente é contagiante, você sorri."
                    p "Bem, acredito que terminamos por aqui então senhor!"
                    m "M3s7r3!"
                    p "M3s7r3? Você pode dizer outra coisa?"
                    m "3... 3u n40 s31 0qu3 4c0nt3c3u..."
                "Sacola":
                    m "S4c0l4"
                    p "Hm..."
                    $pontosCringe += 1
                "Pudim":
                    m "Pud1m"
                    p "Entendo..."
                    $pontosCringe += 1
        "Abelha":
            m "4b3lh4..."
            p "Bem..."
            $pontosCringe += 1
        "Panqueca":
            m "P4nqu3c4"
            p "Saudades disso..."
            $pontosCringe += 1

    # Reação final

    p "Bem... irei pensar em uma solução temporária baseada no seu comportamento recente...."
    n "E assim o tempo da consulta foi sendo consumido como gotas enchendo um balde..."
    n "Após um tempo muito longo para ser expresso em palavras..."
    n "Mas para ter uma ideia foi algo em torno de 15 minutos e 7 segundos..."
    n "Finalmente você bolou uma solução temporária!"

    # Conclusões

    p "Eu acredito que se você se limitar a proferir apenas..."
    p "Palavras com exclusivamente a vogal 'u', você se sentirá normal e talvez venha a falar normalmente..."
    m "Hm.... um... pc... ubuntu..."
    m "Ubuntu...."
    n "Pensamentos sobre Linux invadiram a mente do seu cliente..."
    m "N444400000...."
    m "B3m... 0br1g4d0 d0ut0r"

    # Despedida

    menu:
        "Volte sempre M3s7r3!":
            m "1r3i m3u 4pr3nd1z..."
        "Até mais senhor!":
            m "N40 v0lt4r31..."

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