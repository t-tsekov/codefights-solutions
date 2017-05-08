<div class="markdown"><p>You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different characters to represent pixels. Your current goal is to support <code>rectangle x1 y1 x2 y2</code> operation, which draws a rectangle that has an upper left corner at <code>(x1, y1)</code> and a lower right corner at <code>(x2, y2)</code>. Here the <code>x</code>-axis points from left to right, and the <code>y</code>-axis points from top to bottom.</p>
<p>Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the operation is applied. For the details about how rectangles are painted, see the example.</p>
<p><strong>Example</strong></p>
<p>For</p>
<pre><code>canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
</code></pre>
<p>and <code>rectangle = [1, 1, 4, 3]</code>, the output should be</p>
<pre><code>
drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                                    ['a', <b><font color="red">'*'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'*'</font></b>, 'a', 'a', 'a'],
                                    ['a', <b><font color="red">'|'</font></b>, 'a', 'a', <b><font color="red">'|'</font></b>, 'a', 'a', 'a'],
                                    ['b', <b><font color="red">'*'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'-'</font></b>, <b><font color="red">'*'</font></b>, 'b', 'b', 'b'],
                                    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
</code></pre>
<p>Note that rectangle sides are depicted as <code>-</code>s and <code>|</code>s, asterisks (<code>*</code>) stand for its corners and all of the other "pixels" remain the same. Color in the example is used only for illustration.</p>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.array.char canvas</strong></p>
<p>A non-empty rectangular matrix of characters.</p>
<p><em>Guaranteed constraints:</em><br>
<code>2 ≤ canvas.length ≤ 10</code>,<br>
<code>2 ≤ canvas[0].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.integer rectangle</strong></p>
<p>Array of four integers - <code>[x1, y1, x2, y2]</code>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>0 ≤ x1 &lt; x2 &lt; canvas[i].length</code>,<br>
<code>0 ≤ y1 &lt; y2 &lt; canvas.length</code>.</p>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
</li>
</ul>
</div>