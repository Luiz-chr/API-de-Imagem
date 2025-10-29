const API_URL = "http://127.0.0.1:8000";

async function carregarImagens(query = "") {
  const url = query ? `${API_URL}/search/${query}` : `${API_URL}/list/`;
  const res = await fetch(url);
  const data = await res.json();
  const gallery = document.getElementById("gallery");
  gallery.innerHTML = "";

  data.imagens.forEach(nome => {
    const container = document.createElement("div");
    container.className = "image-container";

    const img = document.createElement("img");
    img.src = `${API_URL}/download/${nome}`;

    const deleteBtn = document.createElement("button");
    deleteBtn.className = "delete-btn";
    deleteBtn.textContent = "X";
    deleteBtn.onclick = () => deletarImagem(nome);

    container.appendChild(img);
    container.appendChild(deleteBtn);
    gallery.appendChild(container);
  });
}

async function deletarImagem(filename) {
  if (confirm(`Deletar ${filename}?`)) {
    await fetch(`${API_URL}/delete/${filename}`, { method: "DELETE" });
    carregarImagens();
  }
}

function buscarImagens() {
  const query = document.getElementById("searchInput").value.trim();
  carregarImagens(query);
}

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("fileInput");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  
  await fetch(`${API_URL}/upload/`, {
    method: "POST",
    body: formData
  });
  fileInput.value = "";
  carregarImagens();
});

carregarImagens();
