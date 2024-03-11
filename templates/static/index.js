const refuelsEl = document.getElementById("refuels");

fetch('/api/refuels')
.then(res => res.json())
.then(data => {
    data.forEach(refuel => {
        element = document.createElement("div");
        element.innerText = refuel.distance_km;
        refuelsEl.appendChild(element);
    });
});