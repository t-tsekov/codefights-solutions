<div class="markdown"><p>Some file managers sort filenames taking into account case of the letters, others compare strings as if all of the letters are of the same case. That may lead to different ways of filename ordering.</p>
<p>Call two filenames <em>an unstable pair</em> if their ordering depends on the case.</p>
<p>To compare two filenames <code>a</code> and <code>b</code>, find the first position <code>i</code> at which <code>a[i] ≠ b[i]</code>. If <code>a[i] &lt; b[i]</code>, then <code>a &lt; b</code>. Otherwise <code>a &gt; b</code>. If such position doesn't exist, the shorter string goes first.</p>
<p>Given two filenames, check whether they form an unstable pair.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>filename1 = "aa"</code> and <code>filename2 = "AAB"</code>, the output should be<br>
<code>isUnstablePair(filename1, filename2) = true</code>.</p>
<p>Because <code>"AAB" &lt; "aa"</code>, but <code>"AAB" &gt; "AA"</code>.</p>
</li>
<li>
<p>For <code>filename1 = "A"</code> and <code>filename2 = "z"</code>, the output should be<br>
<code>isUnstablePair(filename1, filename2) = false</code>.</p>
<p>Both <code>"A" &lt; "z"</code> and <code>"a" &lt; "z"</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string filename1</strong></p>
<p>A non-empty string of letters and digits.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ filename1.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string filename2</strong></p>
<p>A non-empty string of letters and digits. It's guaranteed that there is no ambiguity, i.e. even being considered in the same case strings are never equal.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ filename2.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>filename1</code> and <code>filename2</code> form an unstable pair, <code>false</code> otherwise.</p>
</li>
</ul>
</div>