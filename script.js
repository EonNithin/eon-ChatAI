
function sendMessage() {
    var userInput = document.getElementById("user-input");
    var message = userInput.value;

    if (message.trim() !== "") {
        appendMessage("You: " + message, true);
        userInput.value = "";

        // Send the message to the chatbot backend or API for processing
        sendToChatbot(message);
    }
}

// Event listener for the "Enter" key press in the input field
document.getElementById("user-input").addEventListener("keydown", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    sendMessage();
  }
});

function autoResize(textarea) {
    textarea.style.height = "auto"; // Reset height to auto
    textarea.style.height = textarea.scrollHeight + "px"; // Set height based on scrollHeight
}

function appendMessage(message, isUserMessage) {
    var chatLog = document.getElementById("chat-log");
    var messageNode = document.createElement("div");
    messageNode.textContent = message;

    // Add CSS classes based on the message type
    messageNode.classList.add("message");
    if (isUserMessage) {
        messageNode.classList.add("user-message");
        //messageNode.style.backgroundColor = "#000";
    } else {
        messageNode.classList.add("bot-message");
        //messageNode.style.backgroundColor = "#f2f2f2";
    }

    chatLog.appendChild(messageNode);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function sendToChatbot(message) {
    fetch('/api/endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        handleBackendResponse(data);
    })
    .catch(error => {
        // Handle any errors that occurred during the request
        console.error('Error:', error);
    });
    
    setTimeout(function() {
        var response = "This is a sample response from the chatbot.";
        appendMessage("Eon: " + response);
    }, 500);
}
