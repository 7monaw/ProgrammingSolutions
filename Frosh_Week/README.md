# Frosh Week #

***This problem was taken from the Waterloo Programming Contest 2010-10-02. It was written by Ondřej Lhoták***

<p align="justify">
During Frosh Week, students play various fun games to get to know each other and compete against other teams. In one such game, all the frosh on a team stand
in a line, and are then asked to arrange themselves according to some criterion, such as their height, their birth date, or their student number. This 
rearrangement of the line must be accomplished only by successively swapping pairs of consecutive students. The team that finishes fastest wins. Thus,
in order to win, you would like to minimize the number of swaps required.

### Input ###
The first line of input contains one positive integer $n$, the number of students on the team, which will be no more than one million. The following $n$ lines
each contain one integer between $1$ and $10^9$ (inclusive), the student number of each student on the team. No student number will appear more than once.

### Output ###
Output a line containing the minimum number of swaps required to arrange the students in increasing order by student number.

</p>

<table>
  <tr>
    <th>Sample Input</th>
    <th>Sample Output</th>
  </tr>
  <tr>
    <td valign="top">
    <pre>
3
3
1
2
    </pre>
    </td>
    <td valign="top">
    <pre>2</pre>
    </td>
  </tr>
</table>
