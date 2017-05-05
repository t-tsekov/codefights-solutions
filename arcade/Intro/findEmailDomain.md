<div class="markdown"><p>An email address such as <code>"John.Smith@example.com"</code> is made up of a local part (<code>"John.Smith"</code>), an <code>"@"</code> symbol, then a domain part (<code>"example.com"</code>).</p>
<p>The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. <a href="https://en.wikipedia.org/wiki/Email_address#Examples" target="_blank">Here</a> you can look at several examples of correct and incorrect email addresses.</p>
<p>Given a valid email address, find its domain part.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>address = "prettyandsimple@example.com"</code>, the output should be<br>
<code>findEmailDomain(address) = "example.com"</code>;</li>
<li>For <code>address = "&lt;&gt;[]:,;@\"!#$%&amp;*+-/=?^_{}| ~.a\"@example.org"</code>, the output should be<br>
<code>findEmailDomain(address) = "example.org"</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string address</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>10 ≤ address.length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
</li>
</ul>
</div>