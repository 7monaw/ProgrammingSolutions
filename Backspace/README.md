# Backspace #

***This problem was taken from the Icelandic High School Competition 2016. It was written by Tómas Ken Magnússon and Bjarki Ágúst Guðmundsson***

<p align="justify">
Shortly before the programming contest started, Bjarki decided to update his computer. He didn’t notice anything strange until he started coding in his 
favorite editor, Bim (Bjarki IMproved). Usually when he’s writing in an editor and presses the backspace key a single character is erased to the left. 
But after the update pressing that key outputs the character <. He’s tested all the editors on his machine, Bmacs, Neobim, bjedit, NoteBjad++ and Subjark
Text, but they all seem to have the same problem. He doesn’t have time to search the web for a solution, and instead decides to temporarily circumvent the
issue with a simple program.

Help Bjarki write a program that takes as input the string that was written in the text editor, and outputs the string as Bjarki intended to write it. You
can assume that Bjarki never intended to write the character <, and that Bjarki never pressed the backspace key in an empty line.

### Input ###
One line containing the string that was written in the text editor. The length of the string is at most $10^6$
, and it will only contain lowercase letters from the English alphabet as well as the character <.

### Output ###
One line containing the string as Bjarki intended to write it.

</p>

<table>
  <tr>
    <th>Sample Input 1</th>
    <th>Sample Output 1</th>
  </tr>
  <tr>
    <td valign="top">
      <pre>a<bc<</pre>
      </td>
      <td valign="top">
      <pre>b</pre>
    </td>
  </tr>
  <tr>
    <th>Sample Input 2</th>
    <th>Sample Output 2</th>
  </tr>
  <tr>
    <td valign="top">
      <pre>foss<<rritun</pre>
      </td>
      <td valign="top">
      <pre>forritun</pre>
    </td>
  </tr>
  <tr>
    <th>Sample Input 3</th>
    <th>Sample Output 3</th>
  </tr>
  <tr>
    <td valign="top">
      <pre>a<a<a<aa<<</pre>
      </td>
      <td valign="top">
      <pre> </pre>
    </td>
  </tr>
</table>
