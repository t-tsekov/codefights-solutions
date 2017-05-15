<div class="markdown"><p>Given an array of words and a length <code>L</code>, format the text such that each line has exactly <code>L</code> characters and is fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack as many words as possible in each line. Add extra spaces when necessary so that each line has exactly <code>L</code> characters.</p>
<p>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text and lines with one word only, the words should be left justified with no extra space inserted between them.</p>
<p><strong>Example</strong></p>
<p>For<br>
<code>words = ["This", "is", "an", "example", "of", "text", "justification."]</code><br>
and <code>L = 16</code>, the output should be</p>
<pre><code>textJustification(words, L) = ["This    is    an",
                               "example  of text",
                               "justification.  "]
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string words</strong></p>
<p>An array of words. Each word is guaranteed not to exceed <code>L</code> in length.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ words.length ≤ 150</code>,<br>
<code>0 ≤ words[i].length ≤ L</code>.</p>
</li>
<li>
<p><strong>[input] integer L</strong></p>
<p>The length that all the lines in the output array should be.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ L ≤ 60</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The formatted text as an array containing lines of text, with each line having a length of <code>L</code>.</p>
</li>
</ul>
</div>