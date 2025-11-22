document.addEventListener("DOMContentLoaded", () => {

  // =========================
  // SIDEBAR NAVIGATION
  // =========================
  const navButtons = document.querySelectorAll(".nav button");
  const sections = document.querySelectorAll(".main-section");

  navButtons.forEach(button => {
    button.addEventListener("click", () => {
      const targetId = button.dataset.target;
      const targetSection = document.getElementById(targetId);

      if (!targetSection) return;

      sections.forEach(section => {
        section.style.display = "none";
        section.classList.remove("active");
      });

      targetSection.style.display = "block";
      targetSection.classList.add("active");

      navButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");
    });
  });


  // =========================
  // THEME TOGGLE
  // =========================
  const themeToggle = document.getElementById("themeToggle");

  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const current = document.body.getAttribute("data-theme");
      const next = current === "light" ? "dark" : "light";
      document.body.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      themeToggle.textContent = next === "light" ? "🌙" : "☀️";
    });

    const saved = localStorage.getItem("theme") || "light";
    document.body.setAttribute("data-theme", saved);
    themeToggle.textContent = saved === "light" ? "🌙" : "☀️";
  }


  // =========================
  // CHAT PARSER
  // =========================
  const chatForm = document.getElementById("chatForm");
  const chatInput = document.getElementById("chatInput");
  const chatBox = document.getElementById("chatBox");

  if (chatForm) {
    chatForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const text = chatInput.value.trim();
      if (!text) return;

      chatBox.innerHTML = `<div style="color:var(--muted)">⏳ Memproses chat...</div>`;

      try {
        const response = await fetch("/parse", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: text }) // Fix key to "text" to match backend expectation
        });

        const result = await response.json();

        if (result.message) { // Change from success to message to match backend response
          chatBox.innerHTML = `
            <div class="chat-result">
                <p><strong>Nama:</strong> ${result.data.nama_pelanggan || "-"}</p>
                <p><strong>Alamat:</strong> ${result.data.alamat_kirim || "-"}</p>
                <p><strong>Total:</strong> ${result.data.total_pembayaran || "-"}</p>
                <p><strong>Tag:</strong> ${result.data.tag_auto || "-"}</p>
            </div>
          `;
        } else {
          chatBox.innerHTML = `<div style="color:red">❌ Gagal memproses data</div>`;
        }

      } catch (err) {
        chatBox.innerHTML = `<div style="color:red">⚠️ Terjadi kesalahan server</div>`;
      }
    });
  }


  // =========================
  // DASHBOARD — STATISTIK
  // =========================
  const totalChat = document.getElementById("total-chat");
  const totalPelanggan = document.getElementById("total-pelanggan");
  const totalTransaksi = document.getElementById("total-transaksi");

  fetch("/stats")
    .then(res => res.json())
    .then(data => {
      if (!data) return;
      totalChat.textContent = data.total_chat || 0;
      totalPelanggan.textContent = data.total_pelanggan || 0;
      totalTransaksi.textContent = data.total_transaksi || 0;
    })
    .catch(() => console.warn("Gagal memuat statistik"));

});

function exportCSV(cleanedData) {
    const header = [
        "id_transaksi", "nama_pelanggan", "alamat_kirim",
        "nama_produk", "kuantitas", "harga_unit",
        "subtotal", "ongkir", "total_pembayaran", "tag_auto"
    ];

    let rows = [header];

    cleanedData.forEach(entry => {
        const items = entry.items || [];
        if (items.length > 0) {
            items.forEach(it => {
                rows.push([
                    entry.id_transaksi || "",
                    entry.nama_pelanggan || "",
                    entry.alamat_kirim || "",
                    it.nama_produk || "",
                    it.kuantitas || 0,
                    it.harga_unit || 0,
                    entry.subtotal || 0,
                    entry.ongkir || 0,
                    entry.total_pembayaran || 0,
                    entry.tag_auto || ""
                ]);
            });
        } else {
            rows.push([
                entry.id_transaksi || "",
                entry.nama_pelanggan || "",
                entry.alamat_kirim || "",
                "",
                0,
                0,
                entry.subtotal || 0,
                entry.ongkir || 0,
                entry.total_pembayaran || 0,
                entry.tag_auto || ""
            ]);
        }
    });

    // Convert array → CSV
    const csvContent = rows.map(e => e.join(";")).join("\n");

    // Blob download
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "ayva_export.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

