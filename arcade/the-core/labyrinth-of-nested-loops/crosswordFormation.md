<div class="markdown"><p>You're a crossword fanatic, and have finally decided to try and create your own. However, you also love symmetry and good design, so you come up with a set of rules they should follow:</p>
<ul>
<li>the crossword must contain exactly four words;</li>
<li>these four words should form four pairwise intersections;</li>
<li>all words must be written either left-to-right or top-to-bottom;</li>
<li>the area of the rectangle formed by empty cells inside the intersections isn't equal to zero.</li>
</ul>
<p>Given <code>4</code> words, find the number of ways to make a crossword following the above-described rules. Note that two crosswords which differ by rotation are considered different.</p>
<p><strong>Example</strong></p>
<p>For <code>words = ["crossword", "square", "formation", "something"]</code>, the output should be<br>
<code>crosswordFormation(words) = 6</code>.</p>
<p>The six crosswords can be formed as shown below:</p>
<pre><code>  f                         f                             f
  o                     c r o s s w o r d     c r o s s w o r d
c r o s s w o r d           r   o                   q     r
  m   q                     m   m                   u     m
  a   u            ;  s q u a r e          ;        a     a
  t   a                     t   t                   r     t
  i   r                     i   h             s o m e t h i n g
s o m e t h i n g           o   i                         o
  n                         n   n                         n
                                g                               
                                                              
    c         s               s                                      
f o r m a t i o n       c     q               c         s          
    o         m         r     u               r         o      
    s q u a r e       f o r m a t i o n       o         m            
    s         t    ;    s     r            ;  s q u a r e                  
    w         h         s o m e t i n g       s         t         
    o         i         w                     w         h     
    r         n         o                   f o r m a t i o n            
    d         g         r                     r         n         
                        d                     d         g             
</code></pre>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] array.string words</strong></p>
<p>An array of distinct strings, the words you need to use in your crossword.</p>
<p><em>Guaranteed constraints:</em><br>
<code>words.length = 4</code>,<br>
<code>3 ≤ words[i].length &lt; 15</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of ways to make a correct crossword of the desired formation.</p>
</li>
</ul>
</div>