async function makePrediction() {
    const inputValue = document.getElementById("userInput").value;

    if (!inputValue.trim()) {
        alert("Please enter something!");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ input: inputValue })
        });

        const data = await response.json();

        document.getElementById("resultText").textContent = data.prediction.output;
        document.getElementById("confidence").textContent = data.prediction.confidence;

        document.getElementById("resultBox").classList.remove("hidden");

    } catch (error) {
        alert("Error connecting to AI Service.");
        console.error(error);
    }
}