let lastBuy = null;
let lastSell = null;

async function updateGoldPrice() {

    try {

        const res = await fetch("/api/goldprice/");
        const data = await res.json();

        const buy = document.getElementById("gold-buy");
        const sell = document.getElementById("gold-sell");
        const update = document.getElementById("gold-update-time");

        if (buy) buy.innerText = data.buy;
        if (sell) sell.innerText = data.sell;

        if (update)
            update.innerText = data.update_date + " " + data.update_time;

    } catch (error) {

        console.log("Gold API Error");

    }

}

function updateWorldClock() {

    const el = document.getElementById("world-clock");

    if (!el) return;

    const now = new Date();

    const formatter = new Intl.DateTimeFormat("th-TH", {
        timeZone: "Asia/Bangkok",
        day: "numeric",
        month: "short",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    });

    el.innerText = formatter.format(now);

}


function startSystem() {

    updateGoldPrice();
    updateWorldClock();

    setInterval(updateGoldPrice, 10000); // อัปเดตราคาทองทุก 10 วิ
    setInterval(updateWorldClock, 1000); // นาฬิกาทุก 1 วิ

}

document.addEventListener("DOMContentLoaded", startSystem);