function inicianMap(){
    var coord = {lat: -33.4402862 ,lng:-70.6712917};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
      });

}