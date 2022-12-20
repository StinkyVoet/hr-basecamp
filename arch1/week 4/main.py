from contextlib import suppress
import os
from threading import Thread
from playsound import playsound
import tlib 

def main():
    # Start music on seperate thread
    Thread(target=musicLoop, name='BackgroundMusicThread', daemon=True).start()

    # Intro
    tlib.update_screen(
        "Welcome to \033[1m\033[96mTo the Top\033[0m\n"
        "\n"
        "You find yourself in a basecamp at the foot of the mountain. You only know your purpose is to climb.\n"
        "Can you make it \033[1m\033[96mto the top\033[0m?"
    )
    # print()
    # print("You find yourself in a basecamp at the foot of the mountain. You only know your purpose is to climb.")
    # print("Can you make it \033[1m\033[96mto the top\033[0m?")

    # Setup
    player = tlib.Player.new()
    command: tlib.Command
    output: str
    world = tlib.World.new()

    print()
    print("Your starting stats:")
    print(player.show_stats())

    with suppress(KeyboardInterrupt):
        while True:
            command = tlib.get_input()
            output = world.update_state(command, player)
            tlib.update_screen(output)
            
            if command.__class__ == tlib.Command.Exit:
                tlib.exit()


            """TODO: MOVE CHECKS TO LIB"""
            # if player.stats["height"].value >= player.stats["height"].max:
            #     print("\nYou have reached the top of the mountain!")
            #     break;
            # if player.stats["food"].value == 0:
            #     lost_health = randrange(30,60)
            #     player.stats["health"].value -= lost_health
            #     print("You're starving. You lost %d health" % (lost_health))
            # if player.stats["health"].value <= 0:
            #     print("\nYou died! :(")
            #     break;

def musicLoop():
    while True:
        playsound('media/background_music.mp3')


if __name__ == "__main__":
    os.system('clear')

    main()
