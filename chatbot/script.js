async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    
    if (message === '') return;
    
    // User ka message UI mein dikhao
    addMessage(message, 'user-message');
    input.value = '';
    
    try {
        // Python backend ko message bhejo
        const response = await fetch('https://chatbot-r4z2.onrender.com', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        addMessage(data.reply, 'bot-message');
    } catch (error) {
        addMessage('Kya mc error aa gaya: ' + error.message, 'bot-message');
    }
}

function addMessage(text, className) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', className);
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
    
    // Auto scroll to bottom
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Enter key se bhi message bhejna
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
