Flexbox Layout

Flexbox where new in CSS3, this where to improve items' alignment, direction and oder in a container of dynamic or unknown size.

Flexbox is used for "one dimensional" layouts.
It displays items in either columns or rows, however row is default.

By defining a container as a flex container, you can use properties and values you couldn't access otherwise to position your content.

Using Flexbox

Display

.container {
     -  The class that we'll apply to a container(most likely a <div>)

    display: flex;
    - The display property, with the value "Flex"

    min-height: 100vh;
    - The minimum height of the container

    flex-direction: row;
    -The direction our content displays in
}

Flex-direction

flex-direction: row,
flex-direction: colum;
flex-direction: row-reverse;
flex-direction: column-reverse;

Reverse doesn't flip our content, it flips the whole axis!
flex-start swaps places with flex-end

flex Wrap

Wrap lets our content display in the direction we requested for as long as it can, but will break the line when necessary

Flex Flow

flex-direction: row;
flex-wrap:wrap;

These two lines can be condense into one line called flex-flow.

Flex-flow is the shorthand property for direction and wrap. The display stays the same however just makes the code smaller and more efficient.

flex-flow: row wrap;

Order

Order allows you to control where in the container the flex items using order.

order is used on the flex items, rather than the container. By default they all have order:0; so they will appear in the oder we write them in the HTML.

Flexbox give more control over the layout without having to change the original HTML

Justify Content

It is used to align the items along the main axis - horizontally if we're in a row, or vertically if we're in a column

justify-content:
center;
flex-start;
flex-end;
space-between;
space-around;
space-evenly;

Flexbox works out the locations and values of the spaces based on the amount of items and size of container.

Align Items

Align-items is used to align our items along the cross axis - vertically if we're in a row, or horizontally if we're in a column

