// popup.js

// Function to open the Flask app with the current tab's URL
function openFlaskWithUrl() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const currentTabUrl = tabs[0].url;
        const flaskAppUrl = 'http://127.0.0.1:5000/?url=' + encodeURIComponent(currentTabUrl);
        chrome.tabs.create({ url: flaskAppUrl });
    });
}

// Function to open the landing page
function goToHomePage() {
    chrome.tabs.create({ url: chrome.runtime.getURL('landing.html') });
}

// Add event listeners for both buttons
document.getElementById('extract-url').addEventListener('click', openFlaskWithUrl);
document.getElementById('go-home').addEventListener('click', goToHomePage);
