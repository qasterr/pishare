const chat_box = document.getElementById("chat-box");
const form = document.getElementById("form");
const inputField = document.getElementById("input-field");
const errorBox = document.getElementById("error-box");
const pageBottom = document.getElementById("page-bottom");

const socket = io.connect(`http://${document.domain}:${location.port}/chat`);

socket.on("connect", () => {
    socket.emit("joined", {});
});

socket.on("status", (message) => {
    addMessage(message["msg"], null);
});

socket.on("message", (message) => {
    addMessage(message["msg"], message["author"]);
});

/*
    Add a message to the chat.
    ! WARNING: Be careful to escape the HTML beforehand
*/
function addMessage(message, author = null) {
    if (author === null) {
        chat_box.innerHTML += `
        <div class="message">
            <p><i>${message}</i></p>
        </div>
        `.trim()
    } else {
        chat_box.innerHTML += `
        <div class="message">
            <p><b>${author}:</b> ${message}</p>
        </div>
        `.trim()
    }

    pageBottom.scrollIntoView();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    errorBox.innerText = "";

    const formData = new FormData(form);

    message = formData.get("message");

    console.log(message.length);

    if (message.length > 2000) {
        errorBox.innerText = "Message too long. Messages can only be 2000 characters long."
        return false;
    }

    socket.emit("text", {
        "msg": message
    });

    inputField.value = "";

    return false;
});
