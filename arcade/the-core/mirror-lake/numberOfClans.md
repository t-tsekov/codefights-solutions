<div class="markdown"><p>Let's call two integers <code>A</code> and <code>B</code> <em>friends</em> if each integer from the array <code>divisors</code> is either a divisor of both <code>A</code> and <code>B</code> or neither <code>A</code> nor <code>B</code>. If two integers are <em>friends</em>, they are said to be in the same <em>clan</em>. How many clans are the integers from <code>1</code> to <code>k</code>, inclusive, broken into?</p>
<p><strong>Example</strong></p>
<p>For <code>divisors = [2, 3]</code> and <code>k = 6</code>, the output should be<br>
<code>numberOfClans(divisors, k) = 4</code>.</p>
<p>The numbers <code>1</code> and <code>5</code> are friends and form a <em>clan</em>, <code>2</code> and <code>4</code> are friends and form a <em>clan</em>, and <code>3</code> and <code>6</code> do not have friends and each is a <em>clan</em> by itself. So the numbers <code>1</code> through <code>6</code> are broken into <code>4</code> clans.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer divisors</strong></p>
<p>A non-empty array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ divisors.length &lt; 10</code>,<br>
<code>1 ≤ divisors[i] ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer k</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ k ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>