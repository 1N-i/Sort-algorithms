function getData() {
    return {
        size: Number(document.getElementById("size").value),
        allowNegative: document.getElementById("allow-negatives").checked,
        dataType: document.getElementById("data-style").value
    };
}

function sendData(payload) {
    let link = "/api/render"
    if (payload.algo === "benchmark") {
        link = "/api/benchmark"
    }

    fetch(link, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log("Return: ", data))
    .catch(error => console.error("Error:", error));
}

const algoBtns = document.querySelectorAll(".algo-btn");
algoBtns.forEach(btn => {
    btn.addEventListener("click", renderAlgo);
});

function renderAlgo(event) {
    const nameAlgo = event.currentTarget.dataset.algo
    data = getData()

    const payload = {
        algo: nameAlgo,
        size: data.size,
        allowNegative: data.allowNegative,
        dataType: data.dataType
    };
    sendData(payload)
}

const benchmarkBtn = document.getElementById("benchmark-btn");
benchmarkBtn.addEventListener("click", renderBenchmark);

function renderBenchmark(event) {
    const nameAlgo = "benchmark"
    data = getData()

    const payload = {
        algo: nameAlgo,
        size: data.size,
        allowNegative: data.allowNegative,
        dataType: data.dataType
    };
    sendData(payload)
}