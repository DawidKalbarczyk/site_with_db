const getE = document.getElementById.bind(document);

getE("postButton").addEventListener("click", function() {
    const inputValue = getE("postInput").value;
    alert("Post button clicked with input: " + inputValue);
    // Here you can add code to send the inputValue to your backend API
});

getE("getButton").addEventListener("click", function() {
    const inputValue = getE("getInput").value;
    alert("Get button clicked with input: " + inputValue);
    // Here you can add code to send the inputValue to your backend API
});

