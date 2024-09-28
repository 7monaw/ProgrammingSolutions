# Pebbles Solitaire 2 #

***This problem was taken from the adapted form of Swedish Championships 2000***

<p align="justify">
I bet you have seen a pebble solitaire game. You know the game where you are given a board with an arrangment of small cavities, initially all but one occupied
by a pebble each. The aim of the game is to remove as many pebbles as possible from the board. Pebbles disappear from the board as a result of a move. A move is
possible if there is a straight line of three adjacent cavities, let us call them $A$, $B$, and $C$, with $B$ in the middle, where $A$ is vacant, but $B$ and $C$
each contain a pebble. The move consists of moving the pebble from $C$ to $A$, and removing the pebble in $B$ from the board. You may continue to make moves until
no more moves are possible.

In this problem, we look at a simple variant of this game, namely a board with twelve cavities located along a line. In the beginning of each game, some of the
cavities are occupied by pebbles. Your mission is to find a sequence of moves such that as few pebbles as possible are left on the board.

<p align="center">
    <img src="https://github.com/7monaw/ProgrammingSolutions/blob/main/Pebble_Solitaire/pebbles.png" alt
        width="500" 
        height="178"/>
    <br>
    <caption><b>Figure 1:</b> Figure 1: In a) there are two possible moves, namely $8\rightarrow6$, or $7\rightarrow9$. In b) the result of the $8\rightarrow6$ move
      is depicted, and again there are two possible moves, $5\rightarrow7$, or $6\rightarrow4$. Making the first of these results in c), from which there are no
      further moves.</caption>
</p>


### Input ###
The input begins with a positive integer $n \e 10$ on a line of its own. Thereafter $n$ different games follow. Each game consists of one line of input with exactly
twelve characters, describing the twelve cavities of the board in order. Each character is  either ‘-’ or ‘o’. A ‘-’ character denotes an empty cavity, whereas an ‘o’
character denotes a cavity with a pebble in it. There is at least one pebble in all games.

### Output ###
For each of the $n$ games in the input, output the minimum number of pebbles left on the board possible to obtain as a result of moves, on a line of its own.

</p>

<table>
    <tr>
        <th>Sample Input 1</th>
        <th>Sample Output 1</th>
    </tr>
    <tr>
        <td valign="top">
            <pre>
5
---oo----------oo------
-o--o-oo-----o--o-oo---
-o----ooo----o----ooo--
ooooooooooooooooooooooo
oooooooooo-ooooooooooo-
            </pre>
        </td>
        <td valign="top">
            <pre>
2
4
6
23
4
            </pre>
        </td>
    </tr>
    <tr>
</table>
