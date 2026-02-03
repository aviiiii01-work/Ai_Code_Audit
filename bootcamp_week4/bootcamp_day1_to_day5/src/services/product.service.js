const ProductRepository = require("../repositories/product.repository");

class ProductService {
  static async createProduct(data) {
    return ProductRepository.create(data);
  }

  static async getProduct(id) {
    return ProductRepository.findById(id);
  }

  static async getProducts(query) {
    return ProductRepository.findPaginated(query);
  }

  static async deleteProduct(id) {
    return ProductRepository.softDelete(id);
  }
}

module.exports = ProductService;
