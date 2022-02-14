var display = document.getElementById('displayLetter');

display.addEventListener("mouseenter", mOver,false);

display.addEventListener("mouseleave", mOut, false);

function mOver() {

    display.setAttribute("style", "color:grey;")
}

function mOut() {
    display.setAttribute("style", "color:transparent;")
}

const sound = {65:"http://carolinegabriel.com/demo/js-keyboard/sounds/040.wav",
    87:"http://carolinegabriel.com/demo/js-keyboard/sounds/041.wav",
    83:"http://carolinegabriel.com/demo/js-keyboard/sounds/042.wav",
    69:"http://carolinegabriel.com/demo/js-keyboard/sounds/043.wav",
    68:"http://carolinegabriel.com/demo/js-keyboard/sounds/044.wav",
    70:"http://carolinegabriel.com/demo/js-keyboard/sounds/045.wav",
    84:"http://carolinegabriel.com/demo/js-keyboard/sounds/046.wav",
    71:"http://carolinegabriel.com/demo/js-keyboard/sounds/047.wav",
    89:"http://carolinegabriel.com/demo/js-keyboard/sounds/048.wav",
    72:"http://carolinegabriel.com/demo/js-keyboard/sounds/049.wav",
    85:"http://carolinegabriel.com/demo/js-keyboard/sounds/050.wav",
    74:"http://carolinegabriel.com/demo/js-keyboard/sounds/051.wav",
    75:"http://carolinegabriel.com/demo/js-keyboard/sounds/052.wav",
    79:"http://carolinegabriel.com/demo/js-keyboard/sounds/053.wav",
    76:"http://carolinegabriel.com/demo/js-keyboard/sounds/054.wav",
    80:"http://carolinegabriel.com/demo/js-keyboard/sounds/055.wav",
    186:"http://carolinegabriel.com/demo/js-keyboard/sounds/056.wav"};


const AK = document.getElementById('A');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'a'){
        const a = new Audio(sound['65'])
        a.play();
        AK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            AK.classList.remove('WActive')
        })
    }
})

const SK = document.getElementById('S');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 's'){
        const a = new Audio(sound['83'])
        a.play();
        SK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            SK.classList.remove('WActive')
        })
    }
})

const DK = document.getElementById('D');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'd'){
        const a = new Audio(sound['68'])
        a.play();
        DK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            DK.classList.remove('WActive')
        })
    }
})

const FK = document.getElementById('F');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'f'){
        const a = new Audio(sound['70'])
        a.play();
        FK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            FK.classList.remove('WActive')
        })
    }
})

const GK = document.getElementById('G');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'g'){
        const a = new Audio(sound['71'])
        a.play();
        GK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            GK.classList.remove('WActive')
        })
    }
})

const HK = document.getElementById('H');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'h'){
        const a = new Audio(sound['72'])
        a.play();
        HK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            HK.classList.remove('WActive')
        })
    }
})

const JK = document.getElementById('J');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'j'){
        const a = new Audio(sound['74'])
        a.play();
        JK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            JK.classList.remove('WActive')
        })
    }
})

const KK = document.getElementById('K');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'k'){
        const a = new Audio(sound['75'])
        a.play();
        KK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            KK.classList.remove('WActive')
        })
    }
})

const LK = document.getElementById('L');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'l'){
        const a = new Audio(sound['76'])
        a.play();
        LK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            LK.classList.remove('WActive')
        })
    }
})

const signK = document.getElementById(';');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === ';'){
        const a = new Audio(sound['186'])
        a.play();
        signK.classList.add('WActive');
        document.addEventListener('keyup',() =>{
            signK.classList.remove('WActive')
        })
    }
})


const WK = document.getElementById('W');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'w'){
        const a = new Audio(sound['87'])
        a.play();
        WK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            WK.classList.remove('BActive')
        })
    }
})

const EK = document.getElementById('E');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'e'){
        const a = new Audio(sound['69'])
        a.play();
        EK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            EK.classList.remove('BActive')
        })
    }
})

const TK = document.getElementById('T');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 't'){
        const a = new Audio(sound['84'])
        a.play();
        TK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            TK.classList.remove('BActive')
        })
    }
})

const YK = document.getElementById('Y');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'y'){
        const a = new Audio(sound['89'])
        a.play();
        YK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            YK.classList.remove('BActive')
        })
    }
})

const UK = document.getElementById('U');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'u'){
        const a = new Audio(sound['85'])
        a.play();
        UK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            UK.classList.remove('BActive')
        })
    }
})

const OK = document.getElementById('O');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'o'){
        const a = new Audio(sound['79'])
        a.play();
        OK.classList.add('BActive');
        document.addEventListener('keyup',() =>{
            OK.classList.remove('BActive')
        })
    }
})

const PK = document.getElementById('P');
document.addEventListener('keydown', (event) =>{
    if (event.repeat) return
    if (event.key === 'p'){
        const a = new Audio(sound['80'])
        a.play();
        PK.classList.add('BActive');

        document.addEventListener('keyup',() =>{
            PK.classList.remove('BActive')
        })
    }
})



