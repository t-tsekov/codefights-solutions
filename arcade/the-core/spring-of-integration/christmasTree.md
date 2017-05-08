<div class="markdown"><p>It's Christmas time! To share his Christmas spirit with all his friends, the young Christmas Elf decided to send each of them a Christmas e-mail with a nice Christmas tree. Unfortunately, Internet traffic is very expensive in the North Pole, so instead of sending an actual image he got creative and drew the tree using nothing but asterisks (<code>'*'</code> symbols). He has given you the specs (see below) and your task is to write a program that will generate trees following the spec and some initial parameters.</p>
<p>Here is a formal definition of how the tree should be built, but before you read it the Elf <strong>HIGHLY</strong> recommends first looking at the examples that follow:</p>
<ul>
<li>
<p>Each tree has a <em>crown</em> as follows:</p>
<pre><code> *
 *
***
</code></pre>
</li>
<li>
<p>Define a <em>line</em> as a horizontal group of asterisks and a <em>level</em> as a collection of <code>levelHeight</code> <em>lines</em> stacked one on top of the other.</p>
</li>
<li>
<p>Below the <em>crown</em> there are <code>levelNum</code> <em>levels</em>.</p>
</li>
<li>
<p>The tree is perfectly symmetrical so all the middle asterisks of the <em>lines</em> lie on the center of the tree.</p>
</li>
<li>
<p>Each <em>line</em> of the same <em>level</em> (excluding the first one) has two more asterisks than the previous one (one added to each end);</p>
</li>
<li>
<p>The number of asterisks in the first line of each <em>level</em> is chosen as follows:</p>
<ul>
<li>the first line of the first level has <code>5</code> asterisks;</li>
<li>the first line of each consecutive <em>level</em> contains two more asterisks than the first line of the previous <em>level</em>.</li>
</ul>
</li>
<li>
<p>And finally there is the tree foot which has a height of <code>levelNum</code> and a width of:</p>
<ul>
<li><code>levelHeight</code> asterisks if <code>levelHeight</code> is odd;</li>
<li><code>levelHeight + 1</code> asterisks if <code>levelHeight</code> is even.</li>
</ul>
</li>
</ul>
<p>Given <code>levelNum</code> and <code>levelHeight</code>, return the Christmas tree of the young elf.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>levelNum = 1</code> and <code>levelHeight = 3</code>, the output should be</p>
<pre><code>christmasTree(levelNum, levelHeight) =
    ["    *",
     "    *",
     "   ***",
     "  *****",
     " *******",
     "*********",
     "   ***"]
</code></pre>
<p>, which represents the following tree:</p>
<pre><code>            ___
      *        |
      *        |-- the crown      
     ***    ___|       
    *****      |
   *******     |-- level 1
  ********* ___|
     ***    ___|-- the foot
</code></pre>
</li>
<li>
<p>For <code>levelNum = 2</code> and <code>levelHeight = 4</code>, the output should be</p>
<pre><code>christmasTree(levelNum, levelHeight) = 
    ["      *", 
     "      *", 
     "     ***", 
     "    *****", 
     "   *******", 
     "  *********", 
     " ***********", 
     "   *******", 
     "  *********", 
     " ***********", 
     "*************", 
     "    *****", 
     "    *****"]
</code></pre>
<p>, which represents the following tree:</p>
<pre><code>                ___ 
        *          |
        *          | -- the crown
       ***      ___|
      *****        |
     *******       | -- level 1
    *********      |
   ***********  ___|
     *******       |
    *********      | -- level 2
   ***********     |
  ************* ___|
      *****        | -- the foot
      *****     ___|
</code></pre>
</li>
</ul>
<p><strong>Input/Output</strong></p>
<ul>
<li><strong>[time limit] 4000ms (py3)</strong></li>
</ul>
<ul>
<li>
<p><strong>[input] integer levelNum</strong></p>
<p>A positive integer, the number of <em>levels</em>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>1 ≤ levelNum ≤ 8</code>.</p>
</li>
<li>
<p><strong>[input] integer levelHeight</strong></p>
<p>The number of <em>lines</em> in each <em>level</em>.</p>
<p><em>Guaranteed constraints:</em><br>
<code>3 ≤ levelHeight ≤ 8</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>The Christmas tree according to the specs and inputs. Output elements should not contain trailing whitespaces, and at least one of them should start with the <code>'*'</code> symbol.</p>
</li>
</ul>
</div>