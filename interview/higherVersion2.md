<div class="markdown"><p>You have two version strings composed of several non-negative decimal fields that are separated by periods (<code>"."</code>). Both strings contain an equal number of numeric fields. Return <code>1</code> if the first version is higher than the second version, <code>-1</code> if it is smaller, and <code>0</code> if the two versions are the same.</p>
<p>The syntax follows the regular <em>semver</em> (semantic versioning) ordering rules:</p>
<pre><code>1.0.5 &lt; 1.1.0 &lt; 1.1.5 &lt; 1.1.10 &lt; 1.2.0 &lt; 1.2.2
&lt; 1.2.10 &lt; 1.10.2 &lt; 2.0.0 &lt; 10.0.0
</code></pre>
<p><strong>Example</strong></p>
<ul>
<li>For <code>ver1 = "1.2.2"</code> and <code>ver2 = "1.2.0"</code>, the output should be<br>
<code>higherVersion2(ver1, ver2) = 1</code>;</li>
<li>For <code>ver1 = "1.0.5"</code> and <code>ver2 = "1.1.0"</code>, the output should be<br>
<code>higherVersion2(ver1, ver2) = -1</code>;</li>
<li>For <code>ver1 = "1.0.5"</code> and <code>ver2 = "1.00.05"</code>, the output should be<br>
<code>higherVersion2(ver1, ver2) = 0</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string ver1</strong></p>
<p>Correct version as a string.</p>
<p><em>Guaranteed constraints:</em><br><br>
<code>1 ≤ ver1.length ≤ 350</code>.</p>
</li>
<li>
<p><strong>[input] string ver2</strong></p>
<p>Correct version as a string.</p>
<p><em>Guaranteed constraints:</em><br><br>
<code>1 ≤ ver2.length ≤ 350</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>Return <code>1</code> if <code>ver1</code> is higher than <code>ver2</code>, <code>-1</code> if it's smaller, and <code>0</code> if the two versions are the same.</p>
</li>
</ul>
</div>