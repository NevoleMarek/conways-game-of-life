import curses
import time
from typing import Any, List
from copy import deepcopy
from patterns import PATTERNS

ALIVE = 1
DEAD = 0

DEBUG = 0

class GameOfLife:

    def __init__(self, screen: Any) -> None:
        self.scr = screen
        self.size = (20,80)
        self._reset_board()

    def run(self, render:bool=False) -> None:
        while True:
            if not self._choose_pattern():
                break
            self.scr.nodelay(1)
            self.scr.addstr(self.size[0]+2, 0, f'[q] Stop')
            while True:
                if render:
                    self._render_board()
                self._simulate()
                time.sleep(0.0166)
                ch = self.scr.getch()
                self.scr.refresh()
                if ch == ord('q'):
                    self.scr.addstr(self.size[0]+2, 0, f'Stopped')
                    break
            self.scr.nodelay(0)
            self.scr.addstr(self.size[0]+2, 0, f'[q] Exit [any] New')
            ch = self.scr.getch()
            self.scr.refresh()
            if ch == ord('q'):
                break
            self.scr.addstr(self.size[0]+2, 0, f'{" ":<{self.size[1]}}')

    def _reset_board(self) -> None:
        self.board = [[0 for _ in range(self.size[1])] for _ in range(self.size[0])]

    def _simulate(self) -> None:
        new_board = deepcopy(self.board)
        for y, line in enumerate(self.board):
            for x, cell in enumerate(line):
                live = (
                    self.board[(y-1)%self.size[0]][(x-1)%self.size[1]]
                    + self.board[(y-1)%self.size[0]][(x)%self.size[1]]
                    + self.board[(y-1)%self.size[0]][(x+1)%self.size[1]]
                    + self.board[(y)%self.size[0]][(x-1)%self.size[1]]
                    + self.board[(y)%self.size[0]][(x+1)%self.size[1]]
                    + self.board[(y+1)%self.size[0]][(x-1)%self.size[1]]
                    + self.board[(y+1)%self.size[0]][(x)%self.size[1]]
                    + self.board[(y+1)%self.size[0]][(x+1)%self.size[1]]
                )
                if cell == ALIVE:
                    if live < 4 and live > 1:
                        new_board[y][x] = ALIVE
                    else:
                        new_board[y][x] = DEAD
                else:
                    if live == 3:
                        new_board[y][x] = ALIVE

                if DEBUG:
                    self.scr.addstr(y+1, x+1, f'{"x" if self.board[y][x] else "-"}')
                    self.scr.addstr(self.size[0]+3, 0, f'Cell: {y} {x} Status: {"Alive" if cell else "Dead "} Live: {live}')
                    self.scr.addstr(self.size[0]+4, 0, f'Status in next frame: {"Alive" if new_board[y][x] == ALIVE else "Dead "}')
                    self.scr.refresh()
                    self.scr.getch()

        self.board = new_board

    def _render_board(self) -> None:
        self.scr.addstr(0, 0, f'+{"-"*self.size[1]}+')
        for y in range(self.size[0]):
            line = f'|{self._board_line(y)}|'
            self.scr.addstr(y+1, 0, line)
        self.scr.addstr(self.size[0]+1, 0, f'+{"-"*self.size[1]}+')
        self.scr.refresh()

    def _render_menu(self, pattern:str='glider') -> None:
        self._render_board()
        self.scr.addstr(self.size[0]+3, 0, f'{pattern: ^{self.size[1]}}')
        self.scr.addstr(self.size[0]+4, 0, f'{"<- [a] | [w] Start [q] Exit | [d] ->": ^{self.size[1]}}')
        self.scr.refresh()


    def _load_pattern(self, pattern:str='glider') -> None:
        self._reset_board()
        xl = len(PATTERNS[pattern][0])
        yl = len(PATTERNS[pattern])
        ystart = self.size[0]//2 - yl//2
        xstart = self.size[1]//2 - xl//2
        for i, line in enumerate(PATTERNS[pattern]):
            self.board[ystart+i][xstart : xstart+xl] =  line.copy()


    def _choose_pattern(self) -> bool:
        pattern = 0
        patterns = list(PATTERNS.keys())
        while True:
            self._load_pattern(patterns[pattern])
            self._render_menu(patterns[pattern])
            ch = self.scr.getch()
            if ch == ord('a'):
                pattern = (pattern-1) % len(PATTERNS)
            elif ch == ord('d'):
                pattern = (pattern+1) % len(PATTERNS)
            elif ch == ord('w'):
                return True
            elif ch == ord('q'):
                return False

    def _board_line(self, y:int):
        return ''.join(['*' if cell == ALIVE else ' ' for cell in self.board[y]])

def main() -> None:
    stdscr = curses.initscr()
    curses.noecho()
    gof = GameOfLife(stdscr)
    gof.run(render=True)

    curses.echo()
    curses.endwin()

if __name__=='__main__':
    main()