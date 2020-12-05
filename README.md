# Rich-Text-Analyser
<p align="center">
<img src="https://github.com/amispam/Rich-Text-Analyser/raw/main/IMG/8cd8232b-e956-465f-a33f-cd2995e8fe4d_200x200.png" alt="avatar" height="150" width="150"><br/>
This repository is built for the purpose of analysing text.</p>


[Run a demo](https://repl.it/@Rohit199/RichTextAnalyser?lite=true&outputonly=1)


<h2>Block content</h2>
<table><th>#</th><th>Blocks</th><th>purpose</th>
<tr>
<td>1</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/tree/main/main%20block">Main Block</a></td><td>

`Running programme`

</td>
</tr>
<tr>
 <td>2</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/tree/main/BlockChain">Block chain</a></td><td>

`Contains block files`

</td>
  </tr>
<tr>
<td>3</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/tree/main/Resources">Resources</a></td><td>

`Contains sample text`

</td></tr>
</table>
<h1>Block chain content</h1>
<table>
<th>#</th><th>Block chain</th><th>purpose</th>
<tr><td>1</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/absAndLine.py">Absolute and line</a></td><td>To return absolute value, and to return points of line.</td></tr>
<tr><td>2</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/arrange.py">Arrange</a></td><td>Standardising data</td></tr>
<tr><td>3</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/extract.py">Extract</a></td><td>Extracting content from an array</td></tr>
<tr><td>4</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/finder.py">Finder</a></td><td>Reading and analysing data</td></tr>
<tr><td>5</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/linearFitting.py">Linear fitting</a></td><td>Finding best linear fit for analysed data</td></tr>
<tr><td>6</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/mapper.py">Mapper</a></td><td>To map different arrays</td></tr>
<tr><td>7</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/minMax.py">MinMax</a></td><td>To return minimum or maximum</td></tr>
<tr><td>8</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/splitJoin.py">SplitJoin</a></td><td>To split string or to join array items</td></tr>
<tr><td>9</td><td><a href="https://github.com/amispam/Rich-Text-Analyser/blob/main/BlockChain/swap.py">Swap</a></td><td>Interchanging positions</td></tr>
</table>


## `finder` and it's arguments

> `finder(file.txt,argument 1, argument 2)` is central pillar of text analyzer, which is responsible for reading and analysing data.

Where `argument1` can take two values, one is `rCount` which is responsible for giving repetition count.
Second is `iCount` which is responsible for giving index count, **keep in mind that finder is receiving standardised text from `arrange` function.**
Now `argument2` which is actually third argument of `finder`, can also take two values. One is `0` other is `1` .
You can manage your output using `argument2` .
