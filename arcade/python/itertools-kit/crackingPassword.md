<div class="markdown"><p>You've been trying to crack the password from your friend's laptop (just to prank him, malicious intent!), but with no luck. However, looks like you're finally up to something: you checked the keyboard with the "little detective" game set and determined that the password consists of a limited set of <code>digits</code>.</p>
<p>You've seen your friend typing the password quite a few times, and are now sure that it consists of <code>k</code> digits. You also know that he is very superstitious and believes in the power of number <code>d</code>, so the password is apt to be divisible by it.</p>
<p>Given the <code>digits</code> that comprise the password, its length <code>k</code> and the number <code>d</code> by which it is divisible, return a sorted list of strings that should be tried as passwords.</p>
<p><strong>Example</strong></p>
<p>For <code>digits = [1, 5, 2]</code>, <code>k = 2</code> and <code>d = 3</code>,<br>
the output should be<br>
<code>crackingPassword(digits, k, d) = ["12", "15", "21", "51"]</code>.</p>
<p>Here are all the numbers of length <code>2</code>: <code>11</code>, <code>15</code>, <code>12</code>, <code>51</code>, <code>55</code>, <code>52</code>, <code>21</code>, <code>25</code> and <code>22</code>. Only four of them are divisible by <code>3</code>, and they comprise the answer.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer digits</strong></p>
<p>Array of distinct digits.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ digits.length ≤ 10</code>,<br>
<code>0 ≤ digits[i] ≤ 9</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>The number of digits in the password.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ k ≤ 9</code>.</p>
</li>
<li>
<p><strong>[input] integer d</strong></p>
<p>The lucky number by which the password should be divisible.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ d ≤ 300</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A sorted list of strings that should be tested as passwords.</p>
</li>
</ul>
</div>