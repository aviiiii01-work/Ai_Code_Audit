// storing products here once we fetch them
let allProducts = [];

// fetch products from DummyJSON
async function loadProducts() {
  try {
    const result = await fetch("https://dummyjson.com/products");
    const data = await result.json();

    allProducts = data.products || [];
    renderProducts(allProducts);

  } catch (err) {
    console.log("Error fetching products:", err);
  }
}

// create and push product cards into the grid
function renderProducts(list) {
  const grid = document.getElementById("productGrid");
  grid.innerHTML = "";

  list.forEach(item => {
    const card = document.createElement("div");
    card.className = "product-card";

    // picking a tag based on stock and discount
    let tagLabel = "";
    if (item.stock < 5) {
      tagLabel = `<span class="tag out">OUT OF STOCK</span>`;
    } else if (item.discountPercentage > 10) {
      tagLabel = `<span class="tag sale">SALE</span>`;
    } else {
      tagLabel = `<span class="tag new">NEW</span>`;
    }

    const starCount = Math.ceil(item.rating);   
    const stars = "*".repeat(starCount);     

    card.innerHTML = `
      ${tagLabel}
      <img src="${item.thumbnail}" alt="${item.title}">
      <p class="product-title">${item.title}</p>
      <p class="stars">${stars}</p>
      <p class="price">$${item.price}</p>
    `;

    grid.appendChild(card);
  });
}

// SEARCH FUNCTIONALITY
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", e => {
  const val = e.target.value.toLowerCase();
  const filtered = allProducts.filter(prod =>
    prod.title.toLowerCase().includes(val)
  );
  renderProducts(filtered);
});

// SORTING
const sortSelect = document.getElementById("sortSelect");
sortSelect.addEventListener("change", e => {
  const selected = e.target.value;

  // clone array so original doesn't get messed up
  const sorted = [...allProducts];

  if (selected === "high") {
    sorted.sort((a, b) => b.price - a.price);
  } else if (selected === "low") {
    sorted.sort((a, b) => a.price - b.price);
  }

  renderProducts(sorted);
});

// initial load
loadProducts();
