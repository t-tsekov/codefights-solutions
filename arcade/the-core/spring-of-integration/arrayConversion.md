<div class="markdown"><p>Given an array of <code>2<sup>k</sup></code> integers (for some integer <code>k</code>), perform the following operations until the array contains only one element:</p>
<ul>
<li>On the <code>1<sup>st</sup></code>, <code>3<sup>rd</sup></code>, <code>5<sup>th</sup></code>, etc. iterations (1-based) replace each pair of consecutive elements with their sum;</li>
<li>On the <code>2<sup>nd</sup></code>, <code>4<sup>th</sup></code>, <code>6<sup>th</sup></code>, etc. iterations replace each pair of consecutive elements with their product.</li>
</ul>
<p>After the algorithm has finished, there will be a single element left in the array. Return that element.</p>
<p><strong>Example</strong></p>
<p>For <code>inputArray = [1, 2, 3, 4, 5, 6, 7, 8]</code>, the output should be<br>
<code>arrayConversion(inputArray) = 186</code>.</p>
<p>We have <code>[1, 2, 3, 4, 5, 6, 7, 8] -&gt; [3, 7, 11, 15] -&gt; [21, 165] -&gt; [186]</code>, so the answer is <code>186</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer inputArray</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ inputArray.length ≤ 20</code>,<br>
<code>-9 ≤ inputArray[i] ≤ 99</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>