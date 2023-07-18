function submitForm() {
    document.getElementById('donation-form').submit();
}

function goToStep(step) {
    document.querySelectorAll('[data-step]').forEach(function (element) {
        element.style.display = 'none';
    });

    document.querySelector('[data-step="' + step + '"]').style.display = 'block';
}

function confirmDonation() {
    // Get the form values
    let quantity = document.querySelector('input[name="quantity"]').value;
    let institution = document.querySelector('input[name="institution"]:checked').parentNode.querySelector('.title').innerText;
    let address = document.querySelector('input[name="address"]').value;
    let city = document.querySelector('input[name="city"]').value;
    let zipCode = document.querySelector('input[name="zip_code"]').value;
    let phoneNumber = document.querySelector('input[name="phone_number"]').value;
    let pickUpDate = document.querySelector('input[name="pick_up_date"]').value;
    let pickUpTime = document.querySelector('input[name="pick_up_time"]').value;
    let pickUpComment = document.querySelector('textarea[name="pick_up_comment"]').value;

    // Set the summary values
    document.getElementById('summary-quantity').innerText = quantity + ' worki';
    document.getElementById('summary-institution').innerText = 'Dla fundacji "' + institution;
    document.getElementById('summary-address').innerText = 'Ulica: ' + address;
    document.getElementById('summary-city').innerText = 'Miasto: ' + city;
    document.getElementById('summary-zip-code').innerText = 'Kod pocztowy: ' + zipCode;
    document.getElementById('summary-phone-number').innerText = 'Numer telefonu: ' + phoneNumber;
    document.getElementById('summary-pick-up-date').innerText = 'Data: ' + pickUpDate;
    document.getElementById('summary-pick-up-time').innerText = 'Godzina: ' + pickUpTime;
    document.getElementById('summary-pick-up-comment').innerText = 'Uwagi dla kuriera: ' + pickUpComment;

    // Show the summary step
    goToStep(5);
}