<div class="markdown"><p>You came to work in a big company as a Senior Python Developer. Unfortunately your team members seem to be quite old-school: you can see old-style string formatting everywhere in the code, which is not too cool. You tried to force the team members to start using the new style formatting, but it looks like it will take some time to persuade them: old habits die hard, especially in old-school programmers.</p>
<p>To show your colleagues that the new style formatting is not that different from the old style, you decided to implement a function that will turn the old-style syntax into a new one. Implement a function that will turn the old-style string formating <code>s</code> into a new one so that the following two strings have the same meaning:</p>
<ul>
<li><code>s % (*args)</code></li>
<li><code>s.format(*args)</code></li>
</ul>
<p><strong>Example</strong></p>
<p>For <code>s = "We expect the %f%% growth this week"</code>, the output should be<br>
<code>newStyleFormatting(s) = "We expect the {}% growth this week"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string s</strong></p>
<p>A correct old-style formatting string. It is guaranteed that each <code>%</code> sign in it is always followed either by a correct conversion type or by another <code>'%'</code> sign (see <a href="https://docs.python.org/2/library/string.html#format-specification-mini-language">this</a> for reference). It is also guaranteed that it doesn't contain curly brackets (<code>'{'</code> or <code>'}'</code>).</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ s.length ≤ 70</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A new-style formatting string without positional indices.</p>
</li>
</ul>
</div>