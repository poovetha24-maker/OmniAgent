const API_URL = "http://localhost:8000";

export async function sendChatMessage(message) {
  const response = await fetch(
    `${API_URL}/api/chat`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: message
      })
    }
  );

  if (!response.ok) {
    throw new Error("Failed to connect to backend");
  }

  return await response.json();
}

export async function checkHealth() {
  const response = await fetch(
    `${API_URL}/health`
  );

  if (!response.ok) {
    throw new Error("Backend is not running");
  }

  return await response.json();
}