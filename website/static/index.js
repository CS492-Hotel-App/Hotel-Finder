// function to delete hotel
function delete_hotel(hotelId) {
    fetch("/delete-hotel", {
        method: "POST",
        body: JSON.stringify({hotelId: hotelId}),
    }).then((_res) => {
        window.location.href = "/hotels";
    });
}


// function to send room id to booking 
function sendRoomToBooking(roomId) {
    var roomId = roomId
    var encodedRoomId = encodeURI(roomId)

    window.location.href="/booking?variable=" + encodedRoomId

}

function getRoomId() {
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString)

    var myVariable = urlParams.get('variable')

    alert(myVariable)
}

// function to remove booking from user's profile
function removeBooking(bookingId) {
    fetch("/remove-booking", {
        method: "POST",
        body: JSON.stringify({bookingId: bookingId}),
    }).then((_res) => {
        window.location.href="/profile"
    })
}