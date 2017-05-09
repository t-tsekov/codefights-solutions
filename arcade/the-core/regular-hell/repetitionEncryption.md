<div class="markdown"><p>Jane just got a <code>letter</code> from her friend and realized that something's wrong: some words in the <code>letter</code> are written twice in a row. The thing is, she and her friend devised an ingenious cypher, the key to which is the number of pairs of repeated words in the encoded text. The cases of the words don't matter.</p>
<p>Formally, a <em>word</em> is a <a href="keyword://substring">substring</a> of <code>letter</code> consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.</p>
<p>For obvious reasons, Jane can't tell you how the encryption works, but she needs your help with calculating the number of pairs of consecutive equal words. Write a function that, given a <code>letter</code>, returns this number.</p>
<p><strong>Example</strong></p>
<p>For <code>letter = "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"</code>,<br>
the output should be<br>
<code>repetitionEncryption(letter) = 4</code>.</p>
<p>There are <code>4</code> pairs of consecutive identical words in the text. They are shown in different colors below:<br>
"<b><font color="red">Hi, hi</font></b> Jane! I'm <b><font color="blue">so. So</font></b> glad <b><font color="green">to to</font></b> finally be able to <b><font color="pink">write - WRITE</font></b>!! - to you!"</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string letter</strong></p>
<p>The letter Jane's friend wrote to her. It is guaranteed that there are no more than two consecutive equal words in a row. It is also guaranteed that between two such pairs there are at least two symbols.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of pairs of consecutive equal words in the <code>letter</code>.</p>
</li>
</ul>
</div>