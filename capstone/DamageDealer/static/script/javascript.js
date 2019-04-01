document.getElementById("shipslist").style.display = 'none';
document.getElementById("squadlist").style.display = 'none';
document.getElementById("upgrdlist").style.display = 'none';
document.getElementById("objctlist").style.display = 'none';
document.getElementById("commanderlist").style.display = 'none';
document.getElementById("defenselist").style.display = 'none';
document.getElementById("experimentlist").style.display = 'none';
document.getElementById("fleetcommlist").style.display = 'none';
document.getElementById("fleetsupplist").style.display = 'none';
document.getElementById("ionlist").style.display = 'none';
document.getElementById("offenselist").style.display = 'none';
document.getElementById("officerlist").style.display = 'none';
document.getElementById("ordnancelist").style.display = 'none';
document.getElementById("supportlist").style.display = 'none';
document.getElementById("titlelist").style.display = 'none';
document.getElementById("turbolist").style.display = 'none';
document.getElementById("weapteamlist").style.display = 'none';
document.getElementById("boardlist").style.display = 'none';

function showHideShips() {
    let x = document.getElementById("shipslist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideUpgrades() {
    let x = document.getElementById("upgrdlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideCommander() {
    let x = document.getElementById("commanderlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideDefense() {
    let x = document.getElementById("defenselist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideExperimental() {
    let x = document.getElementById("experimentlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideFleetComm() {
    let x = document.getElementById("fleetcommlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideFleetSupp() {
    let x = document.getElementById("fleetsupplist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideIon() {
    let x = document.getElementById("ionlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideOffense() {
    let x = document.getElementById("offenselist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideOfficer() {
    let x = document.getElementById("officerlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideOrdnance() {
    let x = document.getElementById("ordnancelist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideSupport() {
    let x = document.getElementById("supportlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideTitle() {
    let x = document.getElementById("titlelist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideTurbo() {
    let x = document.getElementById("turbolist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideWeaponsTeam() {
    let x = document.getElementById("weapteamlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideBoarding() {
    let x = document.getElementById("boardlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideSquadrons() {
    let x = document.getElementById("squadlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

function showHideObjectives() {
    let x = document.getElementById("objctlist");
    if (x.style.display === 'none') {
        x.style.display = 'flex';
    } else {
        x.style.display = 'none';
    }
}

let these_cards = document.getElementsByClassName("card");
for (let i=0; i<these_cards.length; i++) {
    these_cards[i].addEventListener('click', function() {
        fetch('cardstoadd', {
            method: 'POST',    
            body: JSON.stringify({
                fleet: this_fleet,
                card: this.id,
                amount: 1
            })
        }).catch((err) => console.log(response))
        .then((response) => {
            console.log('Success!');
            console.log(response);
            console.log(this)
            if(this){
                this.style.cssText = "-webkit-filter: opacity(.2); filter: opacity(.2);"
            };
        })
    })
}




