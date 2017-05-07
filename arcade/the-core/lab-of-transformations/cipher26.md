<div class="markdown"><p>You've intercepted an encrypted message, and you are really curious about its contents. You were able to find out that the message initially contained only lowercase English letters, and was encrypted with the following cipher:</p>
<ul>
<li>Let all letters from <code>'a'</code> to <code>'z'</code> correspond to the numbers from <code>0</code> to <code>25</code>, respectively.</li>
<li>The number corresponding to the <code>i<sup>th</sup></code> letter of the encrypted message is then equal to the sum of numbers corresponding to the first <code>i</code> letters of the initial unencrypted <code>message</code> <em>modulo 26</em>.</li>
</ul>
<p>Now that you know how the <code>message</code> was encrypted, implement the algorithm to decipher it.</p>
<p><strong>Example</strong></p>
<p>For <code>message = "taiaiaertkixquxjnfxxdh"</code>, the output should be<br>
<code>cipher26(message) = "thisisencryptedmessage"</code>.</p>
<p>The initial message <code>"thisisencryptedmessage"</code> was encrypted as follows:</p>
<ul>
<li>letter <code>0</code>: <code>t -&gt; 19 -&gt; t</code>;</li>
<li>letter <code>1</code>: <code>th -&gt; (19 + 7) % 26 -&gt; 0 -&gt; a</code>;</li>
<li>letter <code>2</code>: <code>thi -&gt; (19 + 7 + 8) % 26 -&gt; 8 -&gt; i</code>;</li>
<li>etc.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string message</strong></p>
<p>An encrypted string containing only lowercase English letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ message.length ≤ 200</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>A decrypted message.</p>
</li>
</ul>
</div>