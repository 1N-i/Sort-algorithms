const algoBtns = document.querySelectorAll(".algo-btn");
algoBtns.forEach(btn => {
    btn.addEventListener("click", renderAlgo);
});

function renderAlgo(event) {
    const nameAlgo = event.currentTarget.dataset.algo
    const dataSize = document.getElementById("size").value
    const allowNegative = document.getElementById("allow-negatives").checked
    const dataType = document.getElementById("data-style").value

    const payload = {
        algo: nameAlgo,
        size: Number(dataSize),
        allowNegative: allowNegative,
        dataType: dataType
    };

    console.log(payload)
}

const benchmarkBtn = document.getElementById("benchmark-btn");
benchmarkBtn.addEventListener("click", renderBenchmark);

function renderBenchmark(event) {
    const nameAlgo = "benchmark"
    const dataSize = document.getElementById("size").value
    const allowNegative = document.getElementById("allow-negatives").checked
    const dataType = document.getElementById("data-style").value

    const payload = {
        algo: nameAlgo,
        size: Number(dataSize),
        allowNegative: allowNegative,
        dataType: dataType
    };

    console.log(payload)
}