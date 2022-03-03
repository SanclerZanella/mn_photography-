element = $('input[name="date"]');
element.attr( 'type', 'date' );
type = element.attr('type');

var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0]
});
