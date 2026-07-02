function updateTime() {
    const now = new Date();
    document.getElementById("time").innerHTML = now.toLocaleString();
}

setInterval(updateTime, 1000);
updateTime();

async function getStatus() {
    try {
        const response = await fetch("http://localhost:5000/api");
        const data = await response.json();

        document.getElementById("status").innerHTML =
            `<strong>Status:</strong> ${data.status}<br>
             <strong>Version:</strong> ${data.version}<br>
             <strong>Server Time:</strong> ${data.server_time}`;
    } catch (error) {
        document.getElementById("status").innerHTML =
            "Backend is not running.";
    }
}