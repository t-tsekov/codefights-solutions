<div class="markdown"><p>One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each <code>message</code> received from your friend into a more readable form.</p>
<p>Implement a function that will change the very first symbol of the given <code>message</code> to uppercase, and make all the other letters lowercase.</p>
<p><strong>Example</strong></p>
<p>For <code>message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"</code>,<br>
the output should be<br>
<code>fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1"</code>.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string message</strong></p>
<p>A string consisting of Latin letters, whitespace characters, digits and punctuation marks.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ message.length ≤ 65</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Fixed <code>message</code> with its first letter capitalized, and all other letters converted to lowercase.</p>
</li>
</ul>
</div>