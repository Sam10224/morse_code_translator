// Wait for the DOM content to be loaded
document.addEventListener("DOMContentLoaded", function () {
    // Find the input text element
    var inputText = document.getElementById("inputText");
    var output = document.getElementById("output");

    // Attach input event listener to the input text field
    inputText.addEventListener("input", function () {
        translate(inputText.value.trim().toUpperCase(), output);
    });
});

// Function to handle translation
function translate(input, output) {
    if (input == "") {
        output.value = ""; // Clear the output if input is empty
        return;
    }
    if (input.match(/[.-]/)) {
        // Morse code to text translation
        fetch("/morse_to_text", {
            method: "POST",
            body: JSON.stringify({ morse_code: input }),
            headers: {
                "Content-type": "application/json"
            }
        })
            .then(response => response.json())
            .then(data => output.value = data.text.toLowerCase()) // Convert text to lowercase
            .catch(error => console.error("Error:", error));
    } else {
        // Text to Morse translation
        fetch("/text_to_morse", {
            method: "POST",
            body: JSON.stringify({ text: input }),
            headers: {
                "Content-Type": "application/json"
            }
        })
            .then(response => response.json())
            .then(data => output.value = data.morse_code.toLowerCase()) // Convert Morse code to lowercase
            .catch(error => console.error("Error:", error));
    }
}
