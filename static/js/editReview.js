console.log(1);
const editButtons = document.querySelectorAll('.edit-review-btn')
const reviewTextbox = document.getElementById('add-review');
const submitButton = document.getElementById('submit-review-btn');
console.log(editButtons)

let s;
for (const button of editButtons) {
    button.addEventListener('click', (e) => {
        let contentElement = document.getElementById(e.currentTarget.dataset.id).children[1]
        const reviewDetails = {
            id: e.currentTarget.dataset.id,
            content: contentElement.textContent
        }

        reviewTextbox.value = reviewDetails.content
        submitButton.textContent = "Save Review"
        console.log(reviewDetails)
    })
}