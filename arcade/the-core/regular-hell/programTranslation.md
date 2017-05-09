<div class="markdown"><p>As an avid user of CodeFights, you find it frustrating that there are no debugging and recovery tasks in your favorite language, PHP. You decide to help the platform by translating solutions in JavaScript into PHP.</p>
<p>You quickly discover that this approach is quite convenient: sometimes all you have to do is substitute the function arguments by adding the <code>$</code> sign in front of them. At first you do this manually, but soon realize that it won't get you far enough.</p>
<p>Now you need to implement a function that, given a <code>solution</code> written in JavaScript and its <code>args</code>, adds a <code>$</code> sign in front of each <code>args[i]</code> (unless there is already a dollar sign present).</p>
<p>Given a <code>solution</code> in JavaScript and its <code>args</code>, return the almost-PHP solution.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>solution = 
    "function add($n, m) {\t
       return n + $m;\t
     }"
</code></pre>
<p>and <code>args = ["n", "m"]</code>, the output should be</p>
<pre><code>programTranslation(solution, args) =
    "function add($n, $m) {\t
       return $n + $m;\t
     }"
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string solution</strong></p>
<p>Solution written in JavaScript. It is guaranteed that:</p>
<ul>
<li>the given code snippet is correct and can be executed in the CodeFights environment with <code>$</code> symbols removed;</li>
<li><code>solutions</code> does not contain comments or string variables;</li>
<li><code>solutions</code> does not start with one of the <code>args</code>.</li>
</ul>
<p>Due to system limitations, tabulation (<code>\t</code>) characters are used instead of newlines (<code>\n</code>).</p>
<p><em>Guaranteed constraints:</em><br>
<code>40 ≤ solution.length ≤ 200</code>.</p>
</li>
<li>
<p><strong>[input] array.string args</strong></p>
<p>An array of distinct function arguments. It is guaranteed that each argument is valid, i.e. it consists only of uppercase and lowercase letters <code>'A'</code> through <code>'Z'</code>, the underscore <code>'_'</code> and, except for the first character, the digits <code>'0'</code> through <code>'9'</code>. It is also guaranteed that no argument coincides with one of the reserved words.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ args.length ≤ 10</code>,<br>
<code>1 ≤ args[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The given <code>solution</code> with <code>args</code> replaced to PHP-style.</p>
</li>
</ul>
</div>