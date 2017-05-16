<div class="markdown"><p>Let's define a <em>group of anagrams</em> as a list of words, where for each pair of words <code>w<sub>1</sub></code> and <code>w<sub>2</sub></code>, <code>w<sub>1</sub></code> is an <a href="keyword://anagram">anagram</a> of <code>w<sub>2</sub></code>.</p>
<p>Given a list of <code>words</code>, split it into the smallest possible number of <em>groups of anagrams</em> and return this number as the answer.</p>
<p><strong>Example</strong></p>
<p>For <code>words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]</code>, the output should be<br>
<code>groupsOfAnagrams(words) = 4</code>.</p>
<p>The <code>4</code> groups of anagrams in this example are <code>("tea", "eat", "ate")</code>, <code>("apple")</code>, <code>("vaja", "java")</code>, and <code>("cut", "utc")</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string words</strong></p>
<p>A list of words, each containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ words.length ≤ 10<sup>5</sup></code>,<br>
<code>1 ≤ words[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The smallest possible number of groups of anagrams into which <code>words</code> can be split.</p>
</li>
</ul>
</div>