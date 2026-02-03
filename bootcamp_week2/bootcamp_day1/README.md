##  Stand Blog — Semantic HTML5 Layout  

###  Overview  
This project is part of **Week 2 – Day 1** of the Frontend Bootcamp.  
The goal was to build a **blog page using only semantic HTML5** elements — with **no CSS** and **no `<div>` tags** — to demonstrate understanding of page structure, accessibility, and semantic layout.  

---

###  Learning Outcomes  
- Learned the **fundamental structure** of an HTML5 page.  
- Used **semantic tags** (`<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<nav>`) instead of generic `<div>`s.  
- Built a **multi-section blog layout** that includes:
  - A header with navigation links.  
  - Featured posts section with multiple articles in a row.  
  - An introduction banner.  
  - A recent articles section with sidebar (search, recent posts, categories, and tags).  
- Practiced **accessibility features** like:
  - `aria-label` for screen readers.  
  - `alt` attributes for all images.  
  - Proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`).  
  - Use of `<time>` for dates.  

---

###  Structure Overview  
```
<header>        → Title + Navigation  
<main>
  <section>     → Featured Posts (3 articles with images)
  <section>     → Intro (about the blog)
  <section>     → Split layout (Recent Articles + Sidebar)
    <article>   → Individual blog entries
    <aside>     → Search, Categories, Recent Posts, Tags
</main>
<footer>        → Copyright info
```

---

###  Media Used  
All images are stored inside the local `/images` folder:
- `mountain_landscape.jpg`  
- `church-tower.jpg`  
- `html-website-templates.jpg`

---

###  Key Takeaways  
- Semantic HTML improves **readability, accessibility, and SEO**.  
- A well-structured layout can be meaningful even **without CSS**.  
- Accessibility and structure are as important as design.  

---

### 👨 Author  
**Ravi Pratap Singh**  
Trainee Software Engineer | HestaBit 
