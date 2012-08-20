pyHtml
======

This module is used to generate html using Python. Currently there is very
limited functionlaity being provided by this module. The functionality 
implemented so far can be summed up as :

* Creating an instance of the class will automatically create a file on the 
disk with the name passed to the pyhtml() function. If no name is passed, 
file with the name "My Web Page" will be created. Planning to make the 
filename compulsory because if the user doesn't pass any value to pyHtml() 
function for two instances, the resultant "My Web Page" file becomse a mess.

* The functions implemented are 
    - external\_css : Lets you provide an external CSS file to the html page.
    - internal\_css : Lets you create custom CSS for the html page.
    - a             : Lets you create an anchor tag.
    - hr            : Lets you generate a horizontal ruler bar.
    - printOut      : Lets you print the resulting html file.

* Usage : Import the pyHtml module in a script and use it as per the
documenation.

A lot of improvements need to be made to the code yet.
