<div class="markdown"><p>A character in <a href="https://en.wikipedia.org/wiki/UTF-8">UTF-8</a> can be anywhere from 1 to 4 bytes long. The bytes are 8 bits long and are subject to the following rules:</p>
<ul>
<li>For a <code>1</code>-byte character, the first bit is a <code>0</code>, followed by its unicode code.</li>
<li>For an <code>n</code>-byte character, the first <code>n</code> bits are all <code>1</code>s and the <code>n + 1</code> bit is <code>0</code>. This is followed by <code>n - 1</code> bytes in which the <code>2</code> most significant bits (that is, the leftmost <code>2</code>) are <code>10</code>.</li>
</ul>
<p>This is how the UTF-8 encoding would work:</p>
<pre><code>   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</code></pre>
<p>Given an array of integers representing the data, return <code>true</code> if it can be converted to a valid UTF-8 encoding, otherwise return <code>false</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>stream = [197, 130, 1]</code>, the output should be<br>
<code>streamValidation(stream) = true</code>.</p>
<p>The input stream, when converted from decimal to binary numbers, represents the following octet sequence: <code>11000101 10000010 00000001</code>. The first <code>2</code> bits are <code>1</code>s and the <code>3<sup>rd</sup></code> bit is <code>0</code>, meaning that this sequence is a valid UTF-8 encoding of a <code>2</code>-byte character followed by a <code>1</code>-byte character, making the answer <code>true</code>.</p>
</li>
<li>
<p>For <code>stream = [235, 140, 4]</code>, the output should be<br>
<code>streamValidation(stream) = false</code>.</p>
<p>The input stream, when converted from decimal to binary numbers, represents the following octet sequence: <code>11101011 10001100 00000100</code>. The first <code>3</code> bits are all <code>1</code>s and the <code>4<sup>th</sup></code> bit is <code>0</code>, meaning that this is a <code>3</code>-byte character. The next byte is a correct continuation byte since it starts with <code>10</code>. However, the second continuation byte is invalid because it does not start with <code>10</code>, making the answer <code>false</code>.</p>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.integer stream</strong></p>
<p>An array of integers.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ stream.length ≤ 1100</code>,<br>
<code>0 ≤ stream[i] ≤ 255</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p>Return <code>true</code> if the input array represents a valid UTF-8 encoding, otherwise return <code>false</code>.</p>
</li>
</ul>
</div>