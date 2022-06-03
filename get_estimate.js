/* Web-embedded script for providing moving cost estimates based on input parameters
03.06.22 */

const moveInput = [];
const moveDict = {      // TODO: build dictionary by drawing directly from user input fields in HTML
    numRooms: 0,        // 0 if not less than a room is being moved
    packing: false,
    assemble: false,
    numFlights: 0,
    mileage: 0.0,
    gas: 0.0,           // total gas price for travel
    travelTime: 0.0     // in hours
};

/*main execution goes here
Take out organizeInput and parseMove, just build dictionaries directly from HTML elements
Assign generateMovingEstimate result to the proper label to display estimate on website */


function generateMovingEstimate() {

    let locals;
    let jobHrs;
    let uhaul;

    if (moveDict.numRooms == 0) {
        locals = 2;
        jobHrs = 2;
        uhaul = 83;
    } else if (moveDict.numRooms == 1) {
        locals = 2;
        jobHrs = 3;
        uhaul = 94;
    } else if (moveDict.numRooms == 2) {
        locals = 2;
        jobHrs = 4;
        uhaul = 94;
    } else if (moveDict.numRooms == 3) {
        locals = 3;
        jobHrs = 6;
        uhaul = 103;
    } else if (moveDict.numRooms == 4) {
        locals = 4;
        jobHrs = 7;
        uhaul = 103;
    } else {throw ValueError("Number of bedrooms cannot be greater than 4"); }

    var packVar = moveDict.packing ? 2 : 0;
    var assembleVar = moveDict.assemble ? 0.25 : 0;
    var flightVar = moveDict.numFlights > 0 ? (moveDict.numFlights - 1) * 0.05 + 1 : 0; // Maybe throw an error if numFlights > 5?
    var extras = packVar + assembleVar + flightVar;

    var driving = uhaul + moveDict.mileage + moveDict.gas // TODO: abstract mileage and gas from the user, just use location/gas prices
    var labor = 45*locals;
    var totalHrs = jobHrs + moveDict.travelTime; // TODO: abstract travel time via google maps
    var laborTotal = labor*(totalHrs + extras);

    return laborTotal + driving
}

/* Retired functions
function organizeInput(input) {
// Separates all user input based on relevant type of service. Only moving is supported currently
    moveInput = input;
}

function parseMove() {
//Build moving dictionary
    moveDict.numRooms = moveInput[0];
    moveDict.packing = moveInput[1];
    moveDict.assemble = moveInput[2];
    moveDict.numFlights = moveInput[3];
    moveDict.mileage = moveInput[4];
    moveDict.gas = moveInput[5];
    moveDict.travelTime = moveInput[6];
}
*/