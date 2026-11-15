document.getElementById("new-chat")
    .addEventListener("click", async function () {

        const response = await fetch("/new-chat/", {

            method: "POST",

            headers: {
                "X-CSRFToken": csrf
            }

        });

        const data = await response.json();

        if (!response.ok) {
            alert("Could not create a new chat.");
            return;
        }

        currentChatId = data.chat_id;

        clearMessages();

        const welcome = document.createElement("div");

        welcome.className = "welcome";

        welcome.innerHTML = `
        <h2>Welcome to Llama 🦙</h2>
        <p>What would you like to talk about today?</p>
    `;

        messages.appendChild(welcome);

        await loadChatList();

        input.focus();

    });