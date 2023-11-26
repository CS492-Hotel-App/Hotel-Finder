// function to delete hotel
function delete_hotel(hotelId) {
    fetch("/delete-hotel", {
        method: "POST",
        body: JSON.stringify({hotelId: hotelId}),
    }).then((_res) => {
        window.location.href = "/hotels";
    });
}