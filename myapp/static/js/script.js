
// ---------------------------------------------------------------------------js for the back button or close button ------------
function closeContent(contentId) {
    // Hide the specific hidden content
    var content = document.getElementById('content-' + contentId);
    if (content) {
        content.style.display = 'none';
    }
}
//-----------------------------------------------------------------------


// -----------------------------------------------------------------------------------js for the go to privous page ---------------
function showContent(contentId) {
  // Hide all hidden content
  var hiddenContents = document.querySelectorAll('.hidden-content');
  hiddenContents.forEach(function(content) {
      content.style.display = 'none';
  });

  // Show the hidden content corresponding to the clicked grid container card
  var content = document.getElementById('content-' + contentId);
  if (content) {
      content.style.display = 'block';
  }
}
// --------------------------------------------------------------------------------

//--------------------------------------------------------------------------------------- javascript for plus button ------------------------------------------------------------------------------------

// const plusButton = document.getElementById('plusButton');
// const minusButton = document.getElementById('minusButton');
// const numberDisplay = document.getElementById('numberDisplay');
// let number = 0;

// plusButton.addEventListener('click', () => {
// number++;
// updateNumberDisplay();
// plusButton.style.transform = 'scale(1.2)'; // Add a scale effect when clicked
// setTimeout(() => {
//   plusButton.style.transform = 'scale(1)'; // Reset scale after a short delay
// }, 100); // 100 milliseconds for fast transition
// });


// minusButton.addEventListener('click', () => {
//   if (number > 0) {
//     number--;
//     updateNumberDisplay();
//   }
// });

// function updateNumberDisplay() {
//   numberDisplay.textContent = number;
//   if (number > 0) {
//     numberDisplay.style.display = 'inline-block';
//     minusButton.style.display = 'flex';
//     plusButton.style.display = 'flex';
//   } else {
//     numberDisplay.style.display = 'none';
//     minusButton.style.display = 'none';
//     plusButton.style.display = 'flex';
//   }
// }//-----------------------------------------------------------------------------------------------------------------------------

// ------------------------------------------------------------- js for slide up transition 
// / const header = document.getElementById('header');
// const scrollMenu = document.getElementById('scrollmenu'); // Make sure this matches your HTML ID
// const container = document.getElementById('container');

// let lastScrollTop = 0;

// container.addEventListener('scroll', function() {
//   let scrollTop = container.scrollTop;
//   let scrollAmount = scrollTop - lastScrollTop;

//   // Determine the direction of scroll
//   if (scrollAmount > 0) {
//     // Scroll down
//     if (scrollTop > 50) {
//       header.style.top = '-66px'; // Slide up the header
//       scrollMenu.style.top = '0px'; // Slide up the menu
//       scrollMenu.classList.add('shadow'); // Add shadow class only when at the top
//     }
//   } else {
//     // Scroll up
//     header.style.top = '0'; // Slide down the header
//     scrollMenu.style.top = '66px'; // Slide down the menu
//     if (scrollTop === 0) {
//      scrollMenu.classList.remove('shadow'); // Remove shadow class
//     }
//   }
//   lastScrollTop = scrollTop;
// });
// // -------------------------------------------------------------------------------------------------------


// js for the slider highlighter animation 
{/* document.addEventListener('DOMContentLoaded', function() {
        const highlighter = document.querySelector('.highlighter');
        const menuItems = document.getElementById('scrollmenu');
        const cards = document.querySelectorAll('.card');
        let isFirstSelection = true; // Flag to track the first selection
    
        // Initialize highlighter position based on the active card
        moveHighlighter();
    
        // Add click event listeners to each card
        cards.forEach((card, index) => {
            card.addEventListener('click', function() {
                highlightMenuItem(index);
            });
        });
    
        // Function to highlight the active menu item
        function highlightMenuItem(index) {
            // Remove active class from all cards
            cards.forEach(card => {
                card.classList.remove('active');
            });
    
            // Add active class to the clicked card
            cards[index].classList.add('active');
    
            // Move the highlighter to the clicked card
            moveHighlighter();
        }
    
        // Function to move the highlighter to the active card
        function moveHighlighter() {
            const activeCard = document.querySelector('.card.active');
            const cardImg = activeCard.querySelector('img'); // Get the card image
            const cardImgRect = cardImg.getBoundingClientRect();
            const menuItemsRect = menuItems.getBoundingClientRect();
            const scrollLeft = menuItems.scrollLeft; // Get the scroll left position of the menu
            const highlighterLeft = cardImgRect.left - menuItemsRect.left + scrollLeft;
    
            // Move the highlighter to behind the card image with or without transition
            if (isFirstSelection) {
                isFirstSelection = false; // Set flag to false after the first selection
                highlighter.style.transition = 'none'; // Disable transition for the first selection
            } else {
                highlighter.style.transition = 'transform 0.6s ease'; // Enable transition for subsequent selections
            }
            highlighter.style.transform = `translateX(${highlighterLeft}px)`;
        }
    
        // Update highlighter position when the menu is scrolled
        menuItems.addEventListener('scroll', function() {
            moveHighlighter();
        });
    });
*/}