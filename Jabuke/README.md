# Jabuke #

***This problem was taken from the Croatian Open Competition in Informatics 2007/2008, contest #5***

<p align="justify">
Ante bought a piece of land. The land contains N apple trees, but his piece is triangular and it is not easy for him to determine which apple trees belong to him.
  
Your program will be given the coordinates of the vertices of the triangle forming Ante’s piece, and the coordinates of all apple trees. Determine the area of land belonging to Ante, and the number of trees belonging to him. We consider apple trees on the very border of his piece to belong to him.

The area of a triangle with vertices $(x_A, y_A)$, $(x_B, y_B)$ and $(x_C, y_C)$ is given by the following formula:

<p align="center">
    $\frac{|x_A(y_B-y_C)+x_B(y_C-y_A)+x_C(y_A-y_B)|}{2}$
</p>


### Input ###
The first three lines contain the coordinates of the vertices of the triangle.

The following line contains the integer $N(1\le N\le100)$, the number of apple trees.

Each of the following $N$ lines contains the coordinates of one apple tree.

All coordinate are pairs of positive integers less than 1000, separated by a space.

### Output ###
Output the area of land belonging to Ante on the first line, with exactly one digit after the decimal point.

Output the number of trees belonging to Ante on the second line.

</p>

<table>
    <tr>
        <th>Sample Input 1</th>
        <th>Sample Output 1</th>
    </tr>
    <tr>
        <td valign="top">
            <pre>
1 1
5 1
3 3
4
3 1
3 2
3 3
3 4
            </pre>
            </td>
            <td valign="top">
            <pre>
4.0
3
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
3 2
5 4
1 6
3
2 4
3 5
4 3
        </pre>
        </td>
        <td valign="top">
        <pre>
6.0
3
        </pre>
        </td>
    </tr>
    <tr>
        <th>Sample Input 3</th>
        <th>Sample Output 3</th>
    </tr>
    <tr>
        <td valign="top">
        <pre>
2 6
5 1
7 8
5
1 4
3 5
6 4
6 5
4 7
        </pre>
        </td>
        <td valign="top">
        <pre>
15.5
2
        </pre>
        </td>
    </tr>
</table>
