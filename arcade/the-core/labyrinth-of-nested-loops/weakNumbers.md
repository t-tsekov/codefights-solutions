<div class="markdown"><p>We define the <em>weakness</em> of number <code>x</code> as the number of positive integers smaller than <code>x</code> that have more divisors than <code>x</code>.</p>
<p>It follows that the <em>weaker</em> the number, the greater overall <em>weakness</em> it has. For the given integer <code>n</code>, you need to answer two questions:</p>
<ul>
<li>what is the <em>weakness</em> of the <em>weakest</em> numbers in the range <code>[1, n]</code>?</li>
<li>how many numbers in the range <code>[1, n]</code> have this <em>weakness</em>?</li>
</ul>
<p>Return the answer as an array of two elements, where the first element is the answer to the first question, and the second element is the answer to the second question.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 9</code>, the output should be<br>
<code>weakNumbers(n) = [2, 2]</code>.</p>
<p>Here are the number of divisors and the specific <em>weakness</em> of each number in range <code>[1, 9]</code>:</p>
<ul>
<li><code>1</code>: d(1) = 1, weakness(1) = 0;</li>
<li><code>2</code>: d(2) = 2, weakness(2) = 0;</li>
<li><code>3</code>: d(3) = 2, weakness(3) = 0;</li>
<li><code>4</code>: d(4) = 3, weakness(4) = 0;</li>
<li><code>5</code>: d(5) = 2, weakness(5) = 1;</li>
<li><code>6</code>: d(6) = 4, weakness(6) = 0;</li>
<li><code>7</code>: d(7) = 2, weakness(7) = 2;</li>
<li><code>8</code>: d(8) = 4, weakness(8) = 0;</li>
<li><code>9</code>: d(9) = 3, weakness(9) = 2.</li>
</ul>
<p>As you can see, the maximal <em>weakness</em> is <code>2</code>, and there are <code>2</code> numbers with that <em>weakness</em> level.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array of two elements: the <em>weakness</em> of the <em>weakest</em> number, and the number of integers in range <code>[1, n]</code> with this <em>weakness</em>.</p>
</li>
</ul>
</div>