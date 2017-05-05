<div class="markdown"><p>An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the <em>IPv4 address</em>.</p>
<p>IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, each ranging from <code>0</code> to <code>255</code>, separated by dots, e.g., <code>172.16.254.1</code>.</p>
<p>Given a string, find out if it satisfies the IPv4 address naming rules.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>inputString = "172.16.254.1"</code>, the output should be<br>
<code>isIPv4Address(inputString) = true</code>;</p>
</li>
<li>
<p>For <code>inputString = "172.316.254.1"</code>, the output should be<br>
<code>isIPv4Address(inputString) = false</code>.</p>
<p><code>316</code> is not in range <code>[0, 255]</code>.</p>
</li>
<li>
<p>For <code>inputString = ".254.255.0"</code>, the output should be<br>
<code>isIPv4Address(inputString) = false</code>.</p>
<p>There is no first number.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] string inputString</strong></p>
<p>A string consisting of digits, full stops and lowercase Latin letters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>5 ≤ inputString.length ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>inputString</code> satisfies the IPv4 address naming rules, <code>false</code> otherwise.</p>
</li>
</ul>
</div>