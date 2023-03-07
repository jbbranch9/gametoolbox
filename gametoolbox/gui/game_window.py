"""
This is the parent class for all game windows.

"""

import logging
from PySimpleGUI import Window, WIN_CLOSED


def exit_events():
    return WIN_CLOSED, 'Exit', 'exit', 'EXIT', 'Escape:27', 'F5:116'


def restart_events():
    return 'Restart', 'restart', 'RESTART', 'F2:113'


# these parameters are passed to the parent class __init__ method,
# override with game-specific params as needed
def default_window_parameters():
    return {
        'title': '',
        'layout': [[]],
        'return_keyboard_events': True,
        'no_titlebar': False,
        'grab_anywhere': True,
        'finalize': True,
        'resizable': True,
    }


class GameWindow(Window):
    __EXIT_EVENTS = exit_events()
    __RESTART_EVENTS = restart_events()

    _default_parameters = default_window_parameters()


    
    def __init__(self, **kwargs):
        
        if kwargs:
            window_parameter_kwargs = kwargs
        else:
            window_parameter_kwargs = self._default_parameters

        super().__init__(
            **window_parameter_kwargs
            )

        self.finalize()
        
        self.__window_event_loop()

    # DO NOT overload '__window_event_loop'
    # For gameplay loops, use 'game_event_loop' instead,
    # which is called once per '__window_event_loop' cycle.
    def __window_event_loop(self):
        repeat_loop = True
        while repeat_loop:
            event, values = self.read()
            logging.info(str(event))
            logging.info(str(values))
            
            if event in GameWindow.__EXIT_EVENTS: 
                break 
            
            if event in GameWindow.__RESTART_EVENTS:
                self.__restart()
                break

            # calling 'game_event_loop' returns a bool, which indicates whether
            # '__window_event_loop' should repeat after this loop
            repeat_loop = self.game_event_loop(event, values)


        self.close()  # This is a redundant failsafe to ensure the window closes.

    """
    Overload this method for each game's specific loop(s).
    All overloads of this method MUST return a bool called 'repeat_loop', 
        and SHOULD also assign repeat_loop to True at the top of each loop.
    """
    def game_event_loop(self, event, values) -> bool:
        repeat_loop = True
        return repeat_loop
    
    def __restart(self):
        self.close()
        return GameWindow()

    def get_default_parameters(self):
        return dict(self._default_parameters)
        

def main():
    demo = GameWindow()
    return demo


if __name__ == "__main__":
    main()
    print('done')
