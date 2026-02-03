const ProductRepository = require("../repositories/product.repository");

exports.createProduct = async (req, res, next) => {
  try {
    const product = await ProductRepository.create(req.body);
    res.json(product);
  } catch (err) {
    next(err);
  }
};

exports.getProductsPaginated = async (req, res, next) => {
  try {
    const { page = 1, limit = 10 } = req.query;
    const products = await ProductRepository.findPaginated(page, limit);
    res.json(products);
  } catch (err) {
    next(err);
  }
};

exports.getProduct = async (req, res, next) => {
  try {
    const product = await ProductRepository.findById(req.params.id);
    if (!product) throw { status: 404, message: "Product not found" };
    res.json(product);
  } catch (err) {
    next(err);
  }
};

exports.deleteProduct = async (req, res, next) => {
  try {
    const product = await ProductRepository.softDelete(req.params.id);
    if (!product) throw { status: 404, message: "Product not found" };
    res.json(product);
  } catch (err) {
    next(err);
  }
};
