 // Об'явлення об'єкта для збереження кількості натискань на кожному парфумі
 var clickCount = {};


 var perfumeNameInputG = form.querySelector("[name='perfum_name']");
 var perfumePriceInputG = form.querySelector("[name='perfum_price']");
//  const newElement = document.createElement('div');
//  newElement.innerHTML = '<h1 class="g"> perfumePriceInputG </h1>'

//  perfumePriceInputG.prepend('')

document.addEventListener("DOMContentLoaded", function () {
    // Додаємо слухача подій click до всіх елементів з класом "btn-buy"
    var buyButtons = document.querySelectorAll(".btn-buy");
    buyButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            // Відміна відправки форми
            event.preventDefault();

            // Отримуємо інформацію про парфум з атрибутів даних
            var perfumeId = button.closest("form").getAttribute("data-perfum-id");
            var form = document.querySelector("form[data-perfum-id='" + perfumeId + "']");

            // Перевірка, чи елемент знайдено
            if (form) {
                var perfumeNameInput = form.querySelector("[name='perfum_name']");
                var perfumePriceInput = form.querySelector("[name='perfum_price']");
                
                // Перевірка, чи input-елементи знайдено
                if (perfumeNameInput && perfumePriceInput) {
                    var perfumeName = perfumeNameInput.value;
                    var perfumePrice = perfumePriceInput.value;
                     // Збільшуємо лічильник для відповідного парфуму
                     clickCount[perfumeName] = clickCount[perfumeName] ? clickCount[perfumeName] + 1 : 1;

                    // Логуємо інформацію в консолі
                    console.log("Назва парфуму: " + perfumeName);
                    console.log("Ціна парфуму: " + perfumePrice + " грн");
                    console.log("Кількість натискань: " + clickCount[perfumeName]);
                } else {
                    console.error("Input елементи не знайдено");
                }
            } else {
                console.error("Form елемент не знайдено");
            }
        });
    });
});
