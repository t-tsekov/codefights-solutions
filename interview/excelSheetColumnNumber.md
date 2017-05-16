<div class="markdown"><p>Given a column title as it would appear in an Excel spreadsheet, return its corresponding column number. Column names and numbers follow a consistent pattern:</p>
<pre><code>    A -&gt; 1
    B -&gt; 2
    C -&gt; 3
    ...
    Z -&gt; 26
    AA -&gt; 27
    AB -&gt; 28
</code></pre>
<p><strong>Example</strong></p>
<p>For <code>s = "AB"</code>, the output should be<br>
<code>excelSheetColumnNumber(s) = 28</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string of uppercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 6</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
</div>