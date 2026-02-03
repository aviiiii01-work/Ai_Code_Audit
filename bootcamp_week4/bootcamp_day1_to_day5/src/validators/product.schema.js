const Joi = require("joi");

const ProductSchema = Joi.object({
  title: Joi.string().min(3).max(100).required(),
  price: Joi.number().positive().required(),
  category: Joi.string().min(3).max(30).required(),
  inStock: Joi.boolean().default(true)
});

module.exports = ProductSchema;
