<div class="markdown"><p>A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.</p>
<p>The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (<code>0</code> to <code>9</code> or <code>A</code> to <code>F</code>), separated by hyphens (e.g. <code>01-23-45-67-89-AB</code>).</p>
<p>Your task is to check by given string <code>inputString</code> whether it corresponds to MAC-48 address or not.</p>
<p><strong>Example</strong></p>
<ul>
<li>For <code>inputString = "00-1B-63-84-45-E6"</code>, the output should be<br>
<code>isMAC48Address(inputString) = true</code>;</li>
<li>For <code>inputString = "Z1-1B-63-84-45-E6"</code>, the output should be<br>
<code>isMAC48Address(inputString) = false</code>;</li>
<li>For <code>inputString = "not a MAC-48 address"</code>, the output should be<br>
<code>isMAC48Address(inputString) = false</code>.</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string inputString</strong></p>
<p><em>Guaranteed constraints:</em><br>
<code>15 ≤ inputString.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>inputString</code> corresponds to MAC-48 address naming rules, <code>false</code> otherwise.</p>
</li>
</ul>
</div>