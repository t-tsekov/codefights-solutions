<div class="markdown"><p>You've been invited to a job interview at a famous company that tests programming challenges. To evaluate your coding skills, they have asked you to parse a given problem's input given as an <code>inputString</code> string, and count the number of <em>primitive type</em> elements within it.</p>
<p>The <code>inputString</code> can be either a <em>primitive type</em> variable or an array (possibly multidimensional) that contains elements of the <em>primitive types</em>.<br>
A <em>primitive type</em> variable can be:</p>
<ul>
<li>an integer number;</li>
<li>a string, which is surrounded by <code>"</code> characters (note that it may contain <strong>any</strong> character except <code>"</code>);</li>
<li>a boolean, which is either <code>true</code> or <code>false</code>.</li>
</ul>
<p>Return the total number of <em>primitive type</em> elements inside <code>inputString</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>inputString = "[[0, 20], [33, 99]]"</code>, the output should be<br>
<code>countElements(inputString) = 4</code>;</li>
<li>For <code>inputString = "[ "one", 2, "three" ]"</code>, the output should be<br>
<code>countElements(inputString) = 3</code>;</li>
<li>For <code>inputString = "true"</code>, the output should be<br>
<code>countElements(inputString) = 1</code>;</li>
<li>For <code>inputString = "[[1, 2, [3]], 4]"</code>, the output should be<br>
<code>countElements(inputString) = 4</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string inputString</strong></p>
<p>Correct input of a given problem.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ inputString.length ≤ 60</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The total number of <em>primitive type</em> elements within the input.</p>
</li>
</ul>
</div>