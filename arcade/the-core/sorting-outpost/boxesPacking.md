<div class="markdown"><p>You are given <code>n</code> rectangular boxes, the <code>i<sup>th</sup></code> box has the length <code>length<sub>i</sub></code>, the width <code>width<sub>i</sub></code> and the height <code>height<sub>i</sub></code>. Your task is to check if it is possible to pack all boxes into one so that inside each box there is no more than one another box (which, in turn, can contain at most one another box, and so on). More formally, your task is to check whether there is such sequence of <code>n</code> different numbers <code>p<sub>i</sub></code> (<code>1 ≤ p<sub>i</sub> ≤ n</code>) that for each <code>1 ≤ i &lt; n</code> the box number <code>p<sub>i</sub></code> can be put into the box number <code>p<sub>i+1</sub></code>.<br>
A box can be put into another box if all sides of the first one are less than the respective ones of the second one. You can rotate each box as you wish, i.e. you can swap its length, width and height if necessary.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>length = [1, 3, 2]</code>, <code>width = [1, 3, 2]</code> and <code>height = [1, 3, 2]</code>, the output should be<br>
<code>boxesPacking(length, width, height) = true</code>;</li>
<li>For <code>length = [1, 1]</code>, <code>width = [1, 1]</code> and <code>height = [1, 1]</code>, the output should be<br>
<code>boxesPacking(length, width, height) = false</code>;</li>
<li>For <code>length = [3, 1, 2]</code>, <code>width = [3, 1, 2]</code> and <code>height = [3, 2, 1]</code>, the output should be<br>
<code>boxesPacking(length, width, height) = false</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer length</strong></p>
<p>Array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ length.length ≤ 10<sup>4</sup></code>,<br>
<code>1 ≤ length[i] ≤ 2 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.integer width</strong></p>
<p>Array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>width.length = length.length</code>,<br>
<code>1 ≤ width[i] ≤ 2 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.integer height</strong></p>
<p>Array of positive integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>height.length = length.length</code>,<br>
<code>1 ≤ height[i] ≤ 2 · 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if it is possible to put all boxes into one, <code>false</code> otherwise.</p>
</li>
</ul>
</div>