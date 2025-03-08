<template>
  <div class="main_page">
    <form @submit.prevent="sendForm()" class="main_page__form">
      <h1 class="main_page__title">Заполнить заявку</h1>
      <div class="main_page__input_container ic">
        <input v-model="first_name" required id="first_name" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="first_name">Имя</label>
      </div>
      <div class="main_page__input_container ic">
        <input v-model="last_name" required id="last_name" type="text" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="last_name">Фамилия</label>
      </div>
      <div class="main_page__input_container ic">
        <input v-model="email" required id="email" type="email" class="ic__input" placeholder=" ">
        <label class="main_page__placeholder" for="email">Email</label>
      </div>
      <div class="main_page__input_container ic">
        <input
          :value="phoneDisplay"
          @input="formatPhoneNumber"
          @keydown.delete="handlePhoneDelete"
          required
          id="phone_number"
          type="tel"
          class="ic__input"
          placeholder=" "
        >
        <label class="main_page__placeholder" for="phone_number">Номер телефона</label>
      </div>
      <button class="main_page__submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Отправка...' : 'Отправить' }}
      </button>
    </form>
  </div>
</template>
<script setup>
import {ref} from 'vue'

const first_name = ref('');
const last_name = ref('');
const email = ref('');
const isSubmitting = ref(false);
const phone_number = ref('')
const phoneDisplay = ref('+7 (')
const cursorPosition = ref(4)

function formatPhoneNumber(e) {
  const input = e.target.value
    .replace(/\D/g, '')
    .substring(1)
    .substring(0, 10)

  cursorPosition.value = e.target.selectionStart

  let formatted = '+7 ('
  if (input.length > 0) formatted += input.substring(0, 3)
  if (input.length >= 3) formatted += ') '
  if (input.length >= 6) formatted += input.substring(3, 6) + '-'
  else if (input.length > 3) formatted += input.substring(3, 6)
  if (input.length >= 8) formatted += input.substring(6, 8) + '-'
  else if (input.length > 6) formatted += input.substring(6, 8)
  if (input.length >= 10) formatted += input.substring(8, 10)
  else if (input.length > 8) formatted += input.substring(8, 10)

  phoneDisplay.value = formatted
  phone_number.value = '+7' + input.padEnd(10, '_').replace(/_/g, '')

  nextTick(() => {
    e.target.setSelectionRange(cursorPosition.value, cursorPosition.value)
  })
}

function handlePhoneDelete(e) {
  const startPos = e.target.selectionStart
  if (startPos <= 4) {
    e.preventDefault()
  }
  cursorPosition.value = startPos
}

async function sendForm() {
  try {
    if (
        !first_name.value ||
        !last_name.value ||
        !email.value ||
        !phone_number.value
    ) {
      alert('Заполните все поля!');
      return;
    }

    isSubmitting.value = true;

    const data = {
      first_name: first_name.value,
      last_name: last_name.value,
      email: email.value,
      phone_number: phone_number.value
    };

    // Отправка запроса
    await fetch('http://127.0.0.1/api/forms/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data),
    });

    first_name.value = '';
    last_name.value = '';
    email.value = '';
    phone_number.value = '';

    window.location.replace("http://127.0.0.1/");

  } catch (error) {
    console.error('Ошибка отправки:', error);
    alert('Произошла ошибка при отправке формы!');
  } finally {
    isSubmitting.value = false;
  }
}
</script>