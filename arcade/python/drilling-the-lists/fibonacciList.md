<div class="markdown"><p>No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes <code>0, 1, 1, 2, 3, 5, ...</code>, in other words those whose length increase according to the <a href="keyword://fibonacci-sequence">Fibonacci sequence</a>.</p>
<p>The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer <code>n</code>, return a list of <code>n</code> lists, where the first element consists is empty (consists of <code>0</code> zeros), the second element consists of <code>1</code> zero, and so on.</p>
<p><strong>Example</strong></p>
<p>For <code>n = 6</code>, the output should be</p>
<pre><code>fibonacciList(n) = [[], 
                    [0], 
                    [0], 
                    [0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0, 0, 0]]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer n</strong></p>
<p>The size of the list you should return.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A 2-dimensional list of zeros, where the list sizes form the Fibonacci sequence.</p>
</li>
</ul>
</div>