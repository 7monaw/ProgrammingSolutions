# Guess the Data Structure #

***This problem was taken from the Rujia Liu's Present 3: A datastructure contest celebrating the 100th anniversary of Tsinghua University. It was written by Rujia Liu***

<p align="justify">
There is a bag-like data structure, supporting two operations:

$1$: Throw an element $x$ into the bag.

$2$: Take out an element $x$ from the bag.

Given a sequence of operations with return values, you’re going to guess the data structure. It is a stack (Last-In, First-Out), a queue (First-In, First
-Out), a priority-queue (Always take out larger elements first) or something else that you can hardly imagine!

### Input ###
There are several test cases. Each test case begins with a line containing a single integer $n$ ($1 \le n \le 1000$). Each of the next $n$ lines is either 
a type-1 command, or an integer 2 followed by an integer $x$. This means that executing the type-2 command returned the element $x$. The value of $x$ is
always a positive integer not larger than $100$. The input is terminated by end-of-file (EOF). The size of input file does not exceed 1MB.

### Output ###
For each test case, output one of the following:

`stack`

It’s definitely a stack.

`queue`

It’s definitely a queue.

`priority queue`

It’s definitely a priority queue.

`impossible`

It can’t be a stack, a queue or a priority queue.

`not sure`

It can be more than one of the three data structures mentioned above.

</p>

<table>
  <tr>
    <th>Sample Input</th>
    <th>Sample Output</th>
  </tr>
  <tr>
    <td valign="top">
    <pre>
6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4
1
2 1
    </pre>
    </td>
    <td valign="top">
    <pre>
queue
not sure
impossible
stack
priority queue
impossible
    </pre>
    </td>
  </tr>
</table>
