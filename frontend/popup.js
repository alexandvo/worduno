chrome.runtime.sendMessage({ message: "getSelectedText" }, function (response) {
  if (response.selectedText) {
    if (response.selectedText.length > 500) {
      document.getElementById("loadingText").style.display = "none";
      document.getElementById("highlightedText").innerText = "Highlighted text is too long. Must be shorter than 500 characters.";
      return;
    } 
    var simplifiedText = "";
    fetch("https://worduno-backend.onrender.com/simplify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: response.selectedText }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("loadingText").style.display = "none";
        document.getElementById("highlightedText").innerText = data;
      })
      .catch((error) => console.error("Error:", error));
  } else {
    document.getElementById("loadingText").style.display = "none";
    document.getElementById("highlightedText").innerText = "No text highlighted.";
  }
});
