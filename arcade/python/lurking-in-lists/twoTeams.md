<div class="markdown"><p>There are some <code>students</code> standing in a row, each has some number written on their back. The students are about to divide into two teams by counting off by twos: those standing at the even positions (0-based) will go to team A, and those standing at the odd position will join the team B.</p>
<p>Your task is to calculate the difference between the sums of numbers written on the backs of the students that will join team A, and those written on the backs of the students that will join team B.</p>
<p><strong>Example</strong></p>
<p>For <code>students = [1, 11, 13, 6, 14]</code>, the output should be<br>
<code>twoTeams(students) = 11</code>.</p>
<p>Students with numbers <code>1</code>, <code>13</code> and <code>14</code> will join team A, and students with numbers <code>11</code> and <code>6</code> will join team B. Thus, the answer is <code>(1 + 13 + 14) - (11 + 6) = 11</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer students</strong></p>
<p>Array of numbers written on the students' backs.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ students.length ≤ 50</code>,<br>
<code>1 ≤ students[i] ≤ 99</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>