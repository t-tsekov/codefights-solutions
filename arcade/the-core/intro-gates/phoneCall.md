<div class="markdown"><p>Some phone usage rate may be described as follows:</p>
<ul>
<li>first minute of a call costs <code>min1</code> cents,</li>
<li>each minute from the 2nd up to 10th (inclusive) costs <code>min2_10</code> cents</li>
<li>each minute after 10th costs <code>min11</code> cents.</li>
</ul>
<p>You have <code>s</code> cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?</p>
<p><strong>Example</strong></p>
<p>For <code>min1 = 3</code>, <code>min2_10 = 1</code>, <code>min11 = 2</code> and <code>s = 20</code>, the output should be<br>
<code>phoneCall(min1, min2_10, min11, s) = 14</code>.</p>
<p>Here's why:</p>
<ul>
<li>the first minute costs <code>3</code> cents, which leaves you with <code>20 - 3 = 17</code> cents;</li>
<li>the total cost of minutes <code>2</code> through <code>10</code> is <code>1 * 9 = 9</code>, so you can talk <code>9</code> more minutes and still have <code>17 - 9 = 8</code> cents;</li>
<li>each next minute costs <code>2</code> cents, which means that you can talk <code>8 / 2 = 4</code> more minutes.</li>
</ul>
<p>Thus, the longest call you can make is <code>1 + 9 + 4 = 14</code> minutes long.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer min1</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ min1 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer min2_10</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ min2_10 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer min11</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ min11 ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer s</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ s ≤ 60</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>