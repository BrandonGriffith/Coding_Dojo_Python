// Initialize and add the map
function initMap() {
    // The location of Uluru
    lat1 = '{{location[0]}}';
    lng1 = '{{location[1]}}';
    const uluru = { lat: parseFloat(lat1), lng: parseFloat(lng1) };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    });
}
