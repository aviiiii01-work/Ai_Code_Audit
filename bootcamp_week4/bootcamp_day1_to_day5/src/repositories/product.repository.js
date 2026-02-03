const Product = require("../models/Product");

exports.create = async (data) => {
  return await Product.create(data);
};

exports.findPaginated = async (page = 1, limit = 10) => {
  const skip = (page - 1) * limit;
  const products = await Product.find({ deletedAt: null })
    .skip(skip)
    .limit(limit);
  return products;
};

exports.findById = async (id) => {
  return await Product.findById(id);
};

exports.softDelete = async (id) => {
  return await Product.findByIdAndUpdate(id, { deletedAt: new Date() }, { new: true });
};
