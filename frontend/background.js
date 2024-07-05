chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "getSelectedText") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      let activeTab = tabs[0];
      let url = activeTab.url;

      if (
        url.startsWith("chrome://") ||
        url.startsWith("chrome-extension://")
      ) {
        sendResponse({ selectedText: null });
        return;
      }
      chrome.scripting.executeScript(
        {
          target: { tabId: activeTab.id },
          function: () => window.getSelection().toString(),
        },
        (results) => {
          sendResponse({ selectedText: results[0].result });
        }
      );
    });
    // Required to use sendResponse asynchronously
    return true;
  }
});
