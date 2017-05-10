<div class="markdown"><p>You decided to found your own startup company and now want to choose a proper name for it. There are three large <code>companies</code> that you want to compete against, and since their names are quite popular you want to use their names as a starting point. You want to use only <em>popular</em> characters in the name of your company, but not too <em>mainstream</em>. You consider a character to be <em>popular</em> if it appears in at least two company names, and consider it to be <em>mainstream</em> if it appears in all three.</p>
<p>Given the names of the <code>companies</code>, return the list of characters that are <em>popular</em> but <em>not mainstream</em> sorted by their ASCII codes.</p>
<p><strong>Example</strong></p>
<p>For <code>companies = ["coolcompany", "nicecompany", "legendarycompany"]</code>,<br>
the output should be<br>
<code>startupName(companies) = ['e', 'l']</code>.</p>
<p>Here's how the answer can be obtained:</p>
<ul>
<li>these letters appear in all three company names and are thus <em>mainstream</em>: <code>'a'</code>, <code>'c'</code>, <code>'m'</code>, <code>'n'</code>, <code>'o'</code>, <code>'p'</code>, <code>'y'</code>;</li>
<li>these letters appear only in one of the company names and are thus <em>not popular</em>: <code>'d'</code>, <code>'g'</code>, <code>'i'</code>, <code>'r'</code>;</li>
<li>the remaining letters are <em>popular</em> and <em>not mainstream</em>: <code>'e'</code>, <code>'l'</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string companies</strong></p>
<p>Array of three strings representing the company names. Each name is guaranteed to consist only of lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>companies.length = 3</code>,<br>
<code>2 ≤ companies[i].length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.char</strong></p>
<p>Array of characters that are <em>popular</em> but not <em>mainstream</em>.</p>
</li>
</ul>
</div>