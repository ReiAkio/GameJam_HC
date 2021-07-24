define p = character("@Prot__agonista")
define o = character("O CARECA")
define g = character("Guitarrista de guy")
define m = character("M3s7r3 MuR1l0")
define s = character("Senhor das Trevas")
define r = character("Rainha do GADO")
define f = character("E-GAROTA")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    a "Ta aki Rapha aaaaaaaaa"

    r "Opora meu irmão"

    # This ends the game.

    return
