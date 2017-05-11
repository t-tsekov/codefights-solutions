<div class="markdown"><p>In a large and famous supermarket a new major campaign was launched. From now on, each <code>n<sup>th</sup></code> customer has a chance to win a prize: a brand new luxury car! However, it's not that simple. A customer wins a prize only if the total price of their purchase is divisible by <code>d</code>. This number is kept as a secret, so the customers don't know in advance how much they should spend on their purchases. The winners will be announced once the campaign is over.</p>
<p>Your task is to implement a function that will determine the winners. Given the <code>purchases</code> of some customers over time, return the 1-based indices of all the customers who won the prize, i.e. each <code>n<sup>th</sup></code> who spend on their purchases amount of money divisible by <code>d</code>.</p>
<p><strong>Example</strong></p>
<p>For <code>purchases = [12, 43, 13, 465, 1, 13]</code>, <code>n = 2</code> and <code>d = 3</code>,<br>
the output should be<br>
<code>superPrize(purchases, n, d) = [4]</code>.</p>
<p>Each second customer has a chance to win a car, which makes customers <code>2</code>, <code>4</code> and <code>6</code> potential winners. Customer number <code>2</code> spent <code>43</code> on his purchase, which is not divisible by <code>3</code>. <code>13</code> also is not divisible by <code>3</code>, so the sixth customer also doesn't get the price. Customer <code>4</code>, however, spent <code>465</code>, which is divisible by <code>3</code>, so he is the only lucky guy.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer purchases</strong></p>
<p>A list that represents the cost of the purchases some customers made.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ purchases.length ≤ 100</code>,<br>
<code>1 ≤ purchases[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer d</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ d ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted list of 1-based customers who won the prize.</p>
</li>
</ul>
</div>