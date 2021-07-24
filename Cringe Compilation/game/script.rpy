define p = Character("@Prot__agonista")
define o = Character("O CARECA")
define g = Character("Guitarrista de guy")
define m = Character("M3s7r3 MuR1l0")
define s = Character("Senhor das Trevas")
define r = Character("Rainha do Gado")
define f = Character("E-GAROTA")
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

    p "Ta aki Rapha aaaaaaaa"

    o "Opora meu irmão"

    # This ends the game.

    return
