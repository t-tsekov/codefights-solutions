<div class="markdown"><p>A <code>step(x)</code> operation works like this: it changes a number <code>x</code> into <code>x - s(x)</code>, where <code>s(x)</code> is the sum of <code>x</code>'s digits. You like applying functions to numbers, so given the number <code>n</code>, you decide to build a decreasing sequence of numbers: <code>n</code>, <code>step(n)</code>, <code>step(step(n))</code>, etc., with <code>0</code> as the last element.</p>
<p>Building a single sequence isn't enough for you, so you replace all elements of the sequence with the sums of their digits (<code>s(x)</code>). Now you're curious as to which number appears in the new sequence most often. If there are several answers, return the maximal one.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>n = 88</code>, the output should be<br>
<code>mostFrequentDigitSum(n) = 9</code>.</p>
<ul>
<li>Here is the first sequence you built: <code>88</code>, <code>72</code>, <code>63</code>, <code>54</code>, <code>45</code>, <code>36</code>, <code>27</code>, <code>18</code>, <code>9</code>, <code>0</code>;</li>
<li>And here is <code>s(x)</code> for each of its elements: <code>16</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>0</code>.</li>
</ul>
<p>As you can see, the most frequent number in the second sequence is <code>9</code>.</p>
</li>
<li>
<p>For <code>n = 8</code>, the output should be<br>
<code>mostFrequentDigitSum(n) = 8</code>.</p>
<ul>
<li>At first you built the following sequence: <code>8</code>, <code>0</code></li>
<li><code>s(x)</code> for each of its elements is: <code>8</code>, <code>0</code></li>
</ul>
<p>As you can see, the answer is <code>8</code> (it appears as often as <code>0</code>, but is greater than it).</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ n ≤ 10<sup>5</sup></code>,</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The most frequent number in the sequence <code>s(n)</code>, <code>s(step(n))</code>, <code>s(step(step(n)))</code>, etc.</p>
</li>
</ul>
</div>