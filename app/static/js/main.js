// js/main.js
document.addEventListener("DOMContentLoaded", () => {
  const ayvaText = document.querySelector(".ayva-text");
  const ayvaBubble = document.querySelector(".ayva-bubble");

  const messages = [
    "Hai, aku AYVA 👋",
    "Asisten AI yang siap bantu kamu 💡",
    "Lagi mikirin ide bisnis atau laporan keuangan?",
    "Ceritain aja, aku dengerin 🤍"
  ];

  let messageIndex = 0;
  let charIndex = 0;
  let typingSpeed = 50;

  function typeText() {
    if (charIndex < messages[messageIndex].length) {
      ayvaText.textContent += messages[messageIndex].charAt(charIndex);
      charIndex++;
      setTimeout(typeText, typingSpeed);
    } else {
      setTimeout(() => {
        ayvaText.textContent = "";
        charIndex = 0;
        messageIndex = (messageIndex + 1) % messages.length;
        typeText();
      }, 2500);
    }
  }

  // Mulai mengetik teks
  typeText();

  // Efek interaktif saat mouse bergerak
  document.addEventListener("mousemove", (e) => {
    const x = e.clientX / window.innerWidth - 0.5;
    const y = e.clientY / window.innerHeight - 0.5;
    ayvaBubble.style.transform = `translate(${x * 20}px, ${y * 20}px)`;
  });

  // Efek respon klik
  document.addEventListener("click", () => {
    ayvaBubble.classList.add("pulse");
    setTimeout(() => ayvaBubble.classList.remove("pulse"), 500);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const ayvaText = document.querySelector(".ayva-text");
  const ayvaBubble = document.querySelector(".ayva-bubble");

  const messages = [
    "Hai, aku AYVA 👋",
    "Asisten AI yang siap bantu kamu 💡",
    "Lagi mikirin ide bisnis atau laporan keuangan?",
    "Ceritain aja, aku dengerin 🤍"
  ];

  let messageIndex = 0;
  let charIndex = 0;
  let typingSpeed = 50;

  // 🔊 Efek suara ketikan lembut
  const typeSound = new Audio("assets/sounds/type.mp3");
  typeSound.volume = 0.2;

  function playTypeSound() {
    try {
      typeSound.currentTime = 0;
      typeSound.play();
    } catch (err) {
      // Beberapa browser butuh interaksi dulu sebelum audio bisa dimainkan
    }
  }

  function typeText() {
    if (charIndex < messages[messageIndex].length) {
      ayvaText.textContent += messages[messageIndex].charAt(charIndex);
      playTypeSound(); // mainkan suara tiap huruf
      charIndex++;
      setTimeout(typeText, typingSpeed);
    } else {
      setTimeout(() => {
        ayvaText.textContent = "";
        charIndex = 0;
        messageIndex = (messageIndex + 1) % messages.length;
        typeText();
      }, 2500);
    }
  }

  // Mulai mengetik teks
  typeText();

  // Efek interaktif saat mouse bergerak
  document.addEventListener("mousemove", (e) => {
    const x = e.clientX / window.innerWidth - 0.5;
    const y = e.clientY / window.innerHeight - 0.5;
    ayvaBubble.style.transform = `translate(${x * 20}px, ${y * 20}px)`;
  });

  // Efek respon klik
  document.addEventListener("click", () => {
    ayvaBubble.classList.add("pulse");
    setTimeout(() => ayvaBubble.classList.remove("pulse"), 500);

    // mainkan suara klik lembut
    const clickSound = new Audio("assets/sounds/click.mp3");
    clickSound.volume = 0.3;
    clickSound.play();
  });
});
 