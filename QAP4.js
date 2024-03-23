const motelCustomer = {

    firstname:"Bella",
    lastname:"Hop",
    gender:"Female",
    birthdate:"01-23-1998",
    currentyear: "2024",
    phone:"709-668-7325",

    mailing: {
        postal:"A1B23C",
        address:"101 Unreal Avenue",
        city:"St. John's",
        province:"Newfoundland & Labrador",
    },
    checks: {
        checkin:"03-02-2024",
        checkout:"03-08-2024",

    },

}

    var outt = motelCustomer.checks.checkout.slice(3,5)
    var inn = motelCustomer.checks.checkin.slice(3,5)

    var outt2 = motelCustomer.checks.checkout.slice(0,2)
    var inn2 = motelCustomer.checks.checkin.slice(0,2)


    var age = Math.abs(motelCustomer.currentyear - motelCustomer.birthdate.slice(6,10));

    var time = Math.abs(outt - inn)
    var timemon = Math.abs(outt2 - inn2)


    const rooms = [105, 106, 107, 108]

console.log(`${motelCustomer.checks.checkout.slice(0,2)}`)

console.log(`The customer's name is ${motelCustomer.firstname} ${motelCustomer.lastname}. They were born in ${motelCustomer.birthdate}, they are ${age} years old and they are ${motelCustomer.gender}.`)
console.log(`${motelCustomer.firstname}'s address is ${motelCustomer.mailing.address}, ${motelCustomer.mailing.city}, ${motelCustomer.mailing.province}, PO Box ${motelCustomer.mailing.postal}.`)
console.log(`Their check-in date will be ${motelCustomer.checks.checkin} and their check-out date will be ${motelCustomer.checks.checkout}.`)
console.log(`Their preferred rooms are listed as: ${rooms}. They are staying for ${time} days and ${timemon} months.`)