function simulateOrderStatus() {
    const orderId = document.getElementById('order-id').value;
    if (!orderId) {
        alert("Please enter an Order ID");
        return;
    }

    const simulatedData = {
        order_id: orderId,
        status: "In Transit",
        estimated_delivery: "2023-11-15",
        current_location: "Warehouse #3, San Francisco",
    };

    displayOrderStatus(simulatedData);
}

function displayOrderStatus(data) {
    const orderDetails = document.getElementById('order-details');
    orderDetails.innerHTML = `
        <h3>Order ID: ${data.order_id}</h3>
        <p>Status: ${data.status}</p>
        <p>Estimated Delivery: ${data.estimated_delivery}</p>
        <p>Current Location: ${data.current_location}</p>
    `;

    document.getElementById('location').textContent = data.current_location;
}

function initSimulatedMap() {
    const locations = [
        "Warehouse #1, New York",
        "Warehouse #2, Chicago",
        "Warehouse #3, San Francisco",
        "Port #4, Los Angeles",
        "Port #5, Seattle"
    ];

    let index = 0;

    setInterval(() => {
        document.getElementById('location').textContent = locations[index];
        index = (index + 1) % locations.length;
    }, 3000);
}

function displayOrderTracking(orderId) {
    const trackingData = [
        { status: "Order Received", timestamp: "2023-10-01 08:30:00" },
        { status: "Processing", timestamp: "2023-10-01 09:00:00" },
        { status: "Shipped", timestamp: "2023-10-01 15:00:00" },
        { status: "In Transit", timestamp: "2023-10-02 09:30:00" },
        { status: "Delivered", timestamp: "2023-10-03 12:00:00" }
    ];

    const orderDetails = document.getElementById('order-details');
    orderDetails.innerHTML = `<h3>Order ID: ${orderId}</h3>`;

    trackingData.forEach(record => {
        const recordElement = document.createElement("p");
        recordElement.textContent = `${record.timestamp} - ${record.status}`;
        orderDetails.appendChild(recordElement);
    });
}

window.onload = function() {
    initSimulatedMap();
};
