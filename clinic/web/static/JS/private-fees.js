const arrows = document.querySelectorAll('.arrow'); /*Creating a variable arrows that stores the NodeList by using 'document.querySelectorAll().'
                                                    The Nodelist selects all HTML elements that have the class 'arrow' */

arrows.forEach(arrow => { /*using the forEach() method to iterate through each element in the arrows NodeList */ 
    arrow.addEventListener('click', () => { /*adding a click event listener for each element with the class 'arrow'
                                            The defined function inside the event listener will be run if any element with the class 'arrow' is clicked.*/
        const next_arrow = arrow.nextElementSibling;/*Creating a next_arrow variable that selects the next sibling element (in the HTML structure) of the clicked 'arrow'*/
        arrow.classList.toggle('active');/*toggling the presence of the CSS class 'active' on the clicked 'arrow' element. 
                                        If the class is already present, it will be removed; otherwise, it will be added */
        next_arrow.classList.toggle('active'); /* toggling the presence of the CSS class 'active' on the next_arrow element (the next sibling of the clicked arrow). 
                                                If the class is already present, it will be removed; otherwise, it will be added */
    });
});