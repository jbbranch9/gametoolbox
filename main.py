import logging
from gametoolbox.board.board import Checkerboard
from gametoolbox.gui.demo_window import DemoWindow
from gametoolbox.games.tic_tac_toe import TicTacToeGame
from gametoolbox.gui.turn_indicator import TurnIndicator


def main():

    logging.basicConfig(level=logging.DEBUG)

    # DemoWindow(
    #     single_gui_object=TurnIndicator(font=()),
    # )

    # TicTacToeGame()

    demo = Checkerboard(color_palette="green-white")

    post_final = demo.get_post_finalization_array()

    DemoWindow(
        single_gui_object=demo.get_frame(),
        post_finalization_array=post_final,
    )


if __name__ == "__main__":
    main()
