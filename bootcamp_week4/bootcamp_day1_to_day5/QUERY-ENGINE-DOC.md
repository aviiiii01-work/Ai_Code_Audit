# QUERY-ENGINE-DOC.md

## High-Performance REST API — Query Engine Documentation

1️⃣ Overview
This document explains the query engine implemented for the Product API. The engine supports: dynamic search, filtering, sorting, pagination, and soft deletes. It is designed for high-performance REST APIs following the Controller → Service → Repository pattern.

2️⃣ Dynamic Search
**Endpoint:** `GET /api/products`  
Supports searching product titles using case-insensitive regex: `/api/products?search=phone`  
Matches any product whose title contains `phone`. Search is case-insensitive.

3️⃣ Filtering
**Price Filtering:** `/api/products?minPrice=100&maxPrice=500`  
`minPrice` → products with price ≥ 100  
`maxPrice` → products with price ≤ 500  
Multiple filters can be combined with search: `/api/products?search=phone&minPrice=100&maxPrice=500`

4️⃣ Sorting
`/api/products?sort=price:desc`  
Format: `field:order`, order = `asc` or `desc`. Example: `sort=createdAt:asc`.

5️⃣ Pagination
Default page = 1, default limit = 10. Use `page` and `limit` query parameters: `/api/products?page=2&limit=5`  
skip = (page - 1) * limit  
limit = number of records per page

6️⃣ Soft Delete
Instead of deleting products permanently, set `deletedAt` timestamp: `DELETE /api/products/:id`  
Exclude deleted by default: `GET /api/products`  
Include deleted products: `GET /api/products?includeDeleted=true`

7️⃣ Error Handling
Global error middleware standardizes error responses:

```json
{
  "success": false,
  "message": "Product not found",
  "code": 404,
  "timestamp": "2025-11-27T09:00:00.000Z",
  "path": "/api/products/123"
}

8️⃣ Flow Diagram (Controller → Service → Repository)

[Controller] → receives request
│
▼
[Service] → business logic, validation
│
▼
[Repository] → interacts with MongoDB

Controller → Handles HTTP layer
Service → Applies business rules
Repository → Direct database operations

9️⃣ Notes

Queries are optimized with indexes: productSchema.index({ status: 1, createdAt: -1 })
Soft delete avoids data loss while keeping API performant
Supports advanced search, filter, sort, pagination, soft delete