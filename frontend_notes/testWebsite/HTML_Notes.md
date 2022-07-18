HTML

HTML is short for Hyper Text Markup Language, it is used for coding the content of webpages. HTML has been around since the early 90s and it is still hugely important part of web development.

HTML is the structure of a webpage.

HTML on it own without the use of CSS and Javascript looks really horrible and there is no way of the user being able to interact with the page, this is where both CSS and JavaScript comes into making the website better. CSS is the design and JavaScript makes things on the website more user interactive.

HTML is constructed with lots of elements.

The HTML element is made up of the tagname some content and closing tagname.

Tags - it is the element that determine the type of content is displayed.

The HTML Template
<html> tells the browser that the content inside is Hyper Text Markup Language.
<head> this is all the important information for the HTML document, within the head this is where the css file is linked.
<body> it is everything you see on your webpage, all your images, texts and links.

Some basic elements
<p> elements represents a paragraph

<h1>, <h2>, <h3>, <h4>, <h5> & <h6> elements respresents heading. <h1> is the biggest heading and can only be used once on the page, however you can use as many as the other as you like on the page.

<img> element represent images

The alt attribute and why we use it?

It is a text description of the image, and it is displayed on the web page if the image can't be loaded or is broken.
Also it is very useful for accessibility as screen readers will read this description to the user so they know what the image is.

Links
<a> element represents links
target="_blank" tells the browser where to display the linked url also it will open the link in a new tab - all external links must have this attribute as it allows the user to remain on your web page too, without the target="_blank" you will stop users from coming back to your page

HTML Extras
<nav>
the nav tag defines a set of navigation links. Not all links should be inside a <nav> element, only use it for a major block of navigation links.

<header>
The header element typically contains one or more heading elements.
A logo or icon
Navigation links

<footer>
The footer element typically contains back to top links, contact information and copyright information

<pre>
The pre tag element represents preformatted text which is to be presented exactly as written in the HTML file.
It preserves text spaces, line breaks and tabs.
Displays in a fixed-width font but can be changed in CSS

<div> tag is an HTML element that contain segments of code, however it does nothing until is styled with CSS. It should be only used if there no other element is appropriate. It does work with the parent and child relationship and more so with Flexbox. If you have lots of <div>'s on the page you add id and or class to the div tag so you caan access it within css. You can only use one id per page, however class you can use as many as you like.

<span> tag is an inline container that allows you to group elements for styling, again it does nothing until it is styled with CSS.
Again only use the span tag when there is no other suitable element is appropriate. Also you can add id and or class with span tag.

What is the difference between <div> and <span>? <div> is a block-level as <span> is an inline element.

HTML Entities
They are characters reserved within HTML for example < and > may make your browser think they are tags. They allow you to display characters that would normally be used for other purposes, they can be accessed with either an entity name or an entity number.

non-breaking space - &nbsp; or &#160;
less than - &lt; or &#60;
greater than - &gt; or &#62;
ampersand - &amp; or &#38;
copyright - &copy; or &#169;
pound - &pound; or &#163;

More elements

<code> displays the contents in a style intended to indicate that the text is a fragment of computer code, it is displays text in monospace font.
Also can display multiple lines of code if wrapped within a <pre> element.

<kdb> displays the content to intended to indicate the text is a user input from a keyboard.

<em> tag will make the text italice, and making it of importance, it should be only used for text requires stress emphasis.
<i> should be used for text that is set off from the normal prose.
<cite> should be used for titles of works, such as books or movies.

<strong> tag will make your text bold whilst telling the browser that the text is of importance, either seriousness or urgency.
<b> tag should be used to draw attention to the text without indicating that it is important.