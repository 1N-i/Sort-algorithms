let renderIsRunning = false

const algoBtns = document.querySelectorAll(".algo-btn");
algoBtns.forEach(btn => {
    btn.addEventListener("click", renderAlgo);
});

function renderAlgo(event) {
    if (renderIsRunning) {
        alert("Be sure to close the other algorithm first to see another one")
        return
    } else {
        renderIsRunning = true
    }
    const nameAlgo = event.currentTarget.dataset.algo
    data = getData()

    if (data.size > 800) {
        alert("Algorithms animations will only work with lists with a maximum size of 800 but the benchmark works normally")
        renderIsRunning = false
        return
    }

    const payload = {
        algo: nameAlgo,
        size: data.size,
        allowNegative: data.allowNegative,
        dataType: data.dataType,
        speed: data.speed
    };
    sendData(payload)
}

const benchmarkBtn = document.getElementById("benchmark-btn");
benchmarkBtn.addEventListener("click", renderBenchmark);

function renderBenchmark() {
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

function displayBenchmark(results) {
    const container = document.getElementById("benchmark-results");
    let result = `
        <table>
            <thead>
                <tr>
                    <th>Algorithms</th>
                    <th>Time (ms)</th>
                </tr>
            </thead>
            <tbody>
    `;

    for (const [algo, time] of Object.entries(results)) {
        result += `
            <tr>
                <td>${algo}</td>
                <td>${time} ms</td>
            </tr>
        `;
    }

    result += `</tbody></table>`;
    container.innerHTML = result;
}

function getData() {
    return {
        size: Number(document.getElementById("size").value),
        allowNegative: document.getElementById("allow-negatives").checked,
        dataType: document.getElementById("data-style").value,
        speed: document.getElementById("speed-control").value
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
    .then(data => (link == "/api/render") ? console.log("Return: ", data) : displayBenchmark(data))
    .finally(() => {renderIsRunning = false})
    .catch(error => console.error("Error:", error));
}

const speedControl = document.getElementById('speed-control');
const speedValue = document.getElementById('speed-value');

speedControl.addEventListener('input', (event) => {
    speedValue.textContent = event.target.value;
});