<div class="markdown"><p>The Calkin-Wilf tree is a tree in which the vertices correspond 1-for-1 to the positive rational numbers. The tree is rooted at the number <code>1</code>, and any rational number expressed in simplest terms as the fraction <code>a / b</code> has as its two children the numbers <code>a / (a + b)</code> and <code>(a + b) / b</code>. Every positive rational number appears exactly once in the tree. Here's what it looks like:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/calkinWilfSequence/img/tree.png?_tm=1490625641609" alt=""></p>
<p>The Calkin-Wilf sequence is the sequence of rational numbers generated by a breadth-first traversal of the Calkin-Wilf tree, where the vertices of the same level are traversed from left to right (as displayed in the image above). The sequence thus also contains each rational number exactly once, and can be represented as follows:</p>
<p><img src="https://codefightsuserpics.s3.amazonaws.com/tasks/calkinWilfSequence/img/sequence.png?_tm=1490625641800" alt=""></p>
<p>Given a rational <code>number</code>, your task is to return its 0-based index in the Calkin-Wilf sequence.</p>
<p><strong>Example</strong></p>
<p>For <code>number = [1, 3]</code>, the output should be<br>
<code>calkinWilfSequence(number) = 3</code>.</p>
<p>As you can see in the image above, <code>1 / 3</code> is the <code>3<sup>rd</sup></code> 0-based number in the sequence.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer number</strong></p>
<p>A positive rational number given as a <a href="keyword://reduced-fraction">reduced fraction</a>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>number.length = 2</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The 0-based index of the <code>number</code> in the Calkin-Wilf sequence.</p>
<p>It is guaranteed that the answer is not greater than <code>10<sup>6</sup></code>.</p>
</li>
</ul>
</div>