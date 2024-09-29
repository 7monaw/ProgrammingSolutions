# Restaurant Orders #

***This problem was taken from the KTH Challenge 2012. It was written by Ulf Lundström***

<p align="justify">
A friend of yours who is working as a waiter has a problem. A group of xkcd-fans have started to come to the restaurant and order food as in the comic strip
below. Each order takes him a lot of time to figure out, but maybe you can help him.

<p align="center">
    <img src="https://github.com/7monaw/ProgrammingSolutions/blob/main/Restaurant_Orders/np_complete.png" alt
        width="500" 
        height="178"/>
    <br>
    <caption><b>Figure 1:</b> Figure 1: Comic strip xkcd.com/287.</caption>
</p>

You are to write a program that finds out what was ordered given the total cost of the order and the cost of each item on the menu.

### Input ###
The input starts with a line containing one integer $n$ ($1 \le n \le 100$), the number of items on the menu. The next line contains $n$ space-separated
positive integers $c_1, c_2, ..., c_n$, denoting the cost of each item on the menu in Swedish kronor. No item costs more than $1000$ SEK.

This is followed by a line containing $m$ ($1 \le m \le 1000$), the number of orders placed, and a line with $m$ orders. Each order is given as an integer $s$
($1 \le m \le 30000$), the total cost of all ordered items in SEK.

### Output ###
For each order in the input output one line as follows. If there is one unique order giving the specified total cost, output a space-separated list of the
numbers of the items on that order in ascending order. If the order contains more than one of the same item, print the corresponding number the appropriate
number of times. The first item on the menu has number 1, the second 2, and so on.

If there doesn’t exist an order that gives the specified sum, output Impossible. If there are more than one order that gives the specified sum, output
Ambiguous.
</p>

<table>
    <tr>
        <th>Sample Input 1</th>
        <th>Sample Output 1</th>
    </tr>
    <tr>
        <td valign="top">
            <pre>
3
4 5 8
3
11 13 14
            </pre>
        </td>
        <td valign="top">
            <pre>
Impossible
Ambiguous
1 2 2
            </pre>
        </td>
    </tr>
    <tr>
        <th>Sample Input 2</th>
        <th>Sample Output 2</th>
    </tr>
    <tr>
        <td valign="top">
            <pre>
6
215 275 335 355 420 580
1
1505
            </pre>
        </td>
        <td valign="top">
            <pre>
Ambiguous
            </pre>
        </td>
    </tr>
    <tr>
</table>
