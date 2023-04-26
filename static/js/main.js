const roomBtn = document.getElementById("roomBtn");
const statusBtn = document.getElementById("statusBtn");
const roomBox = document.getElementById("roomBox");
const statusBox = document.getElementById("statusBox");

roomBtn.addEventListener("click", function() {
    if (roomBox.style.display === "block") {
        roomBox.style.display = "none";
    } else {
        roomBox.style.display = "block";
        statusBox.style.display = "none";
    }
});

statusBtn.addEventListener("click", function() {
    if (statusBox.style.display === "block") {
        statusBox.style.display = "none";
    } else {
        statusBox.style.display = "block";
        roomBox.style.display = "none";
    }
});