// popup.js

// Function to open the Flask app with the current tab's URL
function openFlaskWithUrl() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const currentTabUrl = tabs[0].url;
<<<<<<< HEAD

        // Flask app URL with the current tab's URL passed as a query parameter
        const flaskAppUrl = 'http://127.0.0.1:5000/get_link/?url=' + encodeURIComponent(currentTabUrl);

        // Open a new tab with the Flask app, passing the current tab URL as a parameter
=======
        const flaskAppUrl = 'http://127.0.0.1:5000/?url=' + encodeURIComponent(currentTabUrl);
>>>>>>> 2c63a842649bee1ce3acecb134f814a759ff6cb5
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
