// popup.js

document.getElementById('open-flask').addEventListener('click', function() {
    // Get the active tab's URL
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        const currentTabUrl = tabs[0].url;

        // Flask app URL with the current tab's URL passed as a query parameter
        const flaskAppUrl = 'http://127.0.0.1:5000/get_link/?url=' + encodeURIComponent(currentTabUrl);

        // Open a new tab with the Flask app, passing the current tab URL as a parameter
        chrome.tabs.create({ url: flaskAppUrl });
    });
});
