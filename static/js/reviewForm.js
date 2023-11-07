const button = document.getElementById("toggle-review");
const formContainer = document.getElementById("reviewForm");

const hideForm = (element) => {
	element.style.display = "none";
};

const showForm = (element) => {
	element.style.display = "block";
};

// Toggles the element's display, while also updating the session storage about it's current state.
const toggleElement = (element) => {
	elementStatus = element.dataset.status;

	if (elementStatus == "true") {
		sessionStorage.setItem("review_form_status", "false");
		element.dataset.status = "false";
		hideForm(formContainer);
	} else {
		sessionStorage.setItem("review_form_status", "true");
		element.dataset.status = "true";
		showForm(formContainer);
	}
};

// Toggles between showing and hiding the form element.
button.addEventListener("click", (e) => {
	toggleElement(formContainer);
});

// Validation. Makes sure that the text box has more than 12 characters, else it won't submit the form.
formContainer.addEventListener("submit", (e) => {
	e.preventDefault();
	form = formContainer.getElementsByTagName("textarea")[0];

	if (form.value.length > 12) {
		formContainer.getElementsByTagName("p")[0].innerText = "";
		formContainer.getElementsByTagName("form")[0].submit();
	} else {
		formContainer.getElementsByTagName("p")[0].innerText =
			"You can't submit a review with less than 12 characters.";
	}
});

// Deciding whether to have the form opened, or closed when the page opens up based on the session storage.
document.addEventListener("DOMContentLoaded", () => {
	currentStatus = sessionStorage.getItem("review_form_status");
	if (currentStatus && currentStatus == "true") {
		formContainer.dataset.status = "true";
		showForm(formContainer);
	} else if (currentStatus && currentStatus == "false")
		hideForm(formContainer);
});
