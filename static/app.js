// Typhoon Roasters AI Service — Frontend Logic

const chatArea = document.getElementById("chatArea");
const welcomeMessage = document.getElementById("welcomeMessage");
const welcomeText = document.getElementById("welcomeText");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const sourcesBar = document.getElementById("sourcesBar");
const sourcesList = document.getElementById("sourcesList");

let currentMode = "engineer";
let chatHistory = [];
let isLoading = false;

// --- Mode Toggle ---
const modeDescriptions = {
    engineer: "Engineer mode: detailed diagnostics with case references, procedures, and manual citations.",
    client: "Client mode: simple troubleshooting steps and guidance on when to contact support.",
};

document.querySelectorAll(".mode-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        if (isLoading) return;
        document.querySelectorAll(".mode-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        currentMode = btn.dataset.mode;
        welcomeText.textContent = modeDescriptions[currentMode];
    });
});

// --- Quick Questions ---
document.querySelectorAll(".quick-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        if (isLoading) return;
        messageInput.value = btn.dataset.question;
        sendMessage();
    });
});

// --- Input Handling ---
messageInput.addEventListener("input", () => {
    sendBtn.disabled = messageInput.value.trim() === "";
    // Auto-resize textarea
    messageInput.style.height = "auto";
    messageInput.style.height = Math.min(messageInput.scrollHeight, 150) + "px";
});

messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (!sendBtn.disabled && !isLoading) sendMessage();
    }
});

sendBtn.addEventListener("click", () => {
    if (!isLoading) sendMessage();
});

// --- Chat Logic ---
async function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    // Hide welcome, show user message
    welcomeMessage.style.display = "none";
    appendMessage("user", text);
    chatHistory.push({ role: "user", content: text });

    // Clear input
    messageInput.value = "";
    messageInput.style.height = "auto";
    sendBtn.disabled = true;

    // Show typing indicator
    isLoading = true;
    const typingEl = showTyping();

    try {
        const res = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: text,
                mode: currentMode,
                history: chatHistory.slice(-10),
            }),
        });

        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: "Server error" }));
            throw new Error(err.detail || `HTTP ${res.status}`);
        }

        const data = await res.json();

        // Remove typing indicator and show response
        typingEl.remove();
        appendMessage("assistant", data.response);
        chatHistory.push({ role: "assistant", content: data.response });

        // Show sources
        showSources(data.sources || []);
    } catch (err) {
        typingEl.remove();
        appendMessage("assistant", `**Error:** ${err.message}\n\nPlease check that the server is running and the API key is configured.`);
    } finally {
        isLoading = false;
    }
}

function appendMessage(role, content) {
    const div = document.createElement("div");
    div.className = `message ${role}`;

    const roleLabel = document.createElement("div");
    roleLabel.className = `message-role ${role}`;
    roleLabel.textContent = role === "user" ? "You" : "Typhoon AI";

    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";
    contentDiv.innerHTML = role === "assistant" ? marked.parse(content) : escapeHtml(content);

    div.appendChild(roleLabel);
    div.appendChild(contentDiv);
    chatArea.appendChild(div);
    chatArea.scrollTop = chatArea.scrollHeight;
}

function showTyping() {
    const div = document.createElement("div");
    div.className = "message assistant";

    const roleLabel = document.createElement("div");
    roleLabel.className = "message-role assistant";
    roleLabel.textContent = "Typhoon AI";

    const typing = document.createElement("div");
    typing.className = "typing-indicator";
    typing.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';

    div.appendChild(roleLabel);
    div.appendChild(typing);
    chatArea.appendChild(div);
    chatArea.scrollTop = chatArea.scrollHeight;
    return div;
}

function showSources(sources) {
    if (!sources.length) {
        sourcesBar.style.display = "none";
        return;
    }
    sourcesBar.style.display = "flex";
    sourcesList.innerHTML = sources
        .map((s) => `<span class="source-chip">${s}</span>`)
        .join("");
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}
