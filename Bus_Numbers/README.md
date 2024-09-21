# Bus Numbers #

***This problem was taken from the KTH Training. It was written by Lukáš Poláček***

<p align="justify">
Your favourite public transport company LS (we cannot use their real name here, so we permuted the letters) wants to change signs on all bus stops. 
Some bus stops have quite a few buses that stop there and listing all the buses takes space. However, if for example buses $141, 142, 143$ stop there, 
we can write $141 – 143$ instead and this saves space. Note that just for two buses this does not save space.

You are given a list of buses that stop at a bus stop. What is the shortest representation of this list?

### Input ###
The first line of the input contains one integer $N, 1 \le N \le 1000$, the number of buses that stop at a bus stop. Then next line contains a
list of space separated integers between $1$ and $1000$, which denote the bus numbers. All numbers are distinct.

### Output ###
Print the shortest representation of the list of bus numbers. Use the format as in the example, separate numbers with single spaces and output them in sorted order.

<table>
  <tr>
    <th>Sample Input</th>
    <th>Sample Output</th>
  </tr>
  <tr>
    <td valign="top">
    <pre>
6
180 141 174 143 142 175
    </pre>
    </td>
    <td valign="top">
    <pre>141-143 174 175 180<pre>
    </td>
  </tr>
</table>
