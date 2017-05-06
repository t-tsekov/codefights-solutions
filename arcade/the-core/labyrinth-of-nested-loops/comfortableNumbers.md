<div class="markdown"><p>Let's say that number <code>a</code> feels <em>comfortable</em> with number <code>b</code> if <code>a ≠ b</code> and <code>b</code> lies in the segment <code>[a - s(a), a + s(a)]</code>, where <code>s(x)</code> is the sum of <code>x</code>'s digits.</p>
<p>How many pairs <code>(a, b)</code> are there, such that <code>a &lt; b</code>, both <code>a</code> and <code>b</code> lie on the segment <code>[L, R]</code>, and each number feels <em>comfortable</em> with the other?</p>
<p><strong>Example</strong></p>
<p>For <code>L = 10</code> and <code>R = 12</code>, the output should be<br>
<code>comfortableNumbers(L, R) = 2</code>.</p>
<p>Here are all values of <code>s(x)</code> to consider:</p>
<ul>
<li><code>s(10) = 1</code>, so <code>10</code> is <em>comfortable</em> with <code>9</code> and <code>11</code>;</li>
<li><code>s(11) = 2</code>, so <code>11</code> is <em>comfortable</em> with <code>9</code>, <code>10</code>, <code>12</code> and <code>13</code>;</li>
<li><code>s(12) = 3</code>, so <code>12</code> is <em>comfortable</em> with <code>9</code>, <code>10</code>, <code>11</code>, <code>13</code>, <code>14</code> and <code>15</code>.</li>
</ul>
<p>Thus, there are <code>2</code> pairs of numbers <em>comfortable</em> with each other within the segment <code>[10; 12]</code>: <code>(10, 11)</code> and <code>(11, 12)</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer L</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ L ≤ R ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer R</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ L ≤ R ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of pairs satisfying all the above conditions.</p>
</li>
</ul>
</div>