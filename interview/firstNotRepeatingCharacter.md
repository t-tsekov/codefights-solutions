<div class="markdown"><p><em>Note: Write a solution that only iterates over the string once and uses <code>O(1)</code> additional memory, since this is what you would be asked to do during a real interview.</em></p>
<p>Given a string <code>s</code>, find and return the first instance of a non-repeating character in it. If there is no such character, return <code>'_'</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>s = "abacabad"</code>, the output should be<br>
<code>firstNotRepeatingCharacter(s) = 'c'</code>.</p>
<p>There are <code>2</code> non-repeating characters in the string: <code>'c'</code> and <code>'d'</code>. Return <code>c</code> since it appears in the string first.</p>
</li>
<li>
<p>For <code>s = "abacabaabacaba"</code>, the output should be<br>
<code>firstNotRepeatingCharacter(s) = '_'</code>.</p>
<p>There are no characters in this string that do not repeat.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A string that contains only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] char</strong></p>
<p>The first non-repeating character in <code>s</code>, or <code>'_'</code> if there are no characters that do not repeat.</p>
</li>
</ul>
</div>