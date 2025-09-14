document.getElementById("askBtn").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const status = document.getElementById("status");
  const responseBox = document.getElementById("responseBox");

  status.textContent = "⏳ Thinking...";
  responseBox.textContent = "";

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const url = new URL(tab.url);
  const videoId = url.searchParams.get("v");

  if (!videoId) {
    status.textContent = "❌ Not a valid YouTube video.";
    return;
  }

  try {
    const res = await fetch("http://localhost:8000/api/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_id: videoId, question })
    });

    const data = await res.json();
    responseBox.textContent = "💡 " + data.answer;
    status.textContent = "✅ Answer ready.";
  } catch (err) {
    status.textContent = "⚠️ Error fetching answer.";
    console.error(err);
  }
});
